def cadastrarcontato():
    idcontato = input(" Escolha o ID do contato: ")
    nome = input(" Escolha o nome do contato: ")
    telefone = input(" Escolha o Telefone do contato: ")
    email = input(" Escolha o Email do contato: ")

    try:
        agenda= open("agenda.txt", "a")
        dados= f'{idcontato};{nome};{telefone};{email} \n'
        agenda.write(dados)
        agenda.close
        print(f'Contato gravado com sucesso!')
    except:
        print("Erro na gravação!")
        

def listarcontato():
    with open("agenda.txt", "r") as agenda:
        for contato in agenda:
         print(contato)
    

def deletarcontato():
    nomedel = input("Digite o nome para deletar: ").lower()

    with open("agenda.txt", "r") as agenda:
        linhas = agenda.readlines()

    linhas = [linha for linha in linhas if nomedel not in linha.lower()]

    with open("agenda.txt", "w") as agenda:
        agenda.writelines(linhas)

    print(f"Se havia contato com '{nomedel}', ele foi deletado.")


def buscarcontatopelonome():
     nome=input("Digite qual o nome deseja buscar: ").lower()
     with open("agenda.txt", "r") as agenda:
        for contato in agenda:
            if nome in contato.split(";")[1].lower(): # Seperando apenas a linha do nome
                print(contato)
                break
        else:
                print(f"O nome {nome} nao esta na agenda !")
            

def menu():
    opcao = input('''
================================================================
                PROJETO AGENDA EM PYTHON
MENU:
[1] CADASTRAR CONTATO
[2] LISTAR CONTATO            
[3] DELETAR CONTATO          
[4] BUSCAR CONTATO PELO ID
[0] SAIR
================================================================
ESCOLHA UMA OPÇÃO ACIMA:
''')

    if opcao == "1":
        cadastrarcontato() 
        menu()  # chama menu de novo
    elif opcao == "2":
        listarcontato()  
        menu()
    elif opcao == "3":
        deletarcontato()
        menu()
    elif opcao == "4":
        buscarcontatopelonome()
        menu()
    elif opcao == "0":
        print("Saindo do programa")
        return  # para sair da recursão
    else:
        print("Erro: opção inválida.")
        menu()  # tenta de novo

def main():
    menu()

main()