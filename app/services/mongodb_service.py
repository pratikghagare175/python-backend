
class MongoDbService:
    def __init__(self, model):
        self.model = model
    
    async def createDocument(self,document):
        result = await self.model.insert_one(document)
        return result
        
    async def readDocument(self,filter):
       result = await self.model.find_one(filter);
       return result;