from pydantic import BaseModel
from app.config.mongo_config import libraryDatabase
from app.services.mongodb_service import MongoDbService

class LibrarySchema(BaseModel):
    student_name: str;
    books_taken: int;
    books_returned: int;
    
libraryModel = libraryDatabase["library"]
libraryService = MongoDbService(libraryModel)