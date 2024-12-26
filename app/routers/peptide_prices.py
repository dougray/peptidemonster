from fastapi import APIRouter

router = APIRouter()

@router.get("/peptide-prices")
async def get_peptide_prices():
    return {"message": "List of peptide prices will be here."}

@router.get("/peptide-prices/{peptide_id}")
async def get_peptide_price(peptide_id: int):
    return {"peptide_id": peptide_id, "price": "Price details will be here."}