# AI Model Configuration

Striker2.1 uses a provider-independent system. You can enable different "engines" by configuring the `.env` file.

## Available Providers

### 1. Demo Provider (Default)
- **Usage**: No API key required.
- **Behavior**: Simulates generation with placeholders.
- **Purpose**: UI testing and development.

### 2. Stability AI
- **Requirement**: `STABILITY_API_KEY` in `.env`.
- **Capabilities**: High-fidelity Image and Video generation.
- **Setup**: Add your key to `.env` and restart the backend.

### 3. Local Open-Weight Models (Coming Soon)
We are integrating adapters for:
- **Stable Diffusion XL**: For local image generation.
- **Stable Video Diffusion (SVD)**: For local image-to-video.
- **AnimateDiff**: For motion transfer.

### Hardware Requirements for Local Models
Running AI models locally requires substantial hardware:
- **GPU**: NVIDIA GPU with at least 12GB VRAM (16GB+ recommended).
- **RAM**: 32GB+ System Memory.
- **Disk**: 50GB+ for model weights.
- **OS**: Linux (Ubuntu recommended) or Windows with WSL2.
