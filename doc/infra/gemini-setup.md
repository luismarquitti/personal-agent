# Gemini API Setup Guide

This guide explains how to obtain a Google Gemini API Key and configure it for the **Personal AI Core** project.

## 1. Obtain an API Key

There are two primary ways to get a Gemini API Key:

### A. Google AI Studio (Recommended for Individual Devs)
1. Go to [Google AI Studio](https://aistudio.google.com/).
2. Sign in with your Google account.
3. Click on **"Get API key"** in the left sidebar.
4. Click **"Create API key"**. You can choose to create it in a new project or an existing one.
5. Copy the generated API key.

### B. Google Cloud Vertex AI (For Enterprise/Advanced Use)
1. Go to the [Google Cloud Console](https://console.cloud.google.com/).
2. Create or select a project.
3. Enable the **Vertex AI API**.
4. Create a Service Account with appropriate permissions or use the OAuth flow.
5. *Note: The code in this project primarily uses the AI Studio API Key for simplicity.*

## 2. Configure Environment Variables

1. Open (or create) the `.env` file in the root directory of the project.
2. Add your API key using the following variable name:

```env
GEMINI_API_KEY=your_actual_api_key_here
```

## 3. Verify Connection

After setting up the key, you can run the diagnostic script to verify the connection:

```bash
npm run doctor
```

Or use the provided test script:

```bash
python scripts/tests/test_gemini_api.py
```
