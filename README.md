<div align="center">

# 🔐 Personal AI Assistant

**Your own AI assistant. On your machine. Under your control.**

![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=flat-square&logo=python&logoColor=white)
![Ollama](https://img.shields.io/badge/Runs%20on-Ollama-000000?style=flat-square&logo=ollama&logoColor=white)
![FastAPI](https://img.shields.io/badge/API-FastAPI-009688?style=flat-square&logo=fastapi&logoColor=white)
![Privacy](https://img.shields.io/badge/Privacy-100%25%20local-success?style=flat-square)
![License](https://img.shields.io/badge/License-MIT-green?style=flat-square)

</div>

---

## ✨ Why

Most AI assistants send every word you type to a big-tech cloud.
This one runs **entirely on your own computer** using open-source models, and keeps a **long-term memory** of what you tell it — stored locally, in a file you own.

## 🧩 Features

- 🧠 **Long-term memory** — tell it `remember: ...` and it never forgets
- 💬 **Terminal chat** — fast, simple, offline
- 📱 **Phone access** — start the API server and chat from any device on your Wi-Fi
- 🔁 **Any local model** — Llama, Mistral, Qwen, Gemma… anything Ollama can run
- 🔐 **Zero cloud** — nothing leaves your machine

## 🚀 Quick start

```bash
# 1. Install Ollama (https://ollama.com) and pull a model
ollama pull llama3.2

# 2. Get the assistant
git clone https://github.com/toureabdoul2050-alt/personal-ai-assistant.git
cd personal-ai-assistant
pip install requests fastapi uvicorn

# 3. Chat in the terminal
python assistant.py

# 4. Or serve it to your phone
python assistant.py --serve   # then open http://<your-computer-ip>:8000/docs
```

## 🗺 Roadmap

- [x] Local chat with memory
- [x] HTTP API for phone access
- [ ] Voice input / output
- [ ] Local documents search (RAG)
- [ ] Simple mobile web interface

---

<div align="center">Built by <a href="https://github.com/toureabdoul2050-alt">Ladji Touré</a> · MIT License</div>
