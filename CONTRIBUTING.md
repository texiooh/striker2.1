# Contributing to Striker2.1

We welcome contributions to make Striker2.1 the premier open-source AI creative studio.

## How to Contribute

1. **Fork the Repository**: Create your own copy of the project.
2. **Create a Feature Branch**: Use descriptive names (e.g., `feature/motion-transfer-ui`).
3. **Implement & Verify**:
   - Follow the architectural boundaries defined in `docs/architecture.md`.
   - Ensure all changes are verified with tests or concrete evidence.
4. **Submit a Pull Request**: Provide a clear description of the change and evidence of its functionality.

## Development Standards

- **Type Safety**: Use TypeScript for frontend and Pydantic for backend.
- **Modular Providers**: New AI models must be implemented as `AIProvider` adapters.
- **Performance**: Optimize for token usage and inference latency.
- **Clean Code**: Follow PEP 8 for Python and standard React patterns for frontend.

## Contribution Scope

We prioritize:
- New AI provider adapters.
- UI/UX improvements for the creative workspace.
- Optimization of the generation pipeline.
- Security hardening and automated testing.
