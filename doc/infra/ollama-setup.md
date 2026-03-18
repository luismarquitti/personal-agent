# Local LLM Setup Guide (Ollama)

This guide explains how to set up **Ollama** to run Large Language Models locally for the **Personal AI Core** project.

## 1. Install Ollama

### Windows
1. Download the installer from [ollama.com/download](https://ollama.com/download/windows).
2. Run the `.exe` and follow the instructions.
3. Once installed, Ollama will run in your system tray.

### macOS
1. Download the zip from [ollama.com/download](https://ollama.com/download/mac).
2. Extract and move the Ollama application to your `Applications` folder.
3. Launch Ollama.

### Linux
Run the following command in your terminal:
```bash
curl -fsSL https://ollama.com/install.sh | sh
```

## 2. Download Recommended Models

The **Personal AI Core** is optimized for specific models. Pull them using the following commands:

```bash
# General purpose high performance
ollama pull llama3

# Fast, lightweight model
ollama pull phi3

# Specific model for code (if needed)
ollama pull codellama
```

## 3. Environment Configuration

Ensure your project is configured to use the local Ollama provider when needed. In your `.env` file:

```env
OLLAMA_BASE_URL=http://localhost:11434
PREFERRED_LOCAL_MODEL=llama3
```

## 4. Verify Local Instance

Check if the Ollama API is responding:

```bash
curl http://localhost:11434/api/tags
```

Or run the project's test script:

```bash
python scripts/tests/test_ollama_local.py
```
