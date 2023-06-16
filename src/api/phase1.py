import logging
from api.request import Request
from api.response import Response
from core.save_test import save_test
from core.phase1 import Prob1Model, Prob2Model
from fastapi import APIRouter, HTTPException, BackgroundTasks


router = APIRouter()
logger = logging.getLogger("ml_ranger_logger")

@router.post("/prob-1/predict", response_model=Response)
async def phase1_prob1(request: Request, background_task: BackgroundTasks) -> Response:
    try:
        model = Prob1Model()
        response = model.infer(request=request)
        background_task.add_task(save_test, request, response, 'phase-1', 'prob-1')
        return response
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
@router.post("/prob-2/predict", response_model=Response)
async def phase1_prob2(request: Request, background_task: BackgroundTasks) -> Response:
    try:
        model = Prob2Model()
        response = model.infer(request=request)
        background_task.add_task(save_test, request, response, 'phase-1', 'prob-2')
        return response
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))