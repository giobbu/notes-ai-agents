
## Setup Neo4j with Dcoker


```bash
docker run \              
  -p 7474:7474 -p 7687:7687 \
  -e NEO4J_AUTH=<username>/<password> \
  -e NEO4J_PLUGINS='["apoc"]' \
  neo4j:latest
```

connect to db:
```bash
http://localhost:7474/
```
