# 📄 DocMind

DocMind is an AI-Powered PDF information retrieval system that helps you quickly and efficiently extract insights from your documents using state-of-the-art language models and vector search. Whether you're a researcher, student, or professional, DocMind makes it easy to ask questions and get concise answers from your PDF files.

---

## ✨ Features

- ⚡ **Fast & Accurate**: Retrieve information from PDFs using advanced AI models.
- 🖥️ **User-Friendly Interface**: Simple, interactive web UI powered by Streamlit.
- 🤖 **Conversational AI**: Ask questions in natural language and get contextual answers.
- 📄 **Multi-PDF Support**: Upload and process multiple PDF files at once.
- 🔍 **Semantic Search**: Uses vector embeddings for intelligent document retrieval.

---

## ⚠️ Important Notes

- This app uses the latest LangChain integrations. Some imports (like `HuggingFaceEmbeddings`) are deprecated and will need updating for LangChain 1.0+. See the [LangChain migration guide] (https://python.langchain.com/docs/versions/migrating_memory/) for details.
- All required dependencies are listed in `requirements.txt`.
- The codebase is ready for LangChain 0.3.x, but some APIs will need updating for 1.0+.
- The app now handles missing API keys and prevents errors if you try to ask questions before uploading PDFs.

---

## 🛠️ Environment Variables

To run this project, you will need to set up the following environment variable:

| Variable Name         | Description                                 | Example Value                |
|----------------------|---------------------------------------------|------------------------------|
| `ANTHROPIC_API_KEY`  | Your Anthropic API key for Claude models    | `sk-ant-...`                 |

**How to set up:**

- **Locally:** Create a `.env` file in your project root:
  ```env
  ANTHROPIC_API_KEY=your_actual_api_key_here
  ```
- **Streamlit Cloud:** Go to your app dashboard → **Settings** → **Secrets** and add:
  ```env
  ANTHROPIC_API_KEY=your_actual_api_key_here
  ```

> **Never commit your API keys to version control. Always use environment variables or Streamlit secrets for sensitive information.**

---

## 🛠️ Tech Stack

**Backend:**
- Python 3.8+
- [Streamlit](https://streamlit.io/) – Web UI
- [LangChain](https://python.langchain.com/) – LLM orchestration
- [Anthropic Claude](https://www.anthropic.com/) – Conversational AI (via API)
- [HuggingFace Sentence Transformers](https://www.sbert.net/) – Embeddings
- [FAISS](https://github.com/facebookresearch/faiss) – Vector search
- [PyPDF2](https://pypdf2.readthedocs.io/) – PDF parsing
- [python-dotenv](https://pypi.org/project/python-dotenv/) – Environment variable management

**Project Management:**
- `requirements.txt` for dependencies
- `.env` for API keys and secrets

---

## 🗂️ Project Structure

```plaintext
DocMind/
├── app.py                     # Main Streamlit app
├── src/
│   ├── __init__.py
│   └── helper.py              # PDF processing, vector store, and AI logic
├── research/
│   └── trials.ipynb           # Experimental notebooks
├── template.py                # Project scaffolding script
├── requirements.txt           # Python dependencies
├── setup.py                   # Packaging config
├── LICENSE
└── README.md
```

---

## 💻 Prerequisites & System Requirements

- **Python**: 3.8 or higher
- **pip**: Python package manager
- **OS**: Windows, macOS, or Linux
- **Anthropic API Key**: Required for Claude LLM access

---

## 🚀 Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/DocMind.git
   cd DocMind
   ```

2. **Create a virtual environment (recommended)**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables**
   - Create a `.env` file in the project root with the following content:
     ```env
     ANTHROPIC_API_KEY=your_anthropic_api_key_here
     ```

---

## 🏃‍♂️ Usage

### 🧑‍💻 Development

To run the app in development mode:

```bash
streamlit run app.py
```

- Open the provided local URL in your browser.
- Upload one or more PDF files using the sidebar.
- Ask questions in the input box and get instant answers!

### 🚢 Production

For production deployment, you can use [Streamlit Community Cloud](https://streamlit.io/cloud) or deploy on your own server:

```bash
streamlit run app.py
```

- For advanced deployment (Docker, cloud, etc.), see [Streamlit Deployment Docs](https://docs.streamlit.io/streamlit-community-cloud/deploy-your-app).

---

## 🧪 Running Tests

> **Note:** The `test.py` file is currently a placeholder. Add your tests here as the project grows!

---

## 🤝 Contributing

Contributions are welcome! 🎉

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/YourFeature`)
3. Commit your changes (`git commit -am 'Add new feature'`)
4. Push to the branch (`git push origin feature/YourFeature`)
5. Open a Pull Request

Please open an issue for suggestions or bug reports.

---

## 📄 License

This project is licensed under the terms of the [LICENSE](LICENSE) file.

---

## 📬 Contact & Support

- **Author:** Varad Pensalwar
- **Email:** varadpensalwar@gmail.com
- **GitHub Issues:** [Open an issue](https://github.com/yourusername/DocMind/issues)

---

*Made with ❤️ for the AI and open-source community!*
