## Summary of our project -

Think of the repository as a movie production pipeline: data comes in → gets cleaned → becomes knowledge → gets stored → retrieved → an LLM generates an answer → we evaluate whether the answer was actually good.


# To activate the Virtual Environment - 

uv venv

source .venv/bin/activate

## Below is the structure of our project -

                     ┌─────────────────┐
                     │ Bollywood Data  │
                     │ IMDb / Wiki /   │
                     │ TMDB / datasets │
                     └────────┬────────┘
                              │
                              ▼
                    ┌──────────────────┐
                    │    Ingestion     │
                    │                  │
                    │ loaders          │
                    │ cleaning         │
                    │ chunking         │
                    │ pipeline         │
                    └────────┬─────────┘
                             │
              ┌──────────────┴──────────────┐
              ▼                             ▼
      ┌───────────────┐             ┌────────────────┐
      │ Vector Index  │             │ Knowledge Graph│
      │               │             │                │
      │ ChromaDB      │             │ Neo4j          │
      │ embeddings    │             │ entities       │
      └───────┬───────┘             │ relationships  │
              │                     └───────┬────────┘
              │                             │
              └─────────────┬───────────────┘
                            ▼
                   ┌─────────────────┐
                   │ Hybrid Retriever │
                   │                 │
                   │ Vector search   │
                   │ Graph search    │
                   │ Entity search   │
                   └────────┬────────┘
                            │
                            ▼
                     ┌─────────────┐
                     │    LLM      │
                     │             │
                     │ context +   │
                     │ prompt      │
                     └──────┬──────┘
                            │
                            ▼
                    ┌───────────────┐
                    │ Answer +      │
                    │ Sources       │
                    └───────────────┘