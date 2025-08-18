# 🍕 Pizza Review Q&A Bot

An interactive chatbot that answers user questions about a pizza restaurant by combining:
- **LangChain**
- **Ollama** (LLMs + embeddings)
- **Chroma** (vector database)

The system retrieves the most relevant reviews from a dataset (`Restaurants_Reviews.csv`) and provides context-aware answers.

---

## 🚀 Features
- Stores customer reviews in a **Chroma vector database**
- Uses `mxbai-embed-large` embeddings for semantic similarity
- Answers questions with **llama3.2** model via Ollama
- Interactive Q&A loop in the terminal
- Context-driven answers tailored to restaurant reviews

---

## 📦 Installation

1. Clone this repo:
   ```bash
   git clone https://github.com/yourusername/pizza-qa-bot.git
   cd pizza-qa-bot
2.Install Python dependencies:
pip install -r requirements.txt
langchain>=0.2.0
langchain-ollama>=0.1.0
langchain-chroma>=0.1.0
chromadb>=0.4.22
pandas>=2.0.0

3.Install Ollama and pull required models:
 ollama pull llama3.2
 ollama pull mxbai-embed-large


📂 Project Structure

.
├── main.py                   # Chatbot loop (Q&A)
├── vector.py                 # Vector DB setup & retriever
├── Restaurants_Reviews.csv   # Review dataset (must include Title, Review, Rating, Date)
├── requirements.txt
└── README.md
