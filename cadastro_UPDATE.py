print("AGENDA do ADS")

menu = "1"

while menu == "1" or menu == "2" or menu == "3":
    menu = input("Digite a opção desejada: \n 1 - Cadastrar \n 2 - Consultar \n 3 - Sair  \n")



    while menu != "1" and  menu != "2" and  menu != "3":
            print("Opção invalida!!! DIGITE NOVAMENTE!!")
            menu = input("Digite a opção desejada: \n 1 - Cadastrar \n 2 - Consultar \n 3 - Sair  \n")


    
    if menu =="1":
        lista_nome = []
        nome = input("Digite seu Nome: ")
        

        rua = input("Digite da sua Rua: ")
        cep = input("Digite seu CEP:")
        bairro = input("Digite seu Bairro: ")
        estado = input("Digite o estado onde mora")
        telefone = int(input("Digite seu ddd e telefone <sem espaços>"))

        
        dados = ("Nome:{0} Rua:{1} CEP:{2} Bairro:{3} Estado:{4} Telefone:{5}' ".format(nome,rua,cep,bairro,estado,telefone))
        

        print("{0} CADASTRADO COM SUCESSO".format(nome))

        arquivo = open('cadastro.txt','a')
        arquivo.write(dados + "\n")
        print("Dados Adicionados no arquivo")
        arquivo.close()
        


        

    elif menu == "2":
        palavra = input('palavra a pesquisar ')
        for line in open('cadastro.txt'):
            if palavra in line:
                print(line)

        
    elif menu == "3":
        print("Obrigado por utilizar!!!")
        break




            




    
    
            

    
        
        
        
        

        
        


            

        


    








