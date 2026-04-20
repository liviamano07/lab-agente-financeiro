import streamlit as st
import pandas as pd
import json

# =========================
# CONFIGURAÇÃO DA PÁGINA
# =========================
st.set_page_config(
    page_title="FinCoach AI",
    page_icon="🧠",
    layout="centered"
)

st.title("🧠 FinCoach AI")
st.subheader("Seu assistente financeiro educacional")

# =========================
# CARREGAMENTO DOS DADOS
# =========================
@st.cache_data
def load_data():
    transacoes = pd.read_csv("data/transacoes.csv")

    with open("data/perfil_investidor.json", "r", encoding="utf-8") as f:
        perfil = json.load(f)

    with open("data/produtos_financeiros.json", "r", encoding="utf-8") as f:
        produtos = json.load(f)

    return transacoes, perfil, produtos


transacoes, perfil, produtos = load_data()

# =========================
# FUNÇÕES DE ANÁLISE
# =========================
def total_gastos():
    return transacoes[transacoes["tipo"] == "saida"]["valor"].sum()

def gastos_por_categoria():
    return transacoes[transacoes["tipo"] == "saida"].groupby("categoria")["valor"].sum()

def gastos_nao_essenciais():
    return transacoes[
        (transacoes["tipo"] == "saida") &
        (transacoes["essencial"] == "nao")
    ]["valor"].sum()

def simular_economia(valor_mensal, meses=12):
    return valor_mensal * meses

# =========================
# SIDEBAR (PERFIL)
# =========================
st.sidebar.header("👤 Perfil do Usuário")

st.sidebar.write(f"**Nome:** {perfil['nome']}")
st.sidebar.write(f"**Perfil:** {perfil['perfil_financeiro']['tipo']}")
st.sidebar.write(f"**Renda:** R$ {perfil['renda_mensal']}")

# =========================
# DASHBOARD SIMPLES
# =========================
st.markdown("## 📊 Visão financeira")

col1, col2, col3 = st.columns(3)

col1.metric("Gastos totais", f"R$ {total_gastos():.2f}")
col2.metric("Não essenciais", f"R$ {gastos_nao_essenciais():.2f}")
col3.metric("Renda mensal", f"R$ {perfil['renda_mensal']:.2f}")

st.markdown("### 📂 Gastos por categoria")
st.bar_chart(gastos_por_categoria())

# =========================
# SIMULAÇÃO FINANCEIRA
# =========================
st.markdown("## 💰 Simulação financeira")

valor = st.number_input("Quanto você quer economizar por mês?", min_value=0.0, value=100.0)

if st.button("Simular 12 meses"):
    resultado = simular_economia(valor)
    st.success(f"Em 1 ano você terá economizado R$ {resultado:.2f}")

# =========================
# CHAT (IA SIMULADA)
# =========================
st.markdown("## 💬 Converse com o FinCoach AI")

if "chat" not in st.session_state:
    st.session_state.chat = []

user_input = st.text_input("Digite sua pergunta:")

def responder(pergunta):
    pergunta = pergunta.lower()

    if "gasto" in pergunta:
        return f"Você gastou R$ {total_gastos():.2f} no total no período analisado."

    if "economizar" in pergunta:
        return "Posso te ajudar com simulações! Use a seção de simulação financeira abaixo."

    if "categoria" in pergunta:
        return gastos_por_categoria().to_string()

    if "reserva" in pergunta:
        return f"Sua reserva atual é de R$ {perfil['situacao_financeira']['reserva_emergencia_atual']}."

    return "Posso te ajudar com gastos, simulações, categorias e sua reserva financeira."

if user_input:
    resposta = responder(user_input)

    st.session_state.chat.append(("Você", user_input))
    st.session_state.chat.append(("FinCoach AI", resposta))

# Exibir histórico
for role, msg in st.session_state.chat:
    if role == "Você":
        st.markdown(f"🧑‍💬 **Você:** {msg}")
    else:
        st.markdown(f"🤖 **FinCoach AI:** {msg}")
