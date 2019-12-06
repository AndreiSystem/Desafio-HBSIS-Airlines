
#--- Funções de Embarque Smart Fortwo ---

#-- Função de mostrar os Passageiros que faltam Embarcar
def status(lista:list):
    print('---Status---')
    if len(lista) > 0:
        for passageiros in lista:
            print(f'\033[1;31m{passageiros}\033[m')
    else:
        print('\033[1;32mTodos embarcados!\033[m')

#-- Função que retorna o Motorista e o Passageiro embarcados no Smart Fortwo
def viagem_para_aviao(motorista, passageiro):
    print('\033[1;33mEmbarcando para Avião!\033[m')
    print(f'Motorista: \033[1;32m{motorista}\033[m\n'
          f'Passageiro: \033[1;32m{passageiro}\033[m')
    for i in range(1,4):
        print(f'{i}km...')
    print('Pronto para desembarcar passageiro!')

#-- Função de desembarque, remove os Passageiros do Terminal e insere no Avião (passageiro 2 opcional)
#-- Retorna Embarcadas e as que faltam embarcar
def desembarque_aviao(lista_1:list,lista_2:list,passageiro1,passageiro2=None):
    if passageiro2 is None:
        lista_1.remove(passageiro1)
        lista_2.append(passageiro1)
    else:
        lista_1.remove(passageiro1)
        lista_1.remove(passageiro2)
        lista_2.append(passageiro1)
        lista_2.append(passageiro2)

    print('-'*20)
    print('---Pessoas que falta embarcar no Avião!---')
    if len(lista_1) > 0:
        for pessoas in lista_1:
            print(f'\033[1;31m{pessoas}\033[m')
    else:
        print('\033[1;32mTodos Embarcados!\033[m')
    print('---Passageiros no Avião---')
    for passageiros in lista_2:
        print(f'\033[1;32m{passageiros}\033[m')

#-- Função de retorno para o Terminal
def viagem_para_terminal(motorista, passageiro=None):
    print(f'Voltando para terminal: \033[1;32m\n{motorista}\033[m')
    if passageiro is None:
        print('')
    else:
        print(passageiro)

#-- Função para retirar um passageiro do avião caso seja necessário
def retorna_passageiro(motorista, lista_1:list, lista_2:list):
    if motorista in lista_1:
        print(f'Voltando para terminal: \n{motorista}')
        lista_1.remove(motorista)
        lista_2.append(motorista)

    else:
        print('\033[1;31mEsse passageiro não se encontra!\033[m')





