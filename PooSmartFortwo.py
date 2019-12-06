class Smart_Fortwo:
    def __init__(self, terminal:list, aviao:list):
        self.terminal = terminal
        self.aviao = aviao
        print('|-----STATUS-----|')
        for pessoas in self.terminal:
            print(pessoas)
        print('-----------------')

    def get_status(self):
        
        if len(self.terminal) > 0:
            print('|-----STATUS-----|')
            for pessoas in self.terminal:
                print(' '*2, pessoas)
        else:
            print('|----------STATUS------------|')
            print('Todos passageiros embarcados!')

    def viagem_para_aviao(self, motorista, passageiro):
        if motorista == 'policial' or motorista == 'chefe de serviço' or motorista == 'piloto':
            if motorista and passageiro in self.terminal:
                print('Embarcando para Avião')
                print(f'Motorista: {motorista}')
                print(f'Passageiro(a): {passageiro}')

                for i in range(1,4):
                    print(f'{i}km..')
                print('Pronto para desembarcar passageiro!!')
            else:
                print(f'{passageiro} não está presente!')
        else:
            print('Apenas Policial, Chefe de Serviço ou Piloto podem pilotar!')

    def desembarque_aviao(self, passageiro_1, passageiro_2=None):
        if passageiro_2 is None:
            self.terminal.remove(passageiro_1)
            self.aviao.append(passageiro_1)
        else:
            self.terminal.remove(passageiro_1)
            self.terminal.remove(passageiro_2)
            self.aviao.append(passageiro_1)
            self.aviao.append(passageiro_2)

        print('---- Passageiros no Avião ---- ')
        for i in self.aviao:
            print(i)


    def viagem_para_terminal(self, motorista, passageiro=None):
        print(f'Voltando para o Terminal: \n{motorista}')

        if passageiro is None:
            pass
        else:
            if passageiro in self.aviao:
                self.aviao.remove(passageiro)
                self.terminal.append(passageiro)
                print(passageiro)
    
    def retirar_passageiro(self,passageiro):
        print(f'Voltando para o Terminal: \n{passageiro}')
        self.aviao.remove(passageiro)
        self.terminal.append(passageiro)













