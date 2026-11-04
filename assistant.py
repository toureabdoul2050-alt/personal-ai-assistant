"""Personal AI Assistant — 100% local chat with long-term memory (Ollama).

Usage:
    python assistant.py            # chat in the terminal
    python assistant.py --serve    # HTTP API for your phone (port 8000)

Commands in chat:
    remember: <fact>   save a fact to long-term memory
    memory             show what the assistant remembers
    quit               exit
"""
import json
import os
import sys
from pathlib import Path

import requests

OLLAMA_URL = os.getenv("OLLAMA_URL", "http://localhost:11434/api/chat")
MODEL = os.getenv("ASSISTANT_MODEL", "llama3.2")
MEMORY_FILE = Path(os.getenv("ASSISTANT_MEMORY", "memory.json"))
HISTORY_LIMIT = 20


def load_memory() -> list:
    if MEMORY_FILE.exists():
        return json.loads(MEMORY_FILE.read_text(encoding="utf-8"))
    return []


def remember(fact: str) -> None:
    memory = load_memory()
    memory.append(fact.strip())
    MEMORY_FILE.write_text(json.dumps(memory, indent=2, ensure_ascii=False), encoding="utf-8")


def system_prompt() -> str:
    facts = "\n".join(f"- {f}" for f in load_memory()) or "- (nothing yet)"
    return (
        "You are a helpful, private personal assistant running locally. "
        "Be clear and concise. Things the user asked you to remember:\n" + facts
    )


def chat(history: list, message: str) -> str:
    history.append({"role": "user", "content": message})
    messages = [{"role": "system", "content": system_prompt()}] + history[-HISTORY_LIMIT:]
    response = requests.post(
        OLLAMA_URL, json={"model": MODEL, "messages": messages, "stream": False}, timeout=300
    )
    response.raise_for_status()
    reply = response.json()["message"]["content"].strip()
    history.append({"role": "assistant", "content": reply})
    return reply


def handle(history: list, message: str) -> str:
    text = message.strip()
    if text.lower().startswith("remember:"):
        remember(text.split(":", 1)[1])
        return "Saved to memory."
    if text.lower() == "memory":
        return "\n".join(f"- {f}" for f in load_memory()) or "Memory is empty."
    return chat(history, text)


def terminal() -> None:
    history: list = []
    print(f"Personal AI Assistant ({MODEL}) — type 'quit' to exit.")
    while True:
        try:
            message = input("\nyou > ")
        except (EOFError, KeyboardInterrupt):
            break
        if message.strip().lower() in {"quit", "exit"}:
            break
        if message.strip():
            print(f"\nai  > {handle(history, message)}")


def serve() -> None:
    from fastapi import FastAPI
    from pydantic import BaseModel
    import uvicorn

    app = FastAPI(title="Personal AI Assistant")
    history: list = []

    class Message(BaseModel):
        text: str

    @app.post("/chat")
    def chat_endpoint(msg: Message) -> dict:
        return {"reply": handle(history, msg.text)}

    uvicorn.run(app, host="0.0.0.0", port=8000)


if __name__ == "__main__":
    serve() if "--serve" in sys.argv else terminal()
