import numpy as np
import math
import matplotlib.pyplot as plt
class Perceptron:
    def __init__(self,pesos,entradas,salidas):
        self.pesos=pesos
        self.entradas=entradas
        self.salidas=salidas
        self.lr=0.12
        self.tolerancia=4
        self.actualizaciones=0
    def actualizar(self):
            i=0
            # vectores que contienen el cambio de los pesos
            a=[self.pesos[0]]
            b=[self.pesos[1]]
            c=[self.pesos[2]]
            while i in range(len(self.entradas)):        
                prod_escalar=np.dot(self.pesos,self.entradas[i])
                salida_obtenida=self.sigmoidea(prod_escalar)
                error=self.salidas[i]-salida_obtenida
                if error<0.01:
                    self.tolerancia-=1
                    i+=1
                    if self.tolerancia==0:
                            plt.plot(a,'g')
                            plt.plot(b,'r')
                            plt.plot(c,'k')
                            plt.show()
                            print("Pesos finales: ",self.pesos)
                else:
                    delta_chico=salida_obtenida*(1-salida_obtenida)*error
                    for j in range(len(self.entradas[i])):
                        self.pesos[j]=self.pesos[j]+(self.lr*delta_chico*self.entradas[i][j])
                    # print("Peso actualizado: ",self.pesos)
                    self.actualizaciones+=1
                    self.tolerancia=4
                    i=0
                    for count in range(len(self.pesos)):
                        if count==0:
                            a.append(self.pesos[count])
                        if count==1:
                            b.append(self.pesos[count])
                        if count==2:
                            c.append(self.pesos[count])
                    
                    
    def sigmoidea(self,prod_escalar):
        sig = 1 / (1 + math.exp(-prod_escalar))
        return sig
        
np_matrix_pesos=np.array([0.9473185,-0.97817776,0.260055]) 
np_matrix_entradas=np.array([[1,1,1],[1,1,0],[1,0,1],[1,0,0]]) 
np_matrix_salidas=np.array([1,0,0,0]) 
and_perceptor=Perceptron(np_matrix_pesos,np_matrix_entradas,np_matrix_salidas)
if __name__=="__main__":
    and_perceptor.actualizar()