class Schema:
    def __init__(self,sliceName,sliceFieldList,indexName):
        self.sliceName = sliceName
        self.sliceFieldList = sliceFieldList
        self.indexName = indexName

    def setSliceName(self,sliceName):
        self.setSliceName = sliceName

    def setSliceFieldList(self,sliceFieldList):
        self.setSliceFieldList = setSliceFieldList

    def setIndexName(self,indexName):
        self.indexName = indexName

    def getSliceName(self):
        return self.sliceName

    def getSliceFieldList(self):
        return self.sliceFieldList

    def getIndexName(self):
        return self.indexName