# Deployment Guide

Striker2.1 is designed for easy deployment via Docker.

## Local Setup

1. **Clone and Configure**:
   ```bash
   git clone https://github.com/your-username/striker2.1.git
   cd striker2.1
   cp .env.example .env
   ```
2. **Launch**:
   ```bash
   docker-compose up -d --build
   ```
3. **Verify**:
   - Visit `http://localhost:3000` for the Studio.
   - Visit `http://localhost:8000/docs` for the API documentation.

## Production Deployment

For production, we recommend:
- **Cloud Infrastructure**: AWS, GCP, or Azure.
- **GPU Hosting**: Use a provider like Lambda Labs, RunPod, or Vast.ai for local model inference.
- **CI/CD**: GitHub Actions for automated testing and deployment to a Kubernetes cluster.
- **S3 Storage**: Configure the `STORAGE_TYPE=s3` in `.env` to handle large asset volumes.

## Troubleshooting

- **DB Connection**: If the app fails to start, ensure the `db` container is healthy.
- **API Keys**: Ensure the `.env` file contains valid keys for the providers you wish to use.
- **CORS Issues**: The backend is configured to allow all origins by default; restrict this in production.
