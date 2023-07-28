import streamlit as st
import time

def main():
    st.title("Letreiro Eletrônico")

    # Campo de texto para inserir a mensagem
    mensagem = st.text_input("Surfe conosco a onda super gigante da Revolução da Inteligência Artificial:")

    # Botão para iniciar o letreiro
    if st.button("Iniciar Letreiro"):

        # Verifica se a mensagem foi digitada
        if mensagem:
            while True:
                # Exibe a mensagem
                st.write(mensagem)
                
                # Faz uma pausa para criar o efeito de movimento
                time.sleep(0.5)

                # Limpa a tela antes de exibir a mensagem novamente
                st.empty()
        else:
            st.warning("Por favor, digite uma mensagem para exibir.")

if __name__ == "__main__":
    main()
