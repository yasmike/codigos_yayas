import streamlit as st
st.sidebar.title ("aluguel de carros")
st.sidebar.image("logo.png")
st.sidebar.write("escolha o carro ideal para voce")
carros = ["Gol", "BMW" , "Porsche", "Toro"]

opçao = st.sidebar.selectbox("Escolha qual carro voce gostaria de alugar" , carros)


#----------principal
st.title("yaya's cars - Aluguel de carros!!")
st.image(f'{opçao}.png')
st.markdown(f"## voce alugou o modelo : {opçao}")

#-----------------
dias = st.text_input (f"Por quantos dias o {opçao} foi alugado?")
km = st.text_input(f"Quantos km voce rodou com o {opçao}")

#copia -- define a diaria
if opçao == "Gol":
    diaria = 450

elif opçao == "BMW":
    diaria= 500

elif opçao == "Porsche":
    diaria= 700

elif opçao == "Toro":
    diaria = 400

### calcular

if st.button("calcular"):
    dias= int(dias)
    km = float(km)

    total_dias = dias * diaria
    total_km = km * 0.15
    aluguel_total= total_dias + total_km
    st.warning(f"Voce alugo o {opçao} por {dias} dias e rodou {km}km. O valor total a pagar é r${aluguel_total:.2f}")