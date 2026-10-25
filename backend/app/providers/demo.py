import asyncio
import uuid
import random
from .base import AIProvider, GenerationParams, JobSubmissionResponse, JobStatusResponse, AssetResult, ModelCapabilities

class DemoProvider(AIProvider):
    def __init__(self):
        self._jobs = {}

    @property
    def id(self) -> str:
        return "demo"

    @property
    def name(self) -> str:
        return "Striker Demo Engine"

    @property
    def capabilities(self) -> ModelCapabilities:
        return ModelCapabilities(
            t2i=True, i2i=True, t2v=True, i2v=True,
            motion_transfer=True, object_swap=True, video_restyle=True
        )

    async def submit_job(self, params: GenerationParams) -> JobSubmissionResponse:
        job_id = str(uuid.uuid4())
        self._jobs[job_id] = {
            "status": "pending",
            "progress": 0.0,
            "result_url": f"https://placehold.co/1024x1024?text=Demo+Result+{job_id[:8]}"
        }

        # Simulate async processing
        asyncio.create_task(self._simulate_generation(job_id))

        return JobSubmissionResponse(
            job_id=job_id,
            provider_job_id=f"demo_{job_id}",
            estimated_time=10
        )

    async def _simulate_generation(self, job_id: str):
        job = self._jobs[job_id]
        job["status"] = "processing"

        for i in range(1, 11):
            await asyncio.sleep(1)
            job["progress"] = i / 10.0

        job["status"] = "completed"

    async def get_job_status(self, job_id: str) -> JobStatusResponse:
        job = self._jobs.get(job_id)
        if not job:
            return JobStatusResponse(status="failed", progress=0.0, error_message="Job not found")

        return JobStatusResponse(
            status=job["status"],
            progress=job["progress"],
            error_message=None if job["status"] != "failed" else "Demo error occurred"
        )

    async def cancel_job(self, job_id: str) -> None:
        if job_id in self._jobs:
            self._jobs[job_id]["status"] = "cancelled"

    async def retrieve_result(self, job_id: str) -> AssetResult:
        job = self._jobs.get(job_id)
        if not job or job["status"] != "completed":
            raise Exception("Result not available yet")

        return AssetResult(
            url=job["result_url"],
            metadata={"width": 1024, "height": 1024, "format": "png"}
        )
