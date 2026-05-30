# OpenRag

A lightweight, open-source Retrieval-Augmented Generation (RAG) framework that combines **local [all-MiniLM-L6-v2](https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2) embeddings** with **Google Gemini** for answer generation — served through a clean Flask API and Jinja2-powered UI.

No cloud embedding costs. No vendor lock-in for vector search. Just your documents, locally indexed, intelligently queried.

---

## ✨ Features

- 📄 **Multi-format ingestion** — supports `.txt` and `.pdf` source documents
- 🧠 **Local embeddings** — uses local model (all-MiniLM-L6-v2), runs entirely on your machine
- 💾 **Persistent vector store** — embeddings saved to disk, no re-processing needed
- 🤖 **Gemini-powered answers** — leverages Google Gemini for high-quality response generation
- 🖥️ **Jinja2 UI and Flask Backend** — browser-based interface included out of the box


---

## 🚀 Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/ARYV-AI/OpenRAG.git
cd OpenRAG
```

### 2. Install dependencies

```bash
pip install -r requirements-train.txt
```

### 3. Add your source documents

Place your `corpus.txt` or `corpus.pdf` files into the `src/corpus/` directory.

### 4. Generate embeddings

Run `embed.py` from the `src/` directory, passing either `pdf` or `text` as a command-line argument depending on your document type.

**For PDF files:**
```bash
cd src
python3 embed.py pdf
```

**For plain text files:**
```bash
cd src
python3 embed.py txt
```

Once complete, the `src/db/` directory will be populated with vector data.

> ⚠️ Re-run `embed.py` whenever you add new documents to the corpus.

### 5. Set your Gemini API key

Export your Google Gemini API key as an environment variable:

```bash
# Linux / macOS
export GEMINI_API_KEY="your_gemini_api_key_here"

# Windows (Command Prompt)
set GEMINI_API_KEY=your_gemini_api_key_here

# Windows (PowerShell)
$env:GEMINI_API_KEY="your_gemini_api_key_here"
```

> Get your API key at [Google AI Studio](https://aistudio.google.com/app/apikey).

### 6. Start the Flask application

```bash
python3 app.py
```

Then open your browser at `http://localhost:5000` to use the UI, or query the API directly.

---

### 7. Deploying the application in cloud

Use the requirements.txt as it does not contain dependancy required for retraining as the trained data will already be present in Persistent ChromaDB Storage
```bash
pip install -r requirements-train.txt
gunicorn app:app
```

---

## ⚙️ Configuration

| Environment Variable | Description | Required |
|---|---|---|
| `GEMINI_API_KEY` | Your Google Gemini API key | ✅ Yes |

---

## 🤝 Contributing

Contributions are welcome and appreciated! Feel free to open high quality PRs with bugfixes and feature suggestions.

### Reporting Issues

Found a bug or have a feature request? [Open an issue](https://github.com/ARYV-AI/OpenRAG/issues) and include:
- A clear description of the problem or suggestion
- Steps to reproduce (for bugs)
- Your environment details (OS, Python version)

### Roadmap
 - Edgecase and Error handling
 - Support for other LLMs

---

## For enterprise
If you are looking to build a RAG or other AI feature/workflow for your enterprise, check us out [here](https://aryvlabs.com). Our team of professional consultants can help you build your next big AI thing. 
