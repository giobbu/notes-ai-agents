## RAG worflow

### basic rag architecture

![Image Alt Text](img/rag-workflow.png)

### text classifier for document ingestion

![Image Alt Text](img/text-classifier.png)


## Setup n8n and ollama (with GPU) in docker

setup n8n
```bash
docker-compose up -d
```

start ollama on host
```bash
ollama serve
```

list chat/embedding models
```bash
ollama list
```

open `http://localhost:5678/home/workflows` drag rag template from `/template` into canvas and start chatting.

Make sure ollama has the right models in use.

