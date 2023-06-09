def cabecalho(txt):
    print("-" * 50)
    print(f"{txt:^50}")
    print("-" * 50)


def inclusao(agenda):
    pessoa = {'Nome': str(input('Insira o nome: ')), 'Telefone': int(input('Insira o número de telefone: '))}
    agenda.append(pessoa)
    return agenda


def exclusao(agenda):
    if len(agenda) == 0:
        print('Nenhum contato cadastrado!')
    else:
        nome = str(input('Insira o nome da pessoa a ser excluida: '))
        for i in range(0, len(agenda)):
            if agenda[i]['Nome'] == nome and i == 0:
                del agenda[i]
                break
            elif agenda[i]['Nome'] == nome:
                del agenda[i]
                break
            elif nome not in agenda and i + 1 == len(agenda):
                print("Não foi possivel encontrar essa pessoa.")

    return agenda


def alteracao(agenda):
    if len(agenda) == 0:
        print('Nenhum contato cadastrado!')
    else:
        nome = str(input('Insira o nome da pessoa a ser alterada: '))
        for i in range(0, len(agenda)):
            if agenda[i]['Nome'] == nome:
                while True:
                    opc = int(input('Deseja alterar o nome e/ou o número? \n[1-Nome]\t[2-Número]\t[3 - Tudo]: '))
                    if opc == 1:
                        agenda[i]['Nome'] = str(input('Insira o novo nome: '))
                        break
                    elif opc == 2:
                        agenda[i]['Telefone'] = int(input('Insira o novo número: '))
                        break
                    elif opc == 3:
                        agenda[i]['Nome'] = str(input('Insira o novo nome: '))
                        agenda[i]['Telefone'] = int(input('Insira o novo número: '))
                        break
                    else:
                        print('Opção invalida!')
                break
            elif nome not in agenda and i + 1 == len(agenda):
                print("Não foi possivel encontrar essa pessoa.")
    return agenda


def pesquisa(agenda):
    if len(agenda) == 0:
        print('Nenhum contato cadastrado!')
    else:
        nome = str(input('Insira o nome da pessoa a ser pesquisada: '))
        for i in range(0, len(agenda)):
            if agenda[i]['Nome'] == nome:
                print(f'{agenda[i]}')
            elif nome not in agenda and i + 1 == len(agenda):
                print("Não foi possivel encontrar essa pessoa.")
    return agenda


def listar(agenda):
    if len(agenda) == 0:
        print('Nenhum contato cadastrado!')
    else:
        for i in range(0, len(agenda)):
            print(agenda[i])
