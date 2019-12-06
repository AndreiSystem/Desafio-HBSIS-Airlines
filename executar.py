#-- Importando as funções SmartFortwo
from SmartFortwo import *
#-- Arquivo OO
#from PooSmartFortwo import *

#-- Listando os passageiros no Terminal
terminal = ['piloto', 'oficial 1', 'oficial 2', 'chefe serviço', 'comissária 1', 'comissária 2', 'policial', 'presidiário']

#-- Listando os passageiros embarcados no Avião
aviao = []


#-- Ordem de embarque:
status(terminal)
viagem_para_aviao('piloto', 'oficial 2')
desembarque_aviao(terminal,aviao,'oficial 2')
viagem_para_terminal('piloto')
status(terminal)

viagem_para_aviao('chefe_serviço', 'comissária 1')
desembarque_aviao(terminal,aviao,'comissária 1')
viagem_para_terminal('chefe serviço')
status(terminal)

viagem_para_aviao('piloto','oficial 1')
desembarque_aviao(terminal,aviao,'oficial 1')
viagem_para_terminal('piloto')
status(terminal)

viagem_para_aviao('chefe serviço','comissária 2')
desembarque_aviao(terminal,aviao,'comissária 2')
viagem_para_terminal('chefe serviço')
status(terminal)

viagem_para_aviao('chefe serviço','piloto')
desembarque_aviao(terminal,aviao,'piloto')
viagem_para_terminal('chefe serviço')
status(terminal)

viagem_para_aviao('policial','presidiário')
desembarque_aviao(terminal,aviao,'policial','presidiário')
retorna_passageiro('piloto',aviao,terminal)
status(terminal)

viagem_para_aviao('piloto','chefe serviço')
desembarque_aviao(terminal,aviao,'piloto','chefe serviço')
status(terminal)


"""
---------------------------------------
|                                      |
|                                      |
|          TESTE PARA POO              |
|                                      |
---------------------------------------

viagem = Smart_Fortwo(terminal, aviao)

viagem.viagem_para_aviao('piloto','oficial 1')
viagem.desembarque_aviao('oficial 1')
viagem.viagem_para_terminal('piloto')
viagem.get_status()

viagem.viagem_para_aviao('chefe de serviço', 'comissária 1')
viagem.desembarque_aviao('comissária 1')
viagem.viagem_para_terminal('chefe de serviço')
viagem.get_status()

viagem.viagem_para_aviao('piloto', 'oficial 2')
viagem.desembarque_aviao('oficial 2')
viagem.viagem_para_terminal('piloto')
viagem.get_status()

viagem.viagem_para_aviao('chefe de serviço','comissária 2')
viagem.desembarque_aviao('comissária 2')
viagem.viagem_para_terminal('chefe de serviço')
viagem.get_status()

viagem.viagem_para_aviao('piloto','chefe de serviço')
viagem.desembarque_aviao('chefe de serviço')
viagem.viagem_para_terminal('piloto')
viagem.get_status()

viagem.viagem_para_aviao('policial','presidiário')
viagem.desembarque_aviao('policial','presidiário')
viagem.retirar_passageiro('chefe de serviço')
viagem.viagem_para_aviao('piloto','chefe de serviço')
viagem.desembarque_aviao('piloto','chefe de serviço')
viagem.get_status()
"""