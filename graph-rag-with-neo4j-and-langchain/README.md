# Graph RAG with Neo4j and LangChain

Welcome to the **Graph RAG with Neo4j and LangChain** project! This investigation explores the implementation of Graph-based Retrieval Augmented Generation (GraphRAG) using Neo4j graph database and LangChain framework.

<p align="center">
  <img src="./img/notebook_4_full_graph_sample_with_labels.png" alt="" width="600">
</p>

<center>Knowledge graph visualization showing entities and relationships extracted from documents.</center>
<center>Image source: Author.</center>

Below, you'll find details about the implementation of different GraphRAG approaches, including indexing and inference pipelines for both lexical and semantic search strategies.

## Table of Contents

- [Overview](#overview)
- [Setup Instructions](#setup-instructions)
- [Notebooks](#notebooks)
  - [1. GraphRAG Indexing Pipeline for Lexical Search](#notebook-1)
  - [2. GraphRAG Inference Pipeline for Lexical Search](#notebook-2)
  - [3. GraphRAG Inference Pipeline for Semantic Search](#notebook-3)
  - [4. GraphRAG Indexing and Inference Pipelines for Semantic Search](#notebook-4)
- [Environment Variables](#environment-variables)
- [Key Features](#key-features)
- [Data Sources](#data-sources)
- [License](#license)

## Overview

This project includes four Jupyter notebooks that demonstrate different aspects of building and querying knowledge graphs for RAG applications:

1. **Indexing Pipeline for Lexical Search**: Building knowledge graphs from PDF documents using Cypher queries
2. **Inference Pipeline for Lexical Search**: Querying the knowledge graph using lexical/keyword-based search
3. **Inference Pipeline for Semantic Search**: Implementing vector-based semantic search over the graph
4. **Indexing and Inference for Semantic Search**: Complete end-to-end implementation with embeddings

The goal is to explore different approaches to knowledge graph construction and retrieval, comparing lexical search with semantic search strategies, and understanding the trade-offs between automatic, semi-automatic, and manual graph construction methods.

## Setup Instructions

### Prerequisites

You will need to have a running Neo4j instance. You have several options:

1. **Neo4j Aura (Cloud)**: Create a [free Neo4j database instance in their Aura cloud service](https://neo4j.com/cloud/platform/aura-graph-database/)
2. **Neo4j Desktop**: Download and install [Neo4j Desktop application](https://neo4j.com/download/)
3. **Docker**: Run Neo4j as a Docker container

### Installation

Install the required Python packages:

```bash
pip install langchain==0.2.14 \
            langchain-openai==0.1.20 \
            langchain-community==0.2.12 \
            langchain-experimental==0.0.64 \
            neo4j-graphrag==1.2.0 \
            pymupdf==1.24.13 \
            pypdf==5.1.0 \
            python-dotenv==1.0.1
```

## Notebooks

### Notebook 1: GraphRAG Indexing Pipeline for Lexical Search

**File**: `1_GraphRAG_Indexing_Pipeline_for_Lexical_Search.ipynb`

This notebook demonstrates how to build a knowledge graph from PDF documents for lexical (keyword-based) search using Neo4j and LangChain.

**Key Topics**:
- Loading and splitting PDF documents into chunks
- Automatic knowledge graph construction using `LLMGraphTransformer`
- Semi-automatic graph construction with fixed nodes and relationships
- Building lexical graphs with automatic entity resolution
- Exploring different chunking strategies

**Approaches Covered**:
1. **Automatic**: Let the LLM determine entities and relationships
2. **Semi-Automatic (Fixed Schema)**: Define allowed nodes and relationships
3. **Semi-Automatic (Lexical Graph)**: Use Neo4j's native functions with predefined schema
4. **Semi-Manual**: Manual lexical graph with automatic domain graph

**Tech Stack**: Neo4j, LangChain, OpenAI GPT-4

[Link to Notebook](./1_GraphRAG_Indexing_Pipeline_for_Lexical_Search.ipynb)

### Notebook 2: GraphRAG Inference Pipeline for Lexical Search

**File**: `2_GraphRAG_Inference_Pipeline_for_Lexical_Search.ipynb`

This notebook demonstrates how to query the knowledge graph using lexical search strategies with Cypher query language.

**Key Topics**:
- Querying knowledge graphs using Cypher
- Building Q&A chains with `GraphCypherQAChain`
- Lexical graph traversal patterns
- Retrieving structured information from the graph

**Tech Stack**: Neo4j, LangChain, Cypher Query Language

[Link to Notebook](./2_GraphRAG_Inference_Pipeline_for_Lexical_Search.ipynb)

### Notebook 3: GraphRAG Inference Pipeline for Semantic Search

**File**: `3_GraphRAG_Inference_Pipeline_for_Semantic_Search.ipynb`

This notebook demonstrates how to implement semantic (vector-based) search over the knowledge graph.

**Key Topics**:
- Vector embeddings for semantic search
- Combining graph structure with vector similarity
- Semantic retrieval strategies
- Comparing lexical vs semantic search results

**Tech Stack**: Neo4j, LangChain, OpenAI Embeddings

[Link to Notebook](./3_GraphRAG_Inference_Pipeline_for_Semantic_Search.ipynb)

### Notebook 4: GraphRAG Indexing and Inference Pipelines for Semantic Search

**File**: `4_GraphRAG_Indexing_and_Inference_Pipelines_for_Semantic_Search.ipynb`

This notebook presents a complete end-to-end implementation of GraphRAG with semantic search capabilities, including both indexing and inference pipelines.

**Key Topics**:
- Building knowledge graphs with embeddings
- Entity resolution and relationship extraction
- Semantic search implementation
- Complete RAG pipeline with graph context

**Tech Stack**: Neo4j, LangChain, OpenAI GPT-4, OpenAI Embeddings

[Link to Notebook](./4_GraphRAG_Indexing_and_Inference_Pipelines_for_Semantic_Search.ipynb)

## Environment Variables

The project requires the following environment variables. Create a `.env` file in the notebook directory and include:

```
OPENAI_API_KEY=<your_openai_api_key_here>
NEO4J_URI=<your_neo4j_connection_uri>
NEO4J_USERNAME=<your_neo4j_username>
NEO4J_PASSWORD=<your_neo4j_password>
```

**Example for Neo4j Aura**:
```
NEO4J_URI=neo4j+s://xxxxxxxx.databases.neo4j.io
NEO4J_USERNAME=neo4j
NEO4J_PASSWORD=your_password_here
```

## Key Features

- **Multiple Construction Methods**: Explore automatic, semi-automatic, and manual approaches to building knowledge graphs
- **Lexical and Semantic Search**: Compare keyword-based and vector-based retrieval strategies
- **Entity Resolution**: Automatic merging of duplicate entities using LLMs
- **Relationship Extraction**: LLM-powered extraction of entities and their relationships from unstructured text
- **Schema Flexibility**: Work with fixed schemas or allow dynamic entity/relationship discovery
- **Embedding Generation**: Integrate vector embeddings for semantic similarity search
- **Graph Visualization**: Tools and queries for exploring the constructed knowledge graphs

## Data Sources

The notebooks use PDF documents from the UN Sustainable Development Goals as sample data:
- Goal 1: No Poverty
- Goal 2: Zero Hunger
- Goal 3: Good Health and Well-being
- Goal 4: Quality Education

These documents are automatically downloaded from the UN website and stored in the `data/` directory.

## References

1. [LangChain | How to construct knowledge graphs](https://python.langchain.com/v0.2/docs/how_to/graph_constructing/)
2. [Github | Neo4j GraphRAG Package for Python](https://github.com/neo4j/neo4j-graphrag-python)
3. [DeepLearning.AI | Knowledge Graphs for RAG](https://learn.deeplearning.ai/courses/knowledge-graphs-rag/lesson/5/constructing-a-knowledge-graph-from-text-documents)
4. [GraphRAG | Lexical Graph](https://graphr.ag/reference/knowledge-graph/lexical-graph/)

## License

This project is open-sourced under the [MIT License](../LICENSE).
