from fastapi import APIRouter

router = APIRouter()
@router.get("./fetch_all_exchanges/")
async def fetch_all_exchanges():
 return {"message":"Exchange data"}