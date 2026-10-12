

from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session

from app.database import SessionLocal
from app.models import Job
from app.schemas import JobCreate, JobResponse

app = FastAPI(title="Background Job Processing Platform")


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/")
def home():
    return {"message": "Background Job Processing Platform is running"}


@app.post("/jobs", response_model=JobResponse, status_code=201)
def create_job(job_data: JobCreate, db: Session = Depends(get_db)):
    new_job = Job(
        task_name=job_data.task_name,
        status="pending",
    )

    db.add(new_job)
    db.commit()
    db.refresh(new_job)

    return new_job


@app.get("/jobs", response_model=list[JobResponse])
def list_jobs(db: Session = Depends(get_db)):
    jobs = db.query(Job).order_by(Job.id.desc()).all()
    return jobs
