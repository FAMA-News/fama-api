from fastapi import APIRouter, Depends, HTTPException, status

# Declare Router
router = APIRouter()

@router.get("/status")
def system_status():
    return {"isUp": True}