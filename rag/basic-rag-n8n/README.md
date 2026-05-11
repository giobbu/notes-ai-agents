## Setup n8n and ollama in docker

setuo n8n and ollama services
```bash
docker-compose up -d
```

open terminal within ollama container
```bash
docker exec -it ollama bash
```

list models
```bash
ollama list
```
