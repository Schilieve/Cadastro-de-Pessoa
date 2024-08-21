# 1- Pessoa Fisica/2 - Pessoa Juridica/3 - Sair

# 1 - Cadastrar Pessoa Fisica / 2 - Listar Pessoa FIsica / 3 - Sair

# 1 - Cadastrar Pessoa Juridica / 2 - Listar Pessoa Juridica / 3 - Sair

from Pessoa import Endereco, PessoaFisica,PessoaJuridica

from datetime import date,datetime


def main():
    lista_pf=[]
    lista_pj =[]

    while True:
        opcao = int(input("Escolha uma opcao: 1 - Pessoa Fisica/ 2 - Pessoa Juridica/ /3-Atualizar lista/0 - Sair"))

        if opcao ==1:
            while True:
                opcao_pf = int(input("Escolha uma opcao: 1 - Cadastrar Pessoa Fisica / 2 - Listar Pessoa Fisica / 3- exluir cpf da lista/ 0 - Voltar ao menu anterior"))
                 #cadastrar uma pessoa Fisica
                if opcao_pf == 1:
                    novapf = PessoaFisica()
                    novo_end_pf =Endereco()

                    novapf.nome= input("Digite o nome da pessoa fisica")
                    novapf.cpf=  input("Digite o CPF")
                    novapf.rendimento = float(input("Digite o rendimento mensal(Apenas numero)"))

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
                # remover pessoa da lista atual 
                
                elif opcao_pf == 3:

                    cpf_para_remover = input("Digite o cpf")
                    pessoa_encontrada = False
                                

                    for cada_pf in lista_pf:
                            if cada_pf.cpf == cpf_para_remover:
                               lista_pf.remove(cada_pf)
                               pessoa_encontrada = True
                               print("Pessoa Fisica Removida")
                               break
                            if not pessoa_encontrada:
                                print("Nenhuma pessoa encontrada")
                
                
              # Atualização de dadados do cadastro


                      # Atualizar Lista
                if opcao_pf == 4:
                    cpf_para_atualizar = input("Digite o CPF que deseja atualizar: ")
                    pessoa_encontrada = False

                    for cada_pf in lista_pf:
                        if cada_pf.cpf == cpf_para_atualizar:
                            pessoa_encontrada = True

                            print("Escolha qual dado deseja atualizar")
                            print("N - Nome")
                            print("R - Rendimento")
                            print("L - Logradouro")
                            print("M - Numero")

                            escolha = input("Digite a inicial do atributo que deseja alterar:")

                            if escolha == "N":
                                novo_nome = input(f"O nome atual é {cada_pf.nome}. Digite o novo nome para atualizar: ")
                                cada_pf.nome = novo_nome
                            elif escolha == "R":
                                novo_rendimento = input(f"O rendimento atual é {cada_pf.rendimento}. Digite o novo valor do rendimento: ")
                                cada_pf.rendimento = novo_rendimento
                            elif escolha == "L":
                                novo_logradouro = input(f"O logradouro atual é {cada_pf.logradouro}. Digite o novo logradouro: ")
                                cada_pf.logradouro = novo_logradouro
                            elif escolha == "M":
                                novo_numero = input(f"O número atual é {cada_pf.numero}. Digite o novo número para atualizar")
                                cada_pf.numero = novo_numero
                            else:
                                print("Opção inválida!")
                                break
                        
                            

                    
                        

                
                
            
                
                elif opcao_pf ==0:
                    print("Voltando ao menu Anteriro")
                    break 
                else:
                    print("Opcao invalida, por favor digite uma das opcoes indicadas")
                    # PESSOA JURIDICA 

        elif opcao ==2:
            
            while True:
                opcao_pj = int(input("Escolha uma opcao: 1 - Cadastrar Pessoa Juridica/ 2 - Listar Pessoa Juridica/ 3- exluir CNPJ da lista/ 0 - Voltar ao menu anterior"))
                 #cadastrar uma pessoa Juridica
                if opcao_pj == 1:
                    novapj = PessoaJuridica()
                    novo_end_pj =Endereco()

                    novapj.nome= input("Digite o nome da Empresa")
                    novapj.cnpj=  input("Digite o CNPJ")
                    novapj.rendimento = float(input("Digite o rendimento mensal(Apenas numero)"))

                   


                    #Cadastro de Endereco

                    novo_end_pj.logradouro = input("Digite o logradouro:")
                    novo_end_pj.numero = input("Digite o numero")
                    end_comercial = input("Este endereco e comercial: S/N")# Solicita se o endereco e comercial

                    novo_end_pj.endereco_Comercial = end_comercial.strip().upper() =="S" # define se o endereco e comercial com base na resposta
                    novapj.endereco = novo_end_pj

                    lista_pj.append(novapj)



                elif opcao_pj == 2:
                    if lista_pj:
                        for cada_pj in lista_pj:
                            print(f"Nome:{cada_pj.nome}")
                            print(f"CPF:{cada_pj.cnpj}")
                            print(f"Endereco:{cada_pj.endereco.logradouro},{cada_pj.endereco.numero}")
                            
                            print(f"Imposta a ser pago:{cada_pj.calcular_imposto(cada_pj.rendimento)}")
                            print("Digite 0 para sair")
                            input()
                    else:
                        print("Lista Vazia")    
                #Sair do menu atual
                # remover pessoa da lista atual 
                
                elif opcao_pj == 3:

                    cnpj_para_remover = input("Digite o cnpj que deseja remover")
                    empresa_encontrada = False
                                

                    for cada_pj in lista_pj:
                            if cada_pj.cnpj == cnpj_para_remover:
                               lista_pj.remove(cada_pj)
                               empresa_encontrada = True
                               print("Pessoa Juridica Removida")
                               break
                    if not empresa_encontrada:
                        print("Nenhuma pessoa Juridica encontrada")
                    
        elif opcao == 0:
            print("Obrigado por utilizar o nosso sistema!!!Valeu")
            # Atualizar Lista
            if opcao_pj == 4:
                    if lista_pj:
                        cnpj_para_atualizar = input("Digite o CNPJ da Empresa que deseja atualizar:")
                        for cada_pj in lista_pj:
                            if cada_pj.cnpj == cnpj_para_atualizar:
                                novo_rendimento = float(input("Digite o novo rendimento: "))
                                cada_pj.rendimento = novo_rendimento
                                print("Rendimento atualizado com sucesso!")
                                break
                        else:
                            print("Nenhum CNPJ encontrado")


                # Sair do menu Atual
            elif opcao_pf == 0:
                    print("Voltando ao menu anterior")
                    break 

            else: 
                    print("Opção inválida, por favor digite uma das opções abaixo indicadas.")      

            print("Funcionalidades para pessoa jurídica não implementadas.")
            pass


        elif opcao == 0:
            print("Obrigado por utilizar nosso sistema!")
            break
            break 
        
        else:
            print("Opcao invalida, por favor digite uma das opcoes validas")
                    

    
       

      
            

 



if __name__ =="__main__":

    main() #chama a funcao principal



        