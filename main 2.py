import numpy as np
import math
import matplotlib.pyplot as plt
class Perceptron:
    def __init__(self,pesos,entradas,salidas):
        self.pesos=pesos
        self.entradas=entradas
        self.salidas=salidas
        self.lr=0.1

    def balanceo_peso(self):
        salidas_obtenidas=[]
        deltas=[]
            # suma ponderada inicial
        for i in range(len(self.entradas)):
            prod_escalar=np.dot(self.pesos[i],self.entradas[i])  
            salida_obtenida=self.sigmoidea(prod_escalar)
            salidas_obtenidas.append(salida_obtenida)
            
        errores=self.salidas-salidas_obtenidas
            
            # calculamos deltas
        for i in range(len(errores)):
            delta=salidas_obtenidas[i]*(1-salidas_obtenidas[i])*errores[i]
            deltas.append(delta)      
            variaciones=[]
            
        # recorremos los valores de las entradas y obtenemos su variacion
        
        for delta,entrada in zip(deltas,self.entradas):
            variacion_peso=self.lr*delta*entrada
            variaciones.append(variacion_peso)
        
        self.pesos=self.pesos+variaciones
        # print(errores)
        print(self.pesos)
        # xpoints = np.array([0, 6])
        # ypoints = np.array([0, 250])
        # plt.plot(xpoints, ypoints)
        # plt.show()
        
    def sigmoidea(self,salida_obtenida):
        sig = 1/(1 + math.exp(-salida_obtenida))
        return sig

np_matrix_pesos=np.array([[0.9,0.66,-0.2],[0.9,0.66,-0.2],[0.9,0.66,-0.2],[0.9,0.66,-0.2]])
np_matrix_entradas=np.array([[1,0,1],[1,1,1],[0,1,0],[0,1,1]])
np_matrix_salidas=np.array([0,1,0,0])
and_perceptor=Perceptron(np_matrix_pesos,np_matrix_entradas,np_matrix_salidas)
if __name__=="__main__":
    contador=0
    while contador<5:
        print(and_perceptor.balanceo_peso())
        contador+=1
        