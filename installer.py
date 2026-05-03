import locale

# lang = 'pt_PT', encoding = 'UTF-8'
lang, encoding = locale.getdefaultlocale()
portuguese = ["oi", "olá"]
english = ["bye", "goodbye"]

while True:
    entrada = input("Digite algo: ")

    if entrada in portuguese:
        print("Você disse oi ou olá!")

    elif entrada in english:
        print("You said bye or goodbye!")

    else:
        print("Entrada não reconhecida.")