import os
import uuid
from typing import Optional
from .base import AssetResult

class AssetManager:
    def __init__(self, storage_type: str = "local", storage_path: str = "./storage"):
        self.storage_type = storage_type
        self.storage_path = storage_path
        if self.storage_type == "local":
            os.makedirs(self.storage_path, exist_ok=True)

    async def save_asset(self, content: bytes, filename: str) -> str:
        if self.storage_type == "local":
            full_path = os.path.join(self.storage_path, filename)
            with open(full_path, "wb") as f:
                f.write(content)
            return f"/assets/{filename}"

        # S3 implementation would go here
        return f"https://s3.bucket/{filename}"

    async def delete_asset(self, asset_id: str):
        if self.storage_type == "local":
            path = os.path.join(self.storage_path, asset_id)
            if os.path.exists(path):
                os.remove(path)
