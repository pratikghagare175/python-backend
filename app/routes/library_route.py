from fastapi import APIRouter
from bson import ObjectId
from app.models.library_model import LibrarySchema,libraryService
router = APIRouter()

@router.get("/students/{student_id}")
async def read_student(student_id: str):
    filter = {"_id":ObjectId(student_id)}
    result = await libraryService.readDocument(filter)
    return {"success":True,"message":"Student Data Fetched Successfully","data":result}

@router.post("/students/create")
async def create_student(body:LibrarySchema):
    document = body.dict()
    await libraryService.createDocument(document)
    return {"success":True,"message":"Student Created Successfully"}

@router.put("/student/update")
async def update_student(student_id:str,body:LibrarySchema):
    filter = {"_id":ObjectId(student_id)}
    updateQuery = {"$set":{}}