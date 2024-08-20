# 1- Pessoa Fisica/2 - Pessoa Juridica/3 - Sair

# 1 - Cadastrar Pessoa Fisica / 2 - Listar Pessoa FIsica / 3 - Sair

# 1 - Cadastrar Pessoa Juridica / 2 - Listar Pessoa Juridica / 3 - Sair

from Pessoa import Endereco, PessoaFisica

from datetime import date,datetime


def main():
    lista_pf=[]

    while True:
        opcao = int(input("Escolha uma opcao: 1 - Pessoa Fisica/ 2 - Pessoa Juridica/ 0 - Sair"))

        if opcao ==1:
            while True:
                opcao_pf = int(input("Escolha uma opcao: 1 - Cadastrar Pessoa Fisica / 2 - Listar Pessoa Fisica / 0 - Voltar ao menu anterior"))
                 #cadastrar uma pessoa
                if opcao_pf == 1:
                    novapf = PessoaFisica()
                    novo_end_pf =Endereco()

                    novapf.nome= input("Digite o nome da pessoa fisica")
                    novapf.cpf=  input("Digite o CPF")
                    novapf.rendimento = float(input("Digite o rendimento mental(Apenas numero)"))

                    data_nascimento= input("Digite a data de nascimento(dd/mm/aaaa)")
                    novapf.dataNascimento = datetime.strptime(data_nascimento, '%d/%m/%Y').date()
                    idade =(date.today() - novapf.dataNascimento).days // 365

                    if idade >= 18:
                        print("Pessoa tem mais de 18 anos")
                    else:
                        print("Pessoa menor de 18 anos. Retornando ao menu...")
                        continue # Retornar ao inicio do meu loop


                    #Cadastro de Endereco

                    novo_end_pf.logradouro = input("Digite o logradouro:")
                    novo_end_pf.numero = input("Digite o numero")
                    end_comercial = input("Este endereco e comercial: S/N")# Solicita se o endereco e comercial

                    novo_end_pf.endereco_Comercial = end_comercial.strip().upper() =="S" # define se o endereco e comercial com base na resposta
                    novapf.endereco = novo_end_pf

                    lista_pf.append(novapf)



                elif opcao_pf == 2:
                    if lista_pf:
                        for cada_pf in lista_pf:
                            print(f"Nome:{cada_pf.nome}")
                            print(f"CPF:{cada_pf.cpf}")
                            print(f"Endereco:{cada_pf.endereco.logradouro},{cada_pf.endereco.numero}")
                            print(f"CPF:{cada_pf.dataNascimento.strftime('%d/%m/%Y')}")
                            print(f"Imposta a ser pago:{cada_pf.calcular_imposto(cada_pf.rendimento)}")
                            print("Digite 0 para sair")
                            input()
                    else:
                        print("Lista Vazia")    
                #Sair do menu atual
                elif opcao_pf ==0:
                    print("Voltando ao menu Anteriro")
                    break 
                else:
                    print("Opcao invalida, por favor digite uma das opcoes indicadas")
        elif opcao ==2:
            print("Funcionalidades para pessoa juridica nao implementada")
        elif opcao == 0:
            print("Obrigado por utilizar o nosso sistema!!!Valeu")
            break 
        
        else:
            print("Opcao invalida, por favor digite uma das opcoes validas")         
                   



if __name__ =="__main__":
    main() #chama a funcao principal



        