# Passo a Passo de Execução


## Setup do Ollama (5-10 minutos)

```
1. Installar o Ollama (Ollama.com)
2. Baixar um modelo leve
ollama pull gpt-oss

# Testar
ollama run gpt-oss "Olá!"
```

## Código Completo

Todo o código fonte está contido no arquivo `app.py`.

## Como Rodar

```bash
# 1. Instalar dependências
# No terminal, execute:
pip install pandas streamlit requests

# 2. Verificar se o Ollama está rodando
ollama server

# 3. Rodar a aplicação
streamlit run .\src\app.py
```
