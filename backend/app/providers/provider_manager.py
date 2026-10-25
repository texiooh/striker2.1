from typing import Dict
from .base import AIProvider
from .demo import DemoProvider
from .stability import StabilityAIProvider
import os

class ProviderManager:
    def __init__(self):
        self._providers: Dict[str, AIProvider] = {}
        self._load_providers()

    def _load_providers(self):
        # Always load the demo provider
        self.register_provider(DemoProvider())

        # Load real providers if keys are available
        stability_key = os.getenv("STABILITY_API_KEY")
        if stability_key:
            self.register_provider(StabilityAIProvider(stability_key))

    def register_provider(self, provider: AIProvider):
        self._providers[provider.id] = provider

    def get_provider(self, provider_id: str) -> AIProvider:
        provider = self._providers.get(provider_id)
        if not provider:
            raise ValueError(f"Provider {provider_id} not found. Available: {list(self._providers.keys())}")
        return provider

    def list_providers(self):
        return [
            {"id": p.id, "name": p.name, "capabilities": p.capabilities.dict()}
            for p in self._providers.values()
        ]

# Singleton instance
provider_manager = ProviderManager()
