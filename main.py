from core.chatbot import Chatbot


def main():

    chatbot = Chatbot()

    print("===================================")
    print("LinkedIn Post Generator Chatbot")
    print("Escribe 'salir' para terminar")
    print("===================================")

    while True:

        user_input = input("\nTu solicitud: ")

        if user_input.lower() in ["salir", "exit", "quit"]:
            print("\nHasta luego.")
            break

        try:

            response = chatbot.process_user_input(user_input)

            print("\nPublicación generada:\n")
            print(response)

        except Exception as e:

            print("\nError al procesar la solicitud:")
            print(e)
