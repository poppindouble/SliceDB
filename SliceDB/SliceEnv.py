from Schema import Schema
from SliceDB import SliceDB
import pickle
import os.path
class SliceEnv:
    envSchema = {}
    envDB = []
    def __init__(self):
        if not os.path.isfile("Data/Config.txt"):
            # add the default three tables
            sliceName = "CustDB"
            sliceFieldList = ["cust|INT" , "name|STRING" , "age|INT" , "phone|STRING" , "address|STRING"]
            indexName = "cust"
            custSchema = Schema(sliceName,sliceFieldList,indexName)
            SliceEnv.envSchema[sliceName] = custSchema
            
            sliceName = "SalesDB"
            sliceFieldList = ["order|INT" , "cust|INT" , "data|STRING" , "total|FLOAT"]
            indexName = "order"
            salesSchema = Schema(sliceName,sliceFieldList,indexName)
            SliceEnv.envSchema[sliceName] = salesSchema
            
            sliceName = "OrderDB"
            sliceFieldList = ["order|INT" , "item|STRING"]
            indexName = ""
            orderSchema = Schema(sliceName,sliceFieldList,indexName)
            SliceEnv.envSchema[sliceName] = orderSchema
            
            pickle.dump(SliceEnv.envSchema, open( "Data/Config.txt", "wb"))
        else:
            SliceEnv.envSchema = pickle.load(open("Data/Config.txt", "rb"))
    def createDB(self,sliceName,sliceFieldList,indexName):
        # SliceEnv.envSchema is the tables already existed in file, which is a map
        newSchema = Schema(sliceName,sliceFieldList,indexName)
        if newSchema.getSliceName() not in SliceEnv.envSchema:
            # create a new schema in the map
            SliceEnv.envSchema[newSchema.getSliceName()] = newSchema
            open("Data/" + sliceName + ".slc", 'w')
            print "create Sucessful"
        else:
            # update the existed schema
            if not os.path.isfile("Data/" + sliceName + ".slc"):
                open("Data/" + sliceName + ".slc", 'w')
                print "create Sucessful"
            SliceEnv.envSchema[sliceName] = newSchema
        pickle.dump(SliceEnv.envSchema, open( "Data/Config.txt", "wb"))
    def openDB(self,sliceName):
        if sliceName not in SliceEnv.envSchema:
            print "this DB is not existed"
            return False
        else:
            currentSchema = SliceEnv.envSchema[sliceName]
            try:
                currentDB = SliceDB(currentSchema)
                self.envDB.append(currentDB)
                return currentDB
            except:
                return False
    def closeDB(self,sliceName):
        file = open("Data/" + sliceName + ".slc","w")
        tempDB = None
        pickleData = pickle.load(open("Data/Config.txt", "rb"))
        currentSchema = pickleData[sliceName]
        for currentDB in self.envDB:
            if currentDB.schema.getSliceName() == sliceName:
                tempDB = currentDB
                break
        lastElement = len(currentSchema.getSliceFieldList()) - 1
        for tempRecord in tempDB.currentDB:
            for (counter,tempSliceField) in enumerate(currentSchema.getSliceFieldList()):
                if counter != lastElement:
                    file.write(str(tempRecord[tempSliceField.split("|")[0]]) + "|")
                else:
                    file.write(str(tempRecord[tempSliceField.split("|")[0]]))
            file.write('\n')
        file.close()
        self.envDB.remove(tempDB)
        tempDB.currentDB = None
        tempDB.custSchema = None