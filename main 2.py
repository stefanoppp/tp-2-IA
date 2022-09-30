import numpy as np
import math
import matplotlib.pyplot as plt
class Perceptron:
    def __init__(self,pesos,entradas,salidas):
        self.pesos=pesos
        self.entradas=entradas
        self.salidas=salidas
        self.lr=0.4
        self.tolerancia=4
        self.actualizaciones=0
    
    def actualizar(self):
            i=0
            while i in range(len(self.entradas)):        
                prod_escalar=np.dot(self.pesos,self.entradas[i])
                salida_obtenida=self.sigmoidea(prod_escalar)
                error=self.salidas[i]-salida_obtenida
                if abs(error)<0.01:
                    self.tolerancia-=1
                    i+=1
                    if self.tolerancia==0:
                        print("Nuevos pesos: ",self.pesos)
                        print("Actualizaciones: ",self.actualizaciones)
        
                else:
                    for j in range(len(self.entradas[i])):
                        self.pesos[j]=self.pesos[j]+(self.lr*error*self.entradas[i][j])
                    self.actualizaciones+=1
                    self.tolerancia=4
                    i=0
                    
    def sigmoidea(self,prod_escalar):
        sig = 1 / (1 + math.exp(-prod_escalar))
        return sig
        
np_matrix_pesos=np.array([0.6473185,0.37817776,0.33160055]) 
np_matrix_entradas=np.array([[1,1,1],[1,1,0],[1,0,1],[1,0,0]]) 
np_matrix_salidas=np.array([1,0,0,0]) 
and_perceptor=Perceptron(np_matrix_pesos,np_matrix_entradas,np_matrix_salidas)
if __name__=="__main__":
    and_perceptor.actualizar()