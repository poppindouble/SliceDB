class SliceDB:
    INT = "INT_TYPE"
    STRING = "STRING_TYPE"
    DOUBLE = "DOUBLE_TYPE"
    def __init__(self,schema):
        self.schema = schema
        self.currentDB = []
        if self.schema.getSliceName() == "CustDB" or self.schema.getSliceName() == "OrderDB" or self.schema.getSliceName() == "SalesDB":
            try:
                file = open("Data/" + self.schema.getSliceName() + ".slc")
                content = file.readlines()
                fieldName = []
                fieldType = []
                keyValueList = []
                currentSliceFieldList = self.schema.getSliceFieldList()
                for singleField in currentSliceFieldList:
                    fieldName.append(singleField.split("|")[0])
                    fieldType.append(singleField.split("|")[1])
                for line in content:
                    try:
                        tempRecord = {}
                        tempList = [x.strip() for x in line.split('|')]
                        for count in range(len(fieldName)):
                            if tempList[count] == "":
                                if fieldName[count] == self.schema.getIndexName():
                                    tempRecord[fieldName[count]] = int(tempList[count])
                                else:
                                    tempRecord[fieldName[count]] = ""
                            elif fieldType[count] == "INT":
                                tempList[count] = int(tempList[count])
                                if fieldName[count] == self.schema.getIndexName():
                                    if tempList[count] in keyValueList:
                                        raise Exception()
                                    else:
                                        keyValueList.append(tempList[count])
                                        tempRecord[fieldName[count]] = tempList[count]
                                else:
                                    tempRecord[fieldName[count]] = tempList[count]
                            elif fieldType[count] == "STRING":
                                if fieldName[count] == self.schema.getIndexName():
                                    if tempList[count] in keyValueList:
                                        raise Exception()
                                    else:
                                        keyValueList.append(tempList[count])
                                        tempRecord[fieldName[count]] = tempList[count]
                                else:
                                    tempRecord[fieldName[count]] = tempList[count]
                            elif fieldType[count] == "FLOAT":
                                tempList[count] = float(tempList[count])
                                if fieldName[count] == self.schema.getIndexName():
                                    if tempList[count] in keyValueList:
                                        raise Exception()
                                    else:
                                        keyValueList.append(tempList[count])
                                        tempRecord[fieldName[count]] = tempList[count]
                                else:
                                    tempRecord[fieldName[count]] = tempList[count]
                        self.currentDB.append(tempRecord)
                    except:
                        continue
                file.close()

            except:
                print "no such " + self.schema.getSliceName() + ".slc file, i will create a empty table for you"
                open("Data/" + self.schema.getSliceName() + ".slc", 'w')
        else:
            file = open("Data/" + self.schema.getSliceName() + ".slc")
            content = file.readlines()
            fieldName = []
            fieldType = []
            currentSliceFieldList = self.schema.getSliceFieldList()
            for singleField in currentSliceFieldList:
                fieldName.append(singleField.split("|")[0])
                fieldType.append(singleField.split("|")[1])
            for line in content:
                try:
                    tempRecord = {}
                    tempList = [x.strip() for x in line.split('|')]
                    for count in range(len(fieldName)):
                        if tempList[count] == "":
                            if fieldName[count] == self.schema.getIndexName():
                                tempRecord[fieldName[count]] = int(tempList[count])
                            else:
                                tempRecord[fieldName[count]] = ""
                        elif fieldType[count] == "INT":
                            tempRecord[fieldName[count]] = int(tempList[count])
                        elif fieldType[count] == "STRING":
                            tempRecord[fieldName[count]] = tempList[count]
                        elif fieldType[count] == "FLOAT":
                            tempRecord[fieldName[count]] = float(tempList[count])
                    self.currentDB.append(tempRecord)
                except:
                    continue
            file.close()


    def updateRecord(self):
        newRecord = {}
        for currentField in self.schema.getSliceFieldList():
            newValue = raw_input("plase enter the value for " + currentField.split("|")[0] + " : ")
            if currentField.split("|")[0] == self.schema.getIndexName():
                if newValue == "":
                    print "you have to offer the index value"
                    return False
                else:
                    if currentField.split("|")[1] == "INT":
                        try:
                            newValue = int(newValue)
                            newRecord[currentField.split("|")[0]] = newValue
                        except:
                            print "It must be a INT"
                            return False
                    elif currentField.split("|")[1] == "STRING":
                        newRecord[currentField.split("|")[0]] = newValue
                    elif currentField.split("|")[1] == "FLOAT":
                        try:
                            newValue = float(newValue)
                            newRecord[currentField.split("|")[0]] = newValue
                        except:
                            print "It must be a FLOAT"
                            return False
            elif newValue == "":
                newRecord[currentField.split("|")[0]] = newValue
            elif currentField.split("|")[1] == "INT":
                try:
                    newValue = int(newValue)
                    newRecord[currentField.split("|")[0]] = newValue
                except:
                    print "It must be a INT"
                    return False
            elif currentField.split("|")[1] == "STRING":
                newRecord[currentField.split("|")[0]] = newValue
            elif currentField.split("|")[1] == "FLOAT":
                try:
                    newValue = float(newValue)
                    newRecord[currentField.split("|")[0]] = newValue
                except:
                    print "It must be a FLOAT"
                    return False
        findRecord = False
        for (line,currentRecord) in enumerate(self.currentDB):
            if currentRecord[self.schema.getIndexName()] == newRecord[self.schema.getIndexName()]:
                findRecord = True
                self.currentDB[line] = newRecord
                break
        if findRecord == False:
            return False
        else:
            return True

    def addRecord(self):
        newRecord = {}
        keyValueList = []
        if self.schema.getIndexName() != "":
            for currentRecord in self.currentDB:
                keyValueList.append(currentRecord[self.schema.getIndexName()])
        for currentField in self.schema.getSliceFieldList():
            newValue = raw_input("plase enter the value for " + currentField.split("|")[0] + " : ")
            if currentField.split("|")[0] == self.schema.getIndexName():
                if newValue == "":
                    if currentField.split("|")[1] == "INT":
                        newValue = max(keyValueList) + 1
                        newRecord[currentField.split("|")[0]] = newValue
                    else:
                        print "the index is not a type of INT, this system can not automaticaly generate a number as the index key, u have to offer a index key"
                        return False
                else:
                    if currentField.split("|")[1] == "INT":
                        try:
                            newValue = int(newValue)
                            newRecord[currentField.split("|")[0]] = newValue
                        except:
                            print "It must be a INT"
                            return False
                    elif currentField.split("|")[1] == "STRING":
                        newRecord[currentField.split("|")[0]] = newValue
                    elif currentField.split("|")[1] == "FLOAT":
                        try:
                            newValue = float(newValue)
                            newRecord[currentField.split("|")[0]] = newValue
                        except:
                            print "It must be a FLOAT"
                            return False
            elif newValue == "":
                newRecord[currentField.split("|")[0]] = newValue
            elif currentField.split("|")[1] == "INT":
                try:
                    newValue = int(newValue)
                    newRecord[currentField.split("|")[0]] = newValue
                except:
                    print "It must be a INT"
                    return False
            elif currentField.split("|")[1] == "STRING":
                newRecord[currentField.split("|")[0]] = newValue
            elif currentField.split("|")[1] == "FLOAT":
                try:
                    newValue = float(newValue)
                    newRecord[currentField.split("|")[0]] = newValue
                except:
                    print "It must be a FLOAT"
                    return False
        if self.schema.getIndexName() == "":
            self.currentDB.append(newRecord)
            return True
        else:
            findRecord = False
            for (line,currentRecord) in enumerate(self.currentDB):
                if currentRecord[self.schema.getIndexName()] == newRecord[self.schema.getIndexName()]:
                    findRecord = True
                    break
            if findRecord == False:
                self.currentDB.append(newRecord)
                return True
            else:
                print "this index key already existed, please use update"
                return False



    def deleteRecord(self):
        if self.schema.getIndexName() == "":
            print "this table does not have a key value"
            return False
        else:
            keyValue = raw_input("plase enter the value for " + self.schema.getIndexName() + " : ")
            currentSliceFieldList = self.schema.getSliceFieldList()
            for currentField in currentSliceFieldList:
                if currentField.split("|")[0] == self.schema.getIndexName():
                    keyType = currentField.split("|")[1]
                    break
            if keyType == "INT":
                try:
                    keyValue = int(keyValue)
                except:
                    print "It must be a INT"
                    return False
            if keyType == "STRING":
                try:
                    keyValue = str(keyValue)
                except:
                    print "It must be a STRING"
                    return False
            if keyType == "FLOAT":
                try:
                    keyValue = float(keyValue)
                except:
                    print "It must be a FLOAT"
                    return False
            recordFind = False
            for currentRecord in self.currentDB:
                if currentRecord[self.schema.getIndexName()] == keyValue:
                    self.currentDB.remove(currentRecord)
                    recordFind = True
                    break
            if recordFind == True:
                return True
            elif recordFind == False:
                print "There is not such keyValue"
                return False

    def bulkLoad(self):
        newFileName = raw_input("plase enter the file name : ")
        try:
            file = open("Data/" + newFileName + ".apd")
        except:
            print "this file is not existed"
            return False
        content = file.readlines()
        self.currentDB = []
        fieldName = []
        fieldType = []
        keyValueList = []
        currentSliceFieldList = self.schema.getSliceFieldList()
        for singleField in currentSliceFieldList:
            fieldName.append(singleField.split("|")[0])
            fieldType.append(singleField.split("|")[1])
        for line in content:
            try:
                tempRecord = {}
                tempList = [x.strip() for x in line.split('|')]
                for count in range(len(fieldName)):
                    if tempList[count] == "":
                        if fieldName[count] == self.schema.getIndexName():
                            tempRecord[fieldName[count]] = int(tempList[count])
                        else:
                            tempRecord[fieldName[count]] = ""
                    elif fieldType[count] == "INT":
                        tempList[count] = int(tempList[count])
                        if fieldName[count] == self.schema.getIndexName():
                            if tempList[count] in keyValueList:
                                raise Exception()
                            else:
                                keyValueList.append(tempList[count])
                                tempRecord[fieldName[count]] = tempList[count]
                        else:
                            tempRecord[fieldName[count]] = tempList[count]
                    elif fieldType[count] == "STRING":
                        if fieldName[count] == self.schema.getIndexName():
                            if tempList[count] in keyValueList:
                                raise Exception()
                            else:
                                keyValueList.append(tempList[count])
                                tempRecord[fieldName[count]] = tempList[count]
                        else:
                            tempRecord[fieldName[count]] = tempList[count]
                    elif fieldType[count] == "FLOAT":
                        tempList[count] = float(tempList[count])
                        if fieldName[count] == self.schema.getIndexName():
                            if tempList[count] in keyValueList:
                                raise Exception()
                            else:
                                keyValueList.append(tempList[count])
                                tempRecord[fieldName[count]] = tempList[count]
                        else:
                            tempRecord[fieldName[count]] = tempList[count]
                self.currentDB.append(tempRecord)
            except:
                continue
        file.close()
    def runQuery(self):
        resultDB = []
        selectColumns = raw_input("plase enter the columns you want to display : ")
        fieldList = [x.strip() for x in selectColumns.split('|')]
        schemaNameList = []
        for currentField in self.schema.getSliceFieldList():
            schemaNameList.append(currentField.split("|")[0])
        fieldNotFound = False
        for tempField in fieldList:
            if tempField not in schemaNameList:
                fieldNotFound = True
                break
        if fieldNotFound == True:
            print "some of the column you offer is not in the schema"
            return False
        condition = raw_input("plase enter the condition : ")
        conditionList = [x.strip() for x in condition.split('|')]
        if len(conditionList) != 3:
            print "this condition is not legal, we only support single condition"
            return False
        if conditionList[1] != "EQ" and conditionList[1] != "LT" and conditionList[1] != "GT":
            print "this operator is not legal"
            return False
        for currentField in self.schema.getSliceFieldList():
            if currentField.split("|")[0] == conditionList[0]:
                conditionType = currentField.split("|")[1]
                break
        if conditionType == "INT":
            try:
                literalValue = int(conditionList[2])
            except:
                print "the literal value is not the right type"
                return False
        elif conditionType == "STRING":
            literalValue = conditionList[2]
        elif conditionType == "FLOAT":
            try:
                literalValue = float(conditionList[2])
            except:
                print "the literal value is not the right type"
                return False
        conditionField = conditionList[0]
        conditionOperator = conditionList[1]
        for currentRecord in self.currentDB:
            if conditionType == "INT":
                if conditionOperator == "EQ":
                    if currentRecord[conditionField] == literalValue:
                        resultDB.append(currentRecord)
                    else:
                        pass
                elif conditionOperator == "LT":
                    if currentRecord[conditionField] < literalValue:
                        resultDB.append(currentRecord)
                    else:
                        pass
                elif conditionOperator == "GT":
                    if currentRecord[conditionField] > literalValue:
                        resultDB.append(currentRecord)
                    else:
                        pass
            elif conditionType == "STRING":
                if conditionOperator == "EQ":
                    if currentRecord[conditionField] == literalValue:
                        resultDB.append(currentRecord)
                    else:
                        pass
                elif conditionOperator == "LT":
                    print "this system does not support string less then operation"
                    return False
                elif conditionOperator == "GT":
                    print "this system does not support string less then operation"
                    return False
            elif conditionType == "FLOAT":
                if conditionOperator == "EQ":
                    if currentRecord[conditionField] == literalValue:
                        resultDB.append(currentRecord)
                    else:
                        pass
                elif conditionOperator == "LT":
                    if currentRecord[conditionField] < literalValue:
                        resultDB.append(currentRecord)
                    else:
                        pass
                elif conditionOperator == "GT":
                    if currentRecord[conditionField] > literalValue:
                        resultDB.append(currentRecord)
                    else:
                        pass
        for currentRecord in resultDB:
            resultRecord = ""
            for tempSliceField in self.schema.getSliceFieldList():
                for tempName in fieldList:
                    if tempName == tempSliceField.split("|")[0]:
                        resultRecord = resultRecord + str(currentRecord[tempName]) + "|"
            print resultRecord
        return True

    def natureJoin(self,joinDB):
        joinColumn = raw_input("please input the name of join column : ")
        baseDBFieldNames = []
        baseDBFieldTypes = []
        joinDBFieldNames = []
        joinDBFieldTypes = []
        resultDB = []
        for currentField in self.schema.getSliceFieldList():
            baseDBFieldNames.append(currentField.split("|")[0])
            baseDBFieldTypes.append(currentField.split("|")[1])
        for currentField in joinDB.schema.getSliceFieldList():
            joinDBFieldNames.append(currentField.split("|")[0])
            joinDBFieldTypes.append(currentField.split("|")[1])
        if joinColumn not in baseDBFieldNames or joinColumn not in joinDBFieldNames:
            print "it is not a common column"
            return False
        for baseRecord in self.currentDB:
            for joinRecord in joinDB.currentDB:
                if baseRecord[joinColumn] == joinRecord[joinColumn]:
                    tempJoinRecord = ""
                    for currentField in baseDBFieldNames:
                        tempJoinRecord = tempJoinRecord + str(baseRecord[currentField]) + "|"
                    for currentField in joinDBFieldNames:
                        if currentField != joinColumn:
                            tempJoinRecord = tempJoinRecord + str(joinRecord[currentField]) + "|"
                    resultDB.append(tempJoinRecord)
        for resultRecord in resultDB:
            print resultRecord






