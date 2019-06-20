from collections import * 

class Thread(object):
    def __init__(self):
        pass
class AnalisadorSintatico (Thread):
         __ERR = -99
         __ACC = 99
         $ = 37
         
        int __PRODUCAO_TAMANHO[] = { 0,  0,  3,  2,  3,  2,  3,  1,  1,  1,  2,  3,  3,  1,  1,  1,  2,  4,  3,  1,  1,  1,  2,  2,  5,  3,  2,  2,  2,  2,  1};		
        int __PRODUCAO_CODIGO[] =  {-1, -1, 21, 22, 23, 23, 24, 25, 25, 25, 26, 27, 27, 28, 28, 28, 26, 29, 30, 30, 31, 31, 26, 32, 33, 35, 34, 34, 34, 34, 26};     35, 34, 34, 34, 34, 26};     
        def run():
            #class Stack(object):
            	def __init__(self):
		            self.pilha = []
                Token atual = nextToken()
                int estado
                self.pilha.push(0)
                while atual.getCodigo() != $ 
                    estado = self.pilha.push.peek()
                    if estado >= 0:
                        estado = ESTADOS[estado][atual.getCodigo()]
                        if estado >= 0:
                            if estado < 99:
                                self.pilha.push(atual.getCodigo())
                                self.pilha.push(estado)
                                
                                atual = nextToken()
                            else:
                                print("Aceito")
                                break
                        elif: estado > -99:
                            int prod = estado * -1
                            for int i in range (0,PRODUCAO_TAMANHO[PROD]*2,1)
                                self.pilha.pop()
                                int codigaNaoTerminal =PRODUCAO_TAMANHO[prod]
                                int procimoEstado = ESTADOS[self.pilha.peek()][codigaNaoTerminal]
                                self.pilha.push(codigaNaoTerminal)
                                self.pilha.push(proximoEstado)
                        else:
                            print("Erro na linha"+ atual.getLinha() + "e coluna" + atual,getColuna(),end='\n')
                            break
                Token nextToken():
                try:
                    pass fila.take()
                except InterruptedError as e:
                    
                    pass