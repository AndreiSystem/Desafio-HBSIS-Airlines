#-- Importando as funções SmartFortwo
from SmartFortwo import *

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
