from fastapi import FastAPI, Depends, HTTPException, BackgroundTasks, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session
from typing import List, Optional
from pydantic import BaseModel

from .core.database import get_db
from .core.models import User, Project, GenerationJob, Asset
from .core.asset_manager import AssetManager
from .core.job_manager import JobManager
from .providers.provider_manager import provider_manager
from .providers.base import GenerationParams
from .core.exceptions import global_exception_handler
from .core.auth import verify_api_key

app = FastAPI(title="Striker2.1 API")

app.add_exception_handler(Exception, global_exception_handler)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Dependencies
asset_manager = AssetManager()
job_manager = JobManager(asset_manager)

# Request Schemas
class JobRequest(BaseModel):
    project_id: int
    user_id: int
    mode: str
    params: GenerationParams
    inputs: dict = {}
    provider_id: str = "demo"

class ProjectCreate(BaseModel):
    user_id: int
    name: str
    description: Optional[str] = None

@app.get("/")
async def root():
    return {"message": "Welcome to Striker2.1 AI Creative Studio API"}

@app.get("/providers")
async def list_providers():
    return provider_manager.list_providers()

@app.post("/projects")
async def create_project(proj: ProjectCreate, db: Session = Depends(get_db), auth=Depends(verify_api_key)):
    project = Project(user_id=proj.user_id, name=proj.name, description=proj.description)
    db.add(project)
    db.commit()
    db.refresh(project)
    return project

@app.get("/projects")
async def list_projects(user_id: int, db: Session = Depends(get_db), auth=Depends(verify_api_key)):
    return db.query(Project).filter(Project.user_id == user_id).all()

@app.post("/jobs")
async def submit_job(req: JobRequest, background_tasks: BackgroundTasks, db: Session = Depends(get_db), auth=Depends(verify_api_key)):
    job_id = await job_manager.create_job(db, req.user_id, req.project_id, req.mode, req.params, req.inputs)

    # Run the job in background
    background_tasks.add_task(job_manager.run_job, db, job_id, req.provider_id)

    return {"job_id": job_id, "status": "pending"}

@app.get("/jobs/{job_id}")
async def get_job(job_id: str, db: Session = Depends(get_db), auth=Depends(verify_api_key)):
    job = db.query(GenerationJob).filter(GenerationJob.id == job_id).first()
    if not job:
        raise HTTPException(status_code=404, detail="Job not found")
    return job
