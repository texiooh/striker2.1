from abc import ABC, abstractmethod
from typing import Any, Dict, Optional
from pydantic import BaseModel

class GenerationParams(BaseModel):
    prompt: str
    negative_prompt: Optional[str] = None
    aspect_ratio: str = "1:1"
    seed: Optional[int] = None
    ref_image_ids: list[str] = []
    source_video_id: Optional[str] = None
    duration: Optional[int] = None # for video

class JobSubmissionResponse(BaseModel):
    job_id: str
    provider_job_id: str
    estimated_time: int # seconds

class JobStatusResponse(BaseModel):
    status: str # "pending", "processing", "completed", "failed"
    progress: float # 0.0 to 1.0
    error_message: Optional[str] = None

class AssetResult(BaseModel):
    url: str
    metadata: Dict[str, Any]

class ModelCapabilities(BaseModel):
    t2i: bool = False
    i2i: bool = False
    t2v: bool = False
    i2v: bool = False
    motion_transfer: bool = False
    object_swap: bool = False
    video_restyle: bool = False

class AIProvider(ABC):
    @property
    @abstractmethod
    def id(self) -> str:
        pass

    @property
    @abstractmethod
    def name(self) -> str:
        pass

    @property
    @abstractmethod
    def capabilities(self) -> ModelCapabilities:
        pass

    @abstractmethod
    async def submit_job(self, params: GenerationParams) -> JobSubmissionResponse:
        pass

    @abstractmethod
    async def get_job_status(self, job_id: str) -> JobStatusResponse:
        pass

    @abstractmethod
    async def cancel_job(self, job_id: str) -> None:
        pass

    @abstractmethod
    async def retrieve_result(self, job_id: str) -> AssetResult:
        pass
