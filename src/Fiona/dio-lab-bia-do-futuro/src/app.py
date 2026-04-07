# =========== CARREGAR DADOS =========
import json
import pandas as pd
import requests
import streamlit as st

OLLAMA_URL= "http://localhost:11434/api/tags"
MODELO = "gpt-oss:20b-cloud"


perfil = json.load(open("C:/Users/natal/OneDrive/Fiona/dio-lab-bia-do-futuro/data/perfil_investidor.json", encoding="utf-8"))
transacoes = pd.read_csv('C:/Users/natal/OneDrive/Fiona/dio-lab-bia-do-futuro/data/transacoes.csv')
historico = pd.read_csv("C:/Users/natal/OneDrive/Fiona/dio-lab-bia-do-futuro/data/historico_atendimento.csv")
produtos = json.load(open("C:/Users/natal/OneDrive/Fiona/dio-lab-bia-do-futuro/data/produtos_financeiros.json", encoding="utf-8"))

#======== contexto ================
contexto= f"""
CLIENTE: {perfil["nome"]}, {perfil["idade"]} anos.
OBJETIVO: Reserva de Emergência e {perfil["objetivo_segundario"]}
PATRIMÔNIO: R$: {perfil["reserva_emergencial_atual"]}

Transacoes_recentes: 
{transacoes.to_string(index=False)}

Atendimento_anteriores:
{historico.to_string(index=False)}

Produto_disponivel:
{json.dumps(produtos, indent=2, ensure_ascii=False)} """



#=============== SYSTEM PROMPT ===============

SYSTEM_PROMPT = """Você é a Fiona , uma agente financeiro inteligente especializado em Reservas de emergência.

Seu objetivo é monitorar as transaçoes para fins de poupança .

REGRAS:
1. Sempre baseie suas respostas nos dados fornecidos
2. Nunca invente informações financeiras
3. Se não souber algo, admita e ofereça alternativas
4. linguagem simples , como se estivesse conversando com amigo"""

#=========== CHAMAR OLLAMA ===================

def perguntar(msg):
    prompt = f"""{SYSTEM_PROMPT}

CONTEXTO DO CLIENTE:
{contexto}

pergunta:{msg}"""
    
    r = requests.post(OLLAMA_URL,json= {"model":MODELO,"prompt":prompt , "stream":False})
    return r.json()["response"]

#========= INTERFACE================
st.title(" Fiona , seu Agente financeiro")

if pergunta:= st.chat_input ("sua transacão ..."):
    st.chat_message("user").write(pergunta)
    with st.spinner("..."):
        st.chat_message("assistant").write(perguntar(pergunta))