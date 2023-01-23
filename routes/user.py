from fastapi import APIRouter, HTTPException
from database import collection
from models import Blog

router = APIRouter(
    prefix ="/blog",
    tags=['Blogs'])

@router.get('/allblogs')
async def get_blogs():
    blogs = []
    cursor = collection.find({})
    for document in cursor:
        blogs.append(Blog(**document))
    return blogs

@router.get('/{id}',response_model=Blog)
async def get_blog(id:int):
    document = collection.find_one({"id": id})
    if not document:
         raise HTTPException(404, f"There is no blog with the id {id}")
    return document

@router.post("/createblog", response_model=Blog)
async def post_blog(blog: Blog):
    document = blog.dict()
    collection.insert_one(document)
    if document:
        return document
    raise HTTPException(400, "Something went wrong")

@router.put("/{id}", response_model=Blog)
async def put_blog(id:int , title: str, body: str):    
    document = collection.find_one({"id": id})
    if document:
        collection.update_one({"id": id}, {"$set": {"title": title,"body": body}})
        return document
    raise HTTPException(404, f"There is no blog with the id {id}")

@router.delete("/{id}")
async def delete_blog(id:int ):

    document = collection.find_one({"id": id})
    if not document:
         raise HTTPException(404, f"There is no blog with the id {id}")
    document = collection.delete_one({"id": id})
    return f"Successfully deleted blog with id {id}"
    