# Faça um programa que utilize dicionários para gerenciar uma agenda de telefones.
# • A agenda deve guardar nome e telefone de várias pessoas.
# • Operações da aplicação: inclusão, exclusão, alteração, pesquisa e listagem.
# • Em todos as opções o nome da pessoa será utilizado como chave de pesquisa.
# • Fazer uso de menu.
# • Criar biblioteca de funções das operações.

from funcoesOperacoes import *
from time import sleep

menu = 0
agenda = list()
while True:
    print(f'{"Agenda telefônica":^50}')
    cabecalho('menu')
    print('[1 - incluir]\n[2 - excluir]\n[3 - alterar]\n[4 - pesquisar]\n[5 - listar]\n[0 - Sair]')
    while True:
        try:
            menu = int(input('Insira a opção: '))
            break
        except ValueError:
            print("O menu só aceita números")
    match (menu):
        case 0:
            break
        case 1:
            inclusao(agenda)
        case 2:
            exclusao(agenda)
        case 3:
            alteracao(agenda)
        case 4:
            pesquisa(agenda)
        case 5:
            listar(agenda)
        case _:
            print('Opção inválida!')
    sleep(1.5)
