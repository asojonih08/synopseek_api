from fastapi import APIRouter
from models.search import SearchRequest

router = APIRouter()

@router.post("/search")
async def search_and_synopsis(request: SearchRequest):
     pass
