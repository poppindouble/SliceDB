from SliceEnv import SliceEnv
from SliceDB import SliceDB
from SliceField import SliceField
import os
env = SliceEnv();
menuRunning = True
while menuRunning:
    print "1. Create database"
    print "2. Update Record"
    print "3. Add record"
    print "4. Delete Record"
    print "5. Bulk load"
    print "6. Display Join"
    print "7. Run Query"
    print "8. Report 1"
    print "9. Report 2"
    print "10. Exit"
    instruction = raw_input("plase enter an integer : ")
    try:
        instruction = int(instruction)
        if instruction == 1:
            tableName = raw_input("plase enter new table name : ")
            if tableName == "":
                print "you have to enter a name"
                continue
            numOfField = raw_input("count of the number of fields : ")
            try:
                numOfField = int(numOfField)
            except ValueError:
                print("That's not an Integer!")
                continue
            schemaList = []
            isLegalFormat = True
            for tempCount in range(0,numOfField):
                nameAndType = raw_input("please enter the name and type of each column : ")
                tempList = nameAndType.split("|")
                if not len(tempList) == 2:
                    print "format not right"
                    isLegalFormat = False
                    break
                tempName = tempList[0]
                tempType = tempList[1]
                if tempName == "":
                    print "you have to give a name of the field"
                    isLegalFormat = False
                    break
                if not (tempType == "STRING" or tempType == "INT" or tempType == "FLOAT"):
                    print "type not valid"
                    isLegalFormat = False
                    break
                schemaList.append(nameAndType)
            if isLegalFormat == True:
                isLegalIndex = False
                indexColumnName = raw_input("enter the index name : ")
                if indexColumnName == "":
                    env = SliceEnv();
                    env.createDB(tableName,schemaList,"")
                else:
                    for tempNameAndType in schemaList:
                        tempName = tempNameAndType.split("|")[0]
                        if tempName == indexColumnName:
                            isLegalIndex = True
                            break
                    if isLegalIndex == False:
                        print "this index is not legal"
                        pass
                    else:
                        env.createDB(tableName,schemaList,indexColumnName)
            else:
                continue
        elif instruction == 2:
            tableName = raw_input("plase enter table name : ")
            if tableName == "":
                print "you have to enter a name"
                continue
            currentDB = env.openDB(tableName)
            if currentDB == False:
                print "open database failed"
            else:
                if currentDB.schema.getIndexName() == "":
                    print "this table has no index, so please select add function"
                    continue
                else:
                    if currentDB.updateRecord() == False:
                        print "the record is not legal"
                        continue
                    else:
                        env.closeDB(tableName)
                        print "update success"
        elif instruction == 3:
            tableName = raw_input("please enter table name : ")
            if tableName == "":
                print "you have to enter a name"
                continue
            currentDB = env.openDB(tableName)
            if currentDB == False:
                print "open database failed"
            else:
                if currentDB.addRecord() == False:
                    print "the record is not legal"
                    continue
                else:
                    env.closeDB(tableName)
                    print "add success"
        elif instruction == 4:
            tableName = raw_input("please enter table name : ")
            if tableName == "":
                print "you have to enter a name"
                continue
            currentDB = env.openDB(tableName)
            if currentDB == False:
                print "open database failed"
            else:
                if currentDB.deleteRecord() == False:
                    continue
                else:
                    env.closeDB(tableName)
                    print "delete success"
        elif instruction == 5:
            tableName = raw_input("please enter the table name : ")
            if tableName == "":
                print "you have to give a name"
                continue
            currentDB = env.openDB(tableName)
            if currentDB == False:
                print "open database failed, please create the database first"
            else:
                if currentDB.bulkLoad() == False:
                    continue
                else:
                    env.closeDB(tableName)
                    print "bulk load success"
        elif instruction == 6:
            tableName = raw_input("please enter the table name as the base table : ")
            if tableName == "":
                print "you have to give a name"
                continue
            baseDB = env.openDB(tableName)
            if baseDB == False:
                print "open database failed"
            else:
                tableName = raw_input("please enter the table name as the join table : ")
                if tableName == "":
                    print "you have to give a name"
                    continue
                else:
                    joinDB = env.openDB(tableName)
                    if joinDB == False:
                        print "open database failed"
                        continue
                    else:
                        if baseDB.natureJoin(joinDB) == False:
                            print "join failed"
    
        elif instruction == 7:
            tableName = raw_input("please enter table name : ")
            if tableName == "":
                print "you have to enter a name"
                continue
            currentDB = env.openDB(tableName)
            if currentDB == False:
                print "opend database failed"
            else:
                if currentDB.runQuery() == False:
                    continue
                else:
                    pass
                env.closeDB(tableName)
        elif instruction == 8:
            print "i wrote this program on mac, there is no exe file in mac,if it is not working, run it in the terminal, the source code is under the folder of Haskell"
            print (os.system("Data/Report.exe"))
        elif instruction == 9:
            print "i wrote this program on mac, there is no exe file in mac,if it is not working, run it in the terminal, the source code is under the folder of Haskell"
            print (os.system("Data/GroupByReport.exe"))
        elif instruction == 10:
            menuRunning = False
    except ValueError:
        pass