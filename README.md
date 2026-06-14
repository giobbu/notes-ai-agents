# notes-ai-agents
![Made with Love](https://img.shields.io/badge/Made%20with-❤️-red)

## Overview
This repository contains a series of notebooks that progressively build and evaluate LLM-powered chatbot, rag and agents systems. The focus is on experimentation with safeguards, observability, and evaluation frameworks.

In `/checklist` folder:
```bash
checklists
├── 0_tool_design.ipynb
├── 1_metrics_eval_agents.ipynb
├── 2_safety_measures.ipynb
└── 3_deployment.ipynb
```

In `/steps` folder:
```bash
steps
├── text
├── vision
│   └── imgs
└── voice
```

* `/text`
    ```bash
    text
    ├── 0_basic_agent.ipynb
    ├── 1_agent_confidence.ipynb
    ├── 2_ollama_websearch.ipynb
    ├── 3_small_chat_on_sustainability.ipynb
    ├── 4_ollama_safeguard.ipynb
    ├── 5_llm_mlflow_tracing.ipynb
    ├── 6_chabot_mlflow_tracing.ipynb
    ├── 7_chatbot_evaluation.ipynb
    ├── 8_compare_llm.ipynb
    ├── 9_streamlit_fastapi_mlflow.ipynb
    ├── 10_token_budget.ipynb
    ├── 11_semantic_cache.ipynb
    ├── 12_semantic_route.ipynb
    └── 13_prompt_builder.ipynb
    ```

* `/vision`
    ```bash
    vision
    ├── 0_vlm_call.ipynb
    └── imgs
        └── car.jpeg
    ```

In `/advanced` folder:
```bash
advanced
├── agent
└── rag
```

* `/agent`:
    ```bash
    agent
    ├── 0_react_agent.ipynb
    ├── 1_memory_agent.ipynb
    ├── 2_reflection_agent.ipynb
    ├── agent_trace_logs.jsonl
    └── utils
        ├── logger.py
        └── token_budget.py
    ```

* `/rag`:
    ```bash
    rag
    ├── 0_basic-rag-n8n
    │   ├── README.md
    │   ├── articles
    │   ├── docker-compose.yaml
    │   ├── img
    │   │   ├── rag-workflow.png
    │   │   └── text-classifier.png
    │   └── template
    │       ├── simple-RAG-workflow.json
    │       └── text-classifier-ingestion.json
    ├── 1_kg_rag
    │   ├── 0_knowledge_graph_rag.ipynb
    │   └── README.md
    └── imgs
    ```

## License
This project is under the MIT license.
