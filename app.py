import streamlit as st
import requests
import json
import BuscarCep
import pandas as pd


##### TÍTULO DA APLICAÇÃO #####
st.sidebar.image("logo.png")
st.sidebar.title("Busca CEP")

##### Lista de Opções #####
st.sidebar.markdown("Aplicaçao para  buscar endereço a partir do CEP e mostrar a localizaçaono mapa")

##### BARRA LATERAL #####
opcoes = ["Buscar CEP", "Descobrir CEP"]
opcao= st.sidebar.selectbox("escolha uma opçao", opcoes)

##### BOTÃO BUSCAR CEP #####
if opcao == 'Buscar CEP':
    st.image("Principal.png")
    st.subheader("Buscar endereço pelo CEP")
    cep= st.text_input("Dgite o seu cep (apenas o numero).")

    if st.button("buscar"):
        if len(cep) != 8 or not cep.isdigit():
            st.error("por favo, insira um, cep validocom 8 digitos numericos.")
        else:
            try:
                endereco= BuscarCep.buscar_cep(cep)
                if endereco: 
                    st.success("Endereço encontrado")
                    st.write(f"CEP:{endereco[0]}")
                    st.write(f"Endereço:{endereco[1]}")
                    st.write(f"Bairro:{endereco[2]}")
                    st.write(f"Cidade:{endereco[3]}")
                    st.write(f"Estado:{endereco[4]}")

                    ##mapas
                    st.title("Localizaçao no Mapa")
                    df = pd.DataFrame({"latitude": [endereco[5]] , "longitude": [endereco[6]]})
                    st.map(df,zoom=15)
                else:
                    st.error("CEP nao encontrado.")
            except Exception as e:
                st.error(f"Ocorreu um erro ao bsucar o cep: {e}")

##### BOTÃO DESCOBRIR CEP #####
elif opcao == "Descobrir CEP":
    st.image("Descobrir.png")
    st.subheader("descobrir CEP pelo endereço")
    endereco_usuario =st.text_input("Digite seu endereço (ex: Rua Olga , Barueri , SP):")

    if st.button("Descobrir"):
        if not endereco_usuario.strip():
            st.error("Por favor , insira um endereço valido")
        else:
            try:
                resultado= BuscarCep.descobrir_cep(endereco_usuario)
                st.success("Link de busca no Google")
                st.write(resultado)
            except Exception as e:
                st.error(F"Ocorreu um erro ao descobrir o cep:{e}")
