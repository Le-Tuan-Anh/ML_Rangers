from fastapi import APIRouter, HTTPException, BackgroundTasks
from api.request import Request
from api.response import Response
from core.phase1 import Prob1Model, Prob2Model


router = APIRouter()

@router.post("/1/predict", response_model=Response)
def phase1_prob1(request: Request) -> Response:
    try:
        model = Prob1Model()
        response = model.infer(request=request)
        return response
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
@router.post("/2/predict", response_model=Response)
def phase1_prob1(request: Request) -> Response:
    try:
        model = Prob2Model()
        response = model.infer(request=request)
        return response
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))