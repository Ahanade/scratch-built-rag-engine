# Scratch-Built RAG Engine 

An optimized, framework-free **Retrieval-Augmented Generation (RAG)** search engine built from the ground up using pure Python logic. This system avoids heavy framework overhead (like LangChain or vector database packages) by implementing localized parsing, custom token-frequency query matching, and an interactive frontend wrapper.

##  Architecture Workflow
1. **Data Ingestion Pipeline**: Parses structured JSON intent configurations into combined searchable Q&A context blocks.
2. **Algorithmic Search Tier**: Tokenizes user queries, strips noise, and matches string densities dynamically across database rows.
3. **Context Processing Module**: Performs deterministic keyword extractions to deliver immediate zero-latency responses.

##  Tech Stack
* **Language:** Python 3
* **Interface UI:** Gradio 
* **Data Format:** JSON Structured Archetypes

## How to Run Locally
1. Clone the repository:
   ```bash
   git clone [https://github.com/YOUR_USERNAME/scratch-built-rag-engine.git](https://github.com/YOUR_USERNAME/scratch-built-rag-engine.git)
   cd scratch-built-rag-engine
