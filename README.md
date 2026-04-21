# ThaiLLM API Proxy for Luna Translator

A Python-based proxy server designed to bridge **Luna Translator** with the **ThaiLLM (KBTG)** API. This project solves the authentication compatibility issue where Luna Translator uses standard OpenAI headers, but ThaiLLM requires a specific `apikey` header.

## 🚀 The Problem
Luna Translator's OpenAI interface defaults to `Authorization: Bearer <key>`. However, the ThaiLLM API endpoint requires the header format `apikey: <key>`. This discrepancy results in a `401 Unauthorized` error when attempting to connect directly.

## ✨ Solution
This proxy server acts as a middleman:
1. Receives standard OpenAI-compatible requests from Luna Translator on `localhost:8000`.
2. Intercepts and transforms the headers to match ThaiLLM's requirements.
3. Forwards the request to ThaiLLM and returns the fluent Thai translation back to Luna.

## 🛠️ Built With
- **Python 3.12+**
- **FastAPI**: For the lightweight web server.
- **Uvicorn**: ASGI server implementation.
- **Requests**: For handling external API communication.
- **uv**: Next-generation Python package manager.

## 📋 Installation & Usage

### Prerequisites
Ensure you have `uv` installed. If not, get it from [astral.sh/uv](https://astral.sh/uv).

### How to Run
1. Clone this repository or download `thaillm_proxy.py`.
2. Open your terminal in the project folder.
3. Run the proxy using:
   ```bash
   uv run --with fastapi --with uvicorn --with requests python thaillm_proxy.py

------------------------------------------------------------------------------------------------------------------------------------------

Compatibility: Tested with Luna Translator v10.15.6.30( https://github.com/HIllya51/LunaTranslator/releases/tag/v10.15.6.30 )
Luna Translator Configuration
Translator: General LLM / OpenAI

API Endpoint: http://127.0.0.1:8000/v1

API Key: Any dummy text (The proxy handles the real key)

Model: thalle-0.2-thaillm-8b-fa
