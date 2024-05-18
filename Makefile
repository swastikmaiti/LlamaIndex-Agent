install: 
		pip install -r requirements.txt

ollama_download:
		curl -fsSL https://ollama.com/install.sh | sh
		ollama serve
models:
		ollama pull phi3
		ollama pull llama3
		ollama pull nomic-embed-text

