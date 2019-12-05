#-- função smart fortwo movendo


def situacao():
    print('--------TERMINAL---------')
    terminal = [
        'piloto','oficial 1','oficial 2','chefe_serviço','comissária 1','comissária 2','policial','presidiário'
    ]

    aviao = []

    for i in terminal:
        print(i)
    return terminal


def viagem_terminal_aviao(piloto, passageiro=None):
    situacao()
    
    print(f'--------Embarcando Smart Fortwo-------- \nmotorista: {piloto}, passageiro: {passageiro}')
    print('indo até o avião')
    for i in range(1,6):
        print(f'{i}km')
    print('chegada ao avião')

    situacao().remove(passageiro)





viagem_terminal_aviao('piloto', 'oficial 1')



#smart_fortwo()

#status(pessoas)

#remove(pessoas)