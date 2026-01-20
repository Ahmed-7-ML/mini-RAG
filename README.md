# mini-RAG Application

- Minimal Implementation of RAG Model for Question Answering (Q/A).

## Requirements

- Python 3.8+

### Install Python using MiniConda

1. Download and install MiniConda from [here](https://docs.anaconda.com/free/miniconda/#quick-command-line-install)
2. Create a new environment using the following command:

```shell
$ conda create -n mini-rag python=3.8
```

3. Activate the environment:

```shell
$ conda activate mini-rag
```

### (Optional) Setup you command line interface for better readability

```shell
export PS1="\[\033[01;32m\]\u@\h:\w\n\[\033[00m\]\$ "
```

## Installation

### Install the required packages

```shell
$ pip install -r requirements.txt
```

### Setup the environment variables

```shell
$ cp .env.example .env
```

Set your environment variables in the `.env` file. Like `OPENAI_API_KEY` value.

## Run the FastAPI server

```shell
$ uvicorn main:app --reload --host 127.0.0.1 --port 5000
```
