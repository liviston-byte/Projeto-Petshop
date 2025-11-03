servicos = [['Banho', 25.0]]
produtos = [['Ração', 10.0, 20]]
horarios = [['15:00']]
agendapet = []
compras = []
usuarios = [['adm', 'adm123', 'junior', '123']]

while True:
    opcao = input('\nBem-vindo ao SertãoPet\n\n1 - Cadastrar-se\n2 - Login\n0 - Sair\n\nDigite sua opção: ')

    # Opção de Sair do Programa
    if opcao == '0':
        print('Saindo...')
        break

    # Opção de Cadastro
    elif opcao == '1':
        print('\nInforme seus dados abaixo. ')
        nome = input('Digite seu nome: ')
        usuario = input('Digite seu usuario: ')
        senha = input('Digite sua senha: ')
        
        usuario_existe = False
        for u in usuarios:
            if u[0] == usuario:
                usuario_existe = True
                break
        if usuario_existe:
            print('Usuário já cadastrado, tente outro nome de usuário.')
        else:
            usuarios.append([usuario, senha])
            print(f'Cadastro realizado com sucesso! Bem-vindo, {nome}')

    # Opção de Login
    elif opcao == '2':
        while True:
            print('\n----- Menu de Login -----')
            print('Efetue o login')
            usuario = input('Usuario: ')
            senha = input('Senha: ')

            logado = False
            for u in usuarios:
                if(u[0] == usuario and u[1] == senha):
                    logado = True
            if logado:
                print(f'Login bem-sucedido! Olá, {usuario}.')
                
                # Menu do Administrador
                if usuario == 'adm':
                    while True:
                        print('\n----- Menu Administrador -----')
                        print('1 - Cadastra produto')
                        print('2 - Cadastrar serviço')
                        print('3 - Listar produtos')
                        print('4 - Listar serviços')
                        print('5 - Alterar produto')
                        print('6 - Alterar serviço')
                        print('7 - Remover produto')
                        print('8 - Remover serviço')
                        print('9 - Procurar Produto')
                        print('10 - Procurar Serviços')
                        print('0 - Sair')
                        escolha = input('Digite sua opção: ')

                        if escolha == '1':
                            produto = input('Digite o produto que deseja cadastrar: ').lower()
                            valor = float(input('Digite o valor do produto: '))
                            while valor < 0:
                                print('Valor invalido, apenas valores acima de 0')
                                valor =  float(input("Digite um novo valor: "))
                            estoque = int(input('Digite a quantidade do produto: '))
                            while estoque<0:
                                print('Valor invalido, apenas valores acima de 0')
                                estoque= int(input('Digite novamente a quantidade: '))
                            produtos.append([produto, valor, estoque])

                        elif escolha == '2':
                            servico = input('Digite o serviço que deseja cadastrar: ').lower()
                            preco = float(input('Digite o valor do serviço: '))
                            horario = input('Digite horários disponiveis para atendimento: ')
                            while preco < 0:
                                print('Valor invalido, apenas valores acima de 0')
                                preco = float(input('Digite novamente o valor do serviço: '))
                            servicos.append([servico, preco])
                            horarios.append([horario])

                        elif escolha == '3':
                            print('\n\n--------------------------------')
                            print('Produtos dísponiveis\n\n')
                            for p in produtos:
                                print(f'Produto: {p[0]} | Preço: R${p[1]} | Em estoque: {p[2]}')
                            print('--------------------------------\n\n')

                        elif escolha == '4':
                            print('\n\n--------------------------------')
                            print('Serviços dísponiveis\n\n')
                            for s in servicos:
                                print(f'Serviço: {s[0]} | Preço: R${s[1]}')
                            print('--------------------------------\n\n')

                        elif escolha == '5':
                            for indice in range(len(produtos)):
                                print(f'Código {indice} - Produto {produtos[indice][0]}')
                            
                            indice = int(input('Digite o indice que deseja alterar: '))
                            while indice < 0 or indice >= len(produtos):
                                print('Inválido')
                                indice = int(input('Digite o indice que deseja alterar: '))
                            
                            produto = input('Digite o novo produto: ')
                            valor = input('Digite o novo valor do produto: ')
                            estoque = input('Digite a nova quantidade do produto: ')
                            novaSublista = [produto, valor, estoque]
                            produtos[indice] = novaSublista
                        
                        elif escolha == '6':
                            for indice in range(len(servicos)):
                                print(f'Código {indice} - Produto {servicos[indice][0]}')
                            
                            indice = int(input('Digite o indice que deseja alterar: '))
                            while indice < 0 or indice >= len(servicos):
                                print('Inválido')
                                indice = int(input('Digite o indice que deseja alterar: '))
                            
                            servico = input('Digite o novo serviço: ')
                            preco = input('Digite o novo valor: ')
                            novaSublista = [servico, preco]
                            servicos[indice] = novaSublista

                        elif escolha == '7':
                            for indice in range(len(produtos)):
                                print(f'Código {indice} - Produto {produtos[indice][0]}')

                            indice = int(input('Digite o indice que deseja remover: '))
                            while indice < 0 or indice >= len(produtos):
                                print('Inválido')
                                indice = int(input('Digite o indice que deseja remover: '))

                            produtos.remove(produtos[indice])

                        elif escolha == '8':
                            for indice in range(len(servicos)):
                                print(f'Código {indice} - Produto {servicos[indice][0]}')

                            indice = int(input('Digite o indice que deseja remover: '))
                            while indice < 0 or indice >= len(servicos):
                                print('Inválido')
                                indice = int(input('Digite o indice que deseja remover: '))

                            servicos.remove(servicos[indice])

                        elif escolha == '9':
                            print(produtos)
                            busca= input('Qual produto deseja procurar: ').lower()
                            encontrado = False
                            for b in produtos:
                                if b[0].lower() == busca.lower():
                                    print(f'Produto encontrado {b[0]} | Preço: R${b[1]} | Estoque: {b[2]}')
                                    encontrado = True
                                    break
                                    
                            if not encontrado:
                                    print('Produto não encontrado')

                        elif escolha == '10':
                            print(servicos)
                            busca = input('Qual serviço deseja procurar: ').lower()
                            encontrado = False
                            for s in servicos:
                                if s[0].lower() == busca:
                                    print(f'Serviço encontrado: {s[0]} | Preço: R${s[1]}')
                                    encontrado = True
                                    break
                            if not encontrado:
                                print('Serviço não encontrado')

                        elif escolha == '0':
                            print('Saindo...')
                            break
                        else:
                            print('Opção inválida, tente novamente.')
                
                # Menu do Cliente
                else:
                    while True:
                        print('\n----- Menu Cliente -----')
                        print('1 - Comprar produto')
                        print('2 - Agendar serviço')
                        print('3 - Agendamentos')
                        print('4 - Historico de compras')
                        print('0 - Sair')
                        escolha = input('Digite sua opção: ')

                        if escolha == '1':
                            if not produtos:
                                print('Nenhum produto dísponivel no momento.')
                            else:
                                print('\nProdutos dísponiveis: ')
                                for indice in range(len(produtos)):
                                    print(f'Código {indice} | Produto {produtos[indice][0]} | Preço: R${produtos[indice][1]} | Em estoque: {produtos[indice][2]}')

                                indice = int(input('Digite o código do produto que deseja comprar: '))
                                if 0 <= indice < len(produtos):
                                    quantidade = float(input('Digite a quantidade desejada: '))
                                    if quantidade <= produtos[indice][2]:
                                        produtos[indice][2] -= quantidade
                                        total = quantidade * produtos[indice][1]
                                        print(f'Compra realizada! Produto: {produtos[indice][0]}, Quantidade: {quantidade}, Total: R${total:.2f}')
                                    else:
                                        print('Quantidade insuficiente em estoque.')
                                else:
                                    print('Código inválido.')

                        elif escolha == '2':
                            if not servicos:
                                print('Nenhum serviço disponível no momento.')
                            else:
                                print('\nServiços disponíveis: ')
                                for indice in range(len(servicos)):
                                    print(f'{indice} - Serviço: {servicos[indice][0]} | Preço: R${servicos[indice][1]}')

                                indice = int(input('Digite o código do serviço que deseja agendar: '))
                                if 0 <= indice < len(servicos):
                                    print(f'Agendamento realizado! Serviço: {servicos[indice][0]}, Preço: R${servicos[indice][1]}')
                                    agendapet.append([usuario, servicos[indice][0], servicos[indice][1]])
                                    compras.append([usuario, produtos[indice][0], quantidade, total])
                                else:
                                        print('Código inválido.')

                        elif escolha == '3':
                            print('Agendamentos do meu pet')
                            encontrado = False
                            for p in agendapet:
                                if p[0] == usuario:
                                    print(f'serviço: {p[1]} // preço: {p[2]}')
                                    encontrado = True
                            if not encontrado:
                                print('Nenhum agendamento disponivél')

                        elif escolha == '4':
                            print('Historico de compras: ')
                            for c in compras:
                                if c[0] == usuario:
                                     print(f'Produtos {c[1]} | quantidade {c[2]} | total {c[3]}')
                            else:
                                print('Nenhuma compra realizada, efetue a compra')

                        elif escolha == '0':
                            print('Saindo...')
                            break

                        else:
                            print('Opção inválida, tente novamente')
                break
            else:
                print('Usuário ou senha incorretos, tente novamente.')

    else:
        print('Opção inválida, tente novamente.')
        