import subprocess
import textwrap
import openai
import os

# Insérez votre clé API OpenAI ici
openai.api_key = ""

# Définissez le chemin du répertoire du programme à lancer
chemin_programme = __file__


def menu():
    print(
    "╔══════════════════════════════════════════════════════╗\n"
    "║ Bonjour Opium, je suis votre assistant GPT3 Python ! ║\n"
    "╚═════╦════════════════════════════════╦═══════════════╝\n"
    "      ╚════════╗  quit = quit  ╔═══════╝\n"
    "               ║ clear = clear ║\n"
    "               ║    restart    ║\n"
    "               ╚═══════════════╝")


def chatbot():
    menu()
    prompt = "\n > "
    while True:
        question = input(prompt)
        if question == "quit":
            break
        if question == "clear":
            subprocess.call("cls", shell=True)
            menu()
            continue
        if question == "restart":
            # Lancez le programme en utilisant subprocess.run()
            subprocess.call("cls", shell=True)
            subprocess.run(["python", chemin_programme])

        # Utilisez l'API GPT-3 pour obtenir une réponse à la question
        response = openai.Completion.create(engine="text-davinci-003",
                                            prompt=question,
                                            max_tokens=2048,
                                            n=1,
                                            stop=None,
                                            temperature=0.7)

        response_text = response['choices'][0]['text']
        # Utilisez la fonction fill() de textwrap pour splitter le texte en plusieurs lignes
        texte_split = textwrap.fill(response_text, width=120)
        chaine = texte_split

        chaine = chaine.replace("  ", "\n ")
        print("\n")
        print("══════════════════════════════════════════════════")
        print(chaine)
        print("══════════════════════════════════════════════════")


# Démarrez le chatbot
chatbot()
