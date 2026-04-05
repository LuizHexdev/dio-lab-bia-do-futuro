import json
import pandas as pd
import requests
import streamlit as st

# ====== CONFIGURAÇÃO ======

OLLAMA_URL = "httppython ://localhost:11434/api/generate"
MODELO = "gpt-oss"

# ====== CARREGAR DADOS ======

perfil = json.load(open('./data/perfil_investidor.json'))
transacoes = pd.read_csv('./data/transacoes.csv')
historico = pd.read_csv('./data/historico_atendimento.csv')
produtos = json.load(open('./data/produtos_financeiros.json'))

# ====== MONTAR CONTEXTO ======

contexto = f"""
CLIENTE: {perfil['nome']}, {perfil['idade']} anos, perfil {perfil['perfil_investidor']}
OBJETIVO: {perfil['objetivo_principal']}
PATRIMÔNIO: R$ {perfil['patrimonio_total']} | RESERVA: R$ {perfil['reserva_emergencia_atual']}

TRANSAÇÕES RECENTES: 
{transacoes.to_string(index=False)}

ATENDIMENTOS ANTERIORES:
{historico.to_string(index=False)}

PRODUTOS DISPONÍVEIS: 
{json.dumps(produtos, indent=2, ensure_ascii=False)} 
"""

# ====== SYSTEM PROMPT ======

SYSTEM_PROMPT = """Você é a Dina, uma consultora e educadora financeira didática e amigável.

OBJETIVO:
  Ensinar conceitos de finanças pessoais de maneira simples, usando os próprios dados do cliente como exemplos práticos.

REGRAS:
  1. Nunca recomende investimentos específicos, apenas explique como eles funcionam.
  2. Use os dados forne cidos para dar exemplos personalizados.
  3. Linguagem simples e didática, explicando de maneira simples como se fosse para um amigo.
  4. Se não souber de algo, admita: "Não tenho essa informação, mas posso explicar..."
  5. Sempre pergunte se o cliente entendeu.
  6. Responda de forma suinta e direta com no máximo 3 parágrafos.
""" 

# ====== CHAMAR O OLLAMA ======

def perguntar(msg):
    prompt = f"""
    {SYSTEM_PROMPT}

    CONTEXTO DO CLIENTE:
    {contexto}

    Pergunta: {msg}"""

    r = requests.post(OLLAMA_URL, json={"model": MODELO, "prompt": prompt, "stream": False})
    return r.json()['response']

# ====== CRIAÇÃO DA INTERFACE COM STREAMLIT ======

st.title("Dina, Sua educadora Financeira!")

if pergunta := st.chat_input("Sua dúvida sobre Finanças..."):
    st.chat_message("user").write(pergunta)
    with st.spinner("..."):
        st.chat_message("assistant").write(perguntar(pergunta))
