
# Single vs Multi-Agent Article Writer

Welcome to the **Single vs Multi-Agent Article Writer** project! This investigation aims to compare the effectiveness of single-agent versus multi-agent approaches for building an Article Writer app. Below, you'll find details about the implementation of each approach, as well as instructions for setting up the environment.

## Table of Contents

- [Overview](#overview)
- [Setup Instructions](#setup-instructions)
- [Single-Agent Approach](#single-agent-approach)
- [Multi-Agent Approach](#multi-agent-approach)
- [Environment Variables](#environment-variables)
- [License](#license)

## Overview

This project includes two notebooks that demonstrate different approaches for building an Article Writer app:

1. **Single-Agent Approach**: Implemented using LangChain.
2. **Multi-Agent Approach**: Implemented using CrewAI.

The goal is to explore the capabilities, strengths, and limitations of each approach, and to determine whether a multi-agent system provides significant advantages over a single-agent setup.

## Setup Instructions

To set up the environment for running these notebooks, use the provided setup scripts:

- **Windows**: Run `start.cmd` to set up the environment on Windows.
- **Linux/Mac**: Run `start.sh` to set up the environment on Linux or Mac.

Each script will install the necessary dependencies and configure the environment appropriately.

## Single-Agent Approach

### Notebook: Article_Writer_via_Single_Agent_with_LangChain.ipynb

This notebook presents an implementation of an **Article Writer app using an agentic approach** composed of an agent with two LLM-based tools:

- **Research Tool**: A tool that queries the DuckDuckGo search API and is useful for answering questions about current events.
- **Writing Tool**: A tool that writes text by leveraging an LLM and is useful for generating engaging text based on a set of insights.

The code is developed using the LangChain library, the OpenAI LLM API, and the DuckDuckGo search API.

By the end of the notebook, it is discussed why a multi-agent system might be preferable for this task.

[Link to Notebook](./Article_Writer_via_Single_Agent_with_LangChain.ipynb)

## Multi-Agent Approach

### Notebook: Article_Writer_via_Multi_Agent_with_CrewAI.ipynb

This notebook presents an implementation of an **Article Writer app using a multi-agent approach** with two agent executors:

- **Researcher**: An agent that queries the DuckDuckGo search API to answer questions about current events.
- **Writer**: An agent that writes text by leveraging an LLM to generate engaging content based on research insights.

The code is developed using the [CrewAI](https://github.com/crewAIInc/crewAI) library, which is a cutting-edge framework for orchestrating role-playing, autonomous AI agents. By fostering collaborative intelligence, CrewAI empowers agents to work together seamlessly, tackling complex tasks.

By the end of the notebook, a discussion is included on the hierarchical structure nomenclature between CrewAI and [LangGraph](https://www.langchain.com/langgraph), a framework for building stateful, multi-actor agents capable of handling complex scenarios and collaborating with humans.

[Link to Notebook](./Article_Writer_via_Multi_Agent_with_CrewAI.ipynb)

## Environment Variables

The project requires an environment variable for the OpenAI API key. Create a `.env` file in the root directory and include the following:

```
OPENAI_API_KEY=<your_openai_api_key_here>
```

## License

This project is open-sourced under the [MIT License](../LICENSE).
