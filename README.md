# Striker2.1: Open-Source AI Creative Studio

Striker2.1 is a production-oriented, professional AI creative studio for high-fidelity image and video generation. Built with a provider-independent architecture, it allows users to harness the power of both local open-weight models and commercial AI APIs within a cinematic, minimal workspace.

## 🚀 Features

- **AI Image Generation**: Text-to-image and image-to-image workflows.
- **AI Video Generation**: Text-to-video and image-to-video animation.
- **Motion Transfer Engine**: Transfer performance from a source video to a reference subject.
- **Cinematic Workspace**: A professional dark interface designed for creative flow.
- **Provider-Agnostic**: Seamlessly switch between local inference and cloud APIs.
- **Project Management**: Organize your generations into projects and asset libraries.

## 🛠 Tech Stack

- **Frontend**: Next.js 14, React, TypeScript, Tailwind CSS.
- **Backend**: Python 3.11+, FastAPI.
- **Database**: PostgreSQL (Project/Asset persistence), Redis (Job Queue).
- **Infrastructure**: Docker Compose for one-click local deployment.

## 🏁 Quick Start

### Prerequisites
- Docker and Docker Compose installed.

### Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/striker2.1.git
   cd striker2.1
   ```
2. Setup environment variables:
   ```bash
   cp .env.example .env
   # Edit .env with your API keys
   ```
3. Launch the studio:
   ```bash
   docker-compose up -d --build
   ```
4. Access the app:
   - Frontend: `http://localhost:3000`
   - Backend API: `http://localhost:8000`

## 📜 License
Distributed under the MIT License. See `LICENSE` for more information.
