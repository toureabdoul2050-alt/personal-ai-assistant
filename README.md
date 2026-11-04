# personal-ai-assistant

A small assistant that runs entirely on my own computer with [Ollama](https://ollama.com). Nothing is sent to a cloud API.

It keeps a long-term memory in a local `memory.json` file. Anything you tell it with `remember:` is added to the system prompt of every future conversation.

## Setup

```bash
ollama pull llama3.2
pip install requests fastapi uvicorn
python assistant.py
```

In the chat:

- `remember: <something>` saves a fact
- `memory` shows what it has saved
- `quit` exits

## Using it from a phone

```bash
python assistant.py --serve
```

This starts a FastAPI server on port 8000. From any device on the same Wi-Fi, send a POST request to `http://<your-computer-ip>:8000/chat` with `{"text": "..."}`, or open `/docs` to try it in the browser.

## Configuration

- `ASSISTANT_MODEL` (default `llama3.2`)
- `OLLAMA_URL` (default `http://localhost:11434/api/chat`)
- `ASSISTANT_MEMORY` (default `memory.json`)

## Ideas for later

- Voice input and output
- Searching my own documents
- A simple mobile web page instead of the API docs

## License

MIT
