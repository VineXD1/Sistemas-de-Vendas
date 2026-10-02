# Titulo
# Seção Cadastrar Vendas
    # Campo Data
    # Campo vendedor
    # Campo Produto
    # Campo Quantidade
    # Campo Valor
    # Campo Cadastrar Venda
        # quando eu clicar no botão -> adicionar a venda na tabela
    # Seção Vendas Cadastradas
        # Tabela com as Vendas
    # Seção Dashboard
        # Card/Métrica -> Faturamento Total
        # Gráfico de Barra/Coluna -> Vendar por vendedor
        # Gráfico de Pizza -> Venda por produto

# pip install streamlit pandas plotly
# streamlit run codigo.py

import streamlit as st
import pandas as pd
import plotly.express as px

# Carregar a Base de Vendas
tabela_vendas = pd.read_csv("vendas.csv")

st.write("# Sistema de Vendas")

# seção de cadastro de vendas
st.sidebar.write("## Cadastrar Vendas")
data = st.sidebar.date_input("Data")
vendedor = st.sidebar.selectbox("Vendedor", ["Maria", "Pedro", "Claudia"])
produto = st.sidebar.selectbox("Produto", ["Celular", "Tablet", "Carregador"])
quantidade = st.sidebar.number_input("Quantidade", step=1)
valor = st.sidebar.number_input("Valor")
botao_cadastrar = st.sidebar.button("Cadastrar Venda")

# logica de cadastro
if botao_cadastrar:
    if valor <= 0 or quantidade <= 0:
        st.warning("ERRO: Valor Vazio ")
    else:    
        nova_venda = [str(data), vendedor, produto, quantidade ,valor]
        ultima_linha= len(tabela_vendas) #120 linhas
        tabela_vendas.loc[ultima_linha] = nova_venda
        tabela_vendas.to_csv("vendas.csv", index=False)
        st.success("Venda Cadastrada!")

# seção de visualizar as vendas
st.write("## Vendas Cadastradas")
st.dataframe(tabela_vendas)

# seção de Dashboard
st.write("## Dashboard")

# Card/Métrica -> Faturamento Total
faturamento = tabela_vendas["valor"].sum()
st.metric("Faturamento Total", f"R$ {faturamento}")

# Gráfico de Barra/Coluna -> Vendar por vendedor
grafico1 = px.bar(tabela_vendas, x="vendedor" , y="valor", color="produto")
st.plotly_chart(grafico1)

# Gráfico de Pizza -> Venda por produto
grafico2 =px.pie(tabela_vendas, names="produto", values="valor", hole=0.4)
st.plotly_chart(grafico2)
