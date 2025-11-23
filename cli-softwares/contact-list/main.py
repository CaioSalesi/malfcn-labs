import os

from time import sleep

contactList = {
    1: {
        "Name": "Example Contact",
        "Number": "66991122335",
        "E-mail": ""
    },
    2: {
        "Name": "Example Contact",
        "Number": "14935619999",
        "E-mail": "example@contact.net"
    }
}

def advanced_input(mode:int, rule:str, input_text:str):
    # mode 1: mandatory answer
    # mode 2: optional answer
    # rule "just_number": intuitive, right?
    # rule "just_text": intuitive, right?!
    # rule "both": INTUITIVE, RIGHT?!

    rule = rule.lower()

    if mode not in (1, 2):
        print("Modo inválido para a função advanced_input.")
        return 0
    elif rule not in ("just_number", "just_text", "both"):
        print("Regra inválida para a função advanced_input.")
        return 0

    while 1:
        response = input(input_text)

        if response == "":
            if mode == 1:
                print("[!] Esse campo é obrigatório.")
            else:
                return response
        else:
            if rule == "just_number":
                if not response.isnumeric():
                    print("[!] Resposta inválida. Digite apenas NÚMEROS, sem letras ou caracteres especiais.")
                else:
                    return response
            elif rule == "just_text":
                if not response.replace(" ", "").isalpha():
                    print("[!] Resposta inválida. Digite apenas LETRAS, sem números ou caracteres especiais.")
                else:
                    return response
            else:
                return response

def add_contact(name:str, number:str="", email:str=""):
    contact_id = len(contactList) + 1

    contactList[contact_id] = {
        "Name": name,
        "Number": number,
        "E-mail": email
    }

    print("[!] Contato adicionado com êxito.")

def edit_contact(contact_id:int, name:str="", number:str="", email:str=""):
    if contact_id in contactList:

        if name != "":
            contactList[contact_id]['Name'] = name

        if number != "":
            contactList[contact_id]['Number'] = number

        if email != "":
            contactList[contact_id]['E-mail'] = email

        print("[!] Contato editado com êxito.")
    else:
        print(f"[!] Esse ID ({contact_id}) não existe na sua lita de contatos.")

def rm_contact(contact_id:int):
    try:
        contactList.pop(contact_id)

        ids_tuple = tuple(contactList.keys())

        for contact in ids_tuple:
            if contact > contact_id:
                contactList[contact - 1] = contactList.pop(contact)

        print(f"[!] O contato {contact_id} foi excluído e a sua lista foi atualizada.")

    except KeyError:
        print(f"[!] Esse ID ({contact_id}) não existe na sua lita de contatos.")

def show_contacts(title:str="lista de contatos", clist=None):
    print(f"\n{title.upper()}")

    if clist is None:
        clist = contactList

    if len(clist) > 0:
        for contact in clist:
            print()
            print(f"{contact}\t\tName: {clist[contact]['Name']}")
            print(f"\t\tNumber: {clist[contact]['Number']}")
            print(f"\t\tE-mail: {clist[contact]['E-mail']}")
    else:
        print()
        print("[!] Vazio.")

def search_contacts(search_string:str):
    contactlist_copy = dict()

    search_string = search_string.lower()

    for contact in contactList:
        name_similarity = search_string in contactList[contact]["Name"].lower()
        number_similarity = search_string in contactList[contact]["Number"]
        email_similarity = search_string in contactList[contact]["E-mail"].lower()

        if name_similarity or number_similarity or email_similarity:
            contactlist_copy[contact] = contactList[contact]

    show_contacts("resultados", contactlist_copy)

def export_contacts(filename:str="contacts"):
    if filename == "":
        filename = "contacts"

    with open(f'{filename}.csv', 'w', encoding='utf-8') as file:
        for contact in contactList:
            name = contactList[contact]['Name']

            number = contactList[contact]['Number']
            if number == "":
                number = "null"

            email = contactList[contact]['E-mail']
            if email == "":
                email = "null"

            file.write(f'{name};{number};{email}\n')

    print(f"[!] Lista de contatos exportada para o arquivo {filename}.")

def import_contacts(filename:str):
    global contactList

    if os.path.exists(filename):
        temp_contactlist = dict()

        with open(filename, 'r', encoding='utf-8') as file:
            for index, register in enumerate(file):
                register_data = register.strip().split(';', 2)

                if len(register_data) < 3:
                    print("[!] Dados em formato extremamente incompatível.")
                    break
                else:
                    temp_contactlist[index + 1] = {
                        'Name': register_data[0],
                        'Number': register_data[1],
                        'E-mail': register_data[2]
                    }

        contactList = dict(temp_contactlist)

        print("[!] Lista de contatos importada com êxito.")
    else:
        print("[!] Arquivo não encontrado.")

# Program
while 1:
    print("\nCONTACT LIST PYTHON PROGRAM - Selecione uma opção:")
    print("[1] Ver lista de contatos")
    print("[2] Buscar contato")
    print("[3] Adicionar contato")
    print("[4] Editar contato")
    print("[5] Remover contato")
    print("[6] Exportar lista de contatos para CSV")
    print("[7] Carregar lista de contatos de CSV")
    print("[8] Sair do programa (as alterações não serão salvas)")

    option = int(input("\n> "))

    if option == 1:
        show_contacts()
        sleep(2.5)

    elif option == 2:
        search_contacts(str(advanced_input(1, "both", "Pesquisa > ")))
        sleep(2.5)

    elif option == 3:
        nameResponse = str(advanced_input(1,"just_text", "Nome > "))
        numberResponse = str(advanced_input(2, "just_number", "Número > "))
        emailResponse = str(advanced_input(2, "both", "E-mail > "))

        add_contact(nameResponse, numberResponse, emailResponse)
        sleep(2)

    elif option == 4:
        idResponse = int(advanced_input(1, "just_number", "ID > "))

        if idResponse in contactList:
            nameResponse = str(advanced_input(2,"just_text", "Nome (mantenha em branco para não alterar) > "))
            numberResponse = str(advanced_input(2, "just_number", "Número (mantenha em branco para não alterar) > "))
            emailResponse = str(advanced_input(2, "both", "E-mail (mantenha em branco para não alterar) > "))

            edit_contact(idResponse, nameResponse, numberResponse, emailResponse)
        else:
            print(f"[!] Esse ID ({idResponse}) não existe na sua lita de contatos.")

        sleep(2)

    elif option == 5:
        idResponse = int(advanced_input(1, "just_number", "ID > "))

        rm_contact(idResponse)

        sleep(2)

    elif option == 6:
        export_contacts(str(advanced_input(2, "just_text", "Nome do arquivo (sem extensão) > ")))

        sleep(2)

    elif option == 7:
        import_contacts(str(advanced_input(1, "both", "Nome do arquivo > ")))

        sleep (2)

    elif option == 8:
        quit()

    else:
        print("[!] Opção INVÁLIDA. Leia o menu.")
