import streamlit as st
import time

def main():
    st.title("Letreiro Eletrônico - Estilo Neon")
    st.write("Criando um efeito de Neon simulado usando Streamlit.")

    # Campo de texto para inserir a mensagem
    mensagem = st.text_input("Digite a mensagem que deseja exibir:")

    # Escolha da cor Neon
    cor_neon = st.selectbox("Escolha uma cor Neon:", ["#ff0000", "#00ff00", "#0000ff", "#ff00ff", "#ffff00"])

    # Botão para iniciar o letreiro
    if st.button("Iniciar Letreiro"):

        # Verifica se a mensagem foi digitada
        if mensagem:
            # Exibe a mensagem com estilo Neon e efeito de movimento lateral
            st.write(
                f'<p style="font-size: 32px; color: {cor_neon}; text-shadow: 0 0 10px {cor_neon}, 0 0 20px {cor_neon}, 0 0 30px {cor_neon}, 0 0 40px {cor_neon}, 0 0 50px {cor_neon}; '
                f'white-space: nowrap; overflow: hidden; animation: marquee 5s linear infinite;">{mensagem}</p>',
                unsafe_allow_html=True
            )
            
if __name__ == "__main__":
    main()

