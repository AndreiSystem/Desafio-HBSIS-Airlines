# Desafio-HBSIS-Airlines
link http://dontpad.com/aula4-ex1

1-piloto
2-oficiais       x
3-oficiais	 x
--------------
4-chefe de serv  x
5-comissarias
6-comissarias
--------------
7-policial
8-presidiário

tripulação tecnica = ['piloto', 'oficiais'x, 'oficiais' x]

tripulação de cabine = ['chefe_serviço', 'comissárias'x, 'comissárias'x]

terminal = ['policial', 'presidiário']

smart_fortwo (2 pessoas)

terminal de embarque = ['piloto', 'oficiais', 'oficiais','chefe_serviço', 
			'comissárias', 'comissárias', 'policial', 'presidiário']


leva:
piloto -> oficial
piloto <-
chefe_serviço -> comissária
chefe_serviço <-
piloto -> oficial
piloto <-
chefe_serviço -> comissária
chefe_serviço <-
chefe_serviço -> piloto
chefe_serviço <-
policial -> presidiário
piloto <-
piloto -> chefe_serviço


