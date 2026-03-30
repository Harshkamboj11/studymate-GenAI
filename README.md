        # StudyMate AI

StudyMate AI is a lightweight multi-agent learning assistant built with Python and Streamlit, powered by Google Gemini.

It routes user prompts to specialized agents for:

- Summarization
- Simple ELI5-style explanations
- Quiz/question generation

## Features

- Multi-agent routing based on user intent keywords
- Streamlit web UI for interactive usage
- Gemini-backed text generation via `google-genai`
- Simple modular structure (`agents/` + `services/`)
- Docker support for containerized deployment

## Project Structure

```text
studymate-GenAI/
  app.py                  # Streamlit app entrypoint
  main.py                 # CLI entrypoint (currently references route_task)
  requirements.txt
  Dockerfile
  config.toml             # Streamlit config
  agents/
    __init__.py
    main_agent.py         # Central request router
    summarizer_agent.py   # Summary specialist
    eli5_agent.py         # Explain-like-I'm-5 specialist
    question_agent.py     # Quiz/question specialist
  services/
    __init__.py
    gemini_service.py     # Gemini API integration
    config.toml           # Streamlit config duplicate
```

## How It Works

### 1) Request Routing

`agents/main_agent.py` inspects user input and routes by keyword:

- Contains `summarize` -> `Summarizer Agent`
- Contains `question` or `quiz` -> `Question Generator Agent`
- Contains `explain` -> `Explain Agent (ELI5)`
- No recognized keyword -> defaults to `Explain Agent (ELI5)`

The router returns a dictionary:

```python
{
  "agent": "Agent Name",
  "response": "Generated text"
}
```

### 2) Specialized Agents

Each agent builds a role-specific prompt and calls a shared Gemini service:

- `summarizer_agent.handle(text)`
- `eli5_agent.handle(text)`
- `question_agent.handle(text)`

### 3) LLM Service Layer

`services/gemini_service.py` initializes a Gemini client using `GEMINI_API_KEY` and calls:

- Model: `gemini-2.5-flash`
- Method: `client.models.generate_content(...)`

## Setup

## Prerequisites

- Python 3.10+ (3.11 recommended)
- A Google Gemini API key

## 1. Clone and enter project

```bash
git clone <your-repo-url>
cd studymate-GenAI
```

If your local folder contains a nested `studymate-GenAI` directory, run commands from the directory that contains `app.py`.

## 2. Create and activate a virtual environment

### Windows (PowerShell)

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

### macOS/Linux

```bash
python -m venv .venv
source .venv/bin/activate
```

## 3. Install dependencies

```bash
pip install -r requirements.txt
```

## 4. Configure environment variables

Create a `.env` file in the same folder as `app.py`:

```env
GEMINI_API_KEY=your_actual_api_key_here
```

## Run the App (Streamlit)

```bash
streamlit run app.py
```

Then open the URL shown in your terminal (typically `http://localhost:8501`).

## Docker Run

Build image:

```bash
docker build -t studymate-ai .
```

Run container:

```bash
docker run --rm -p 8080:8080 --env GEMINI_API_KEY=your_actual_api_key_here studymate-ai
```

App will be available at `http://localhost:8080`.

## Usage Examples

Type prompts like:

- `Summarize the history of Rome`
- `Explain quantum computing`
- `Give me a quiz on Python lists`

Routing behavior is keyword-based, so include words like `summarize`, `explain`, `question`, or `quiz` for predictable results.

## Configuration Notes

The repository includes Streamlit config in both:

- `config.toml`
- `services/config.toml`

Both currently define:

- `enableCORS = false`
- `enableXsrfProtection = false`
- `headless = true`

For production deployments, you should review security-related settings (`CORS` and `XSRF`) before exposing publicly.

## Known Issue

`main.py` imports `route_task` from `agents/main_agent.py`, but the router function currently defined is `process_request`. This means CLI mode may fail unless updated.

Web mode (`app.py`) correctly uses `process_request` and works as intended.

## Troubleshooting

- Missing API key error in UI:
  - Ensure `.env` exists and contains `GEMINI_API_KEY`.
- Empty/failed responses:
  - Check API key validity and quota.
  - Verify internet connectivity.
- Import errors:
  - Confirm dependencies installed from `requirements.txt`.

## Tech Stack

- Python
- Streamlit
- Google Gemini (`google-genai`)
- python-dotenv

## Future Improvements

- Replace keyword routing with intent classification
- Add unit tests for agent routing and service layer
- Add chat history and session memory
- Add confidence/fallback handling for unsupported requests
- Fix CLI entrypoint (`main.py`) naming mismatch

