# ambient-assistant

## Getting Started with Dev Containers

Development for this project runs entirely inside a Docker container. No local Python installation is required.

### Prerequisites

- [Docker Desktop](https://www.docker.com/products/docker-desktop)
- [VS Code](https://code.visualstudio.com/)
- [Dev Containers extension](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers) for VS Code

### Starting the Development Environment

1. Open the project folder in VS Code.
2. Open the Command Palette (`Ctrl+Shift+P` / `Cmd+Shift+P`) and run **Dev Containers: Reopen in Container**.
3. VS Code will build the Docker image and start the development environment. All required extensions will be installed automatically.

Once the container is running, a fully configured Python 3.11 environment is available with all project dependencies installed.

## Setup

1. Install dependencies:

   ```bash
   make install
   ```

2. Copy the example env file and add your OpenAI API key:

   ```bash
   cp .env.example .env
   ```

   Open `.env` and set `OPENAI_API_KEY` to your key.

3. Start the server:

   ```bash
   make run
   ```

The API will be available at `http://localhost:8000`.

### Example request

```bash
curl -X POST http://localhost:8000/assistant/message \
     -H "Content-Type: application/json" \
     -d '{"content": "Hello, who are you?"}'
```

## Development commands

| Command       | Description                  |
|---------------|------------------------------|
| `make run`    | Start the development server |
| `make install`| Install Python dependencies  |
| `make test`   | Run the test suite           |
| `make lint`   | Run ruff linter              |
| `make format` | Run black formatter          |
