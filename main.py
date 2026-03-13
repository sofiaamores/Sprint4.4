from core.chatbot import Chatbot


def main():

    chatbot = Chatbot()

    print("===================================")
    print("LinkedIn Post Generator Chatbot")
    print("Escribe 'salir' para terminar")
    print("===================================")

    while True:

        user_input = input("\nTu solicitud: ")

        if user_input.lower() == "salir":
            break

        print("\nProcesando consulta...\n")

        response = chatbot.process_user_input(user_input)

        print("\nPublicación generada:\n")
        print(response)


if __name__ == "__main__":
    main()
