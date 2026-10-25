import uuid
import asyncio
from datetime import datetime
from sqlalchemy.orm import Session
from .models import GenerationJob, Asset
from .database import get_db
from ..providers.provider_manager import provider_manager
from ..providers.base import GenerationParams

class JobManager:
    def __init__(self, asset_manager):
        self.asset_manager = asset_manager

    async def create_job(self, db: Session, user_id: int, project_id: int, mode: str, params: GenerationParams, inputs: dict) -> str:
        job_id = str(uuid.uuid4())
        new_job = GenerationJob(
            id=job_id,
            user_id=user_id,
            project_id=project_id,
            status="pending",
            mode=mode,
            params_json=params.dict(),
            inputs_json=inputs
        )
        db.add(new_job)
        db.commit()
        return job_id

    async def run_job(self, db: Session, job_id: str, provider_id: str):
        job = db.query(GenerationJob).filter(GenerationJob.id == job_id).first()
        if not job:
            return

        try:
            job.status = "processing"
            job.started_at = datetime.utcnow()
            db.commit()

            provider = provider_manager.get_provider(provider_id)
            params = GenerationParams(**job.params_json)

            # 1. Submit
            submission = await provider.submit_job(params)

            # 2. Poll for status
            while True:
                status_res = await provider.get_job_status(submission.job_id)
                if status_res.status == "completed":
                    break
                if status_res.status == "failed":
                    raise Exception(status_res.error_message or "Provider failed")

                await asyncio.sleep(2)

            # 3. Retrieve Result
            result = await provider.retrieve_result(submission.job_id)

            # 4. Save Asset
            # In a real provider, we'd download the bytes from result.url
            # For now, we simulate the binary save
            asset_id = str(uuid.uuid4())
            # Simulating binary content download
            await self.asset_manager.save_asset(b"fake_binary_content", f"{asset_id}.png")

            new_asset = Asset(
                id=asset_id,
                project_id=job.project_id,
                user_id=job.user_id,
                type="image" if "image" in job.mode else "video",
                storage_url=result.url,
                metadata_json=result.metadata
            )
            db.add(new_asset)

            job.output_asset_id = asset_id
            job.status = "completed"
            job.completed_at = datetime.utcnow()
            db.commit()

        except Exception as e:
            job.status = "failed"
            job.error_message = str(e)
            db.commit()
