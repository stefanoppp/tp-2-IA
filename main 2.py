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
        # plt.plot(self.pesos,'r')
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
        return self.pesos
        # print(errores)
        

        
    def sigmoidea(self,salida_obtenida):
        sig = 1/(1 + math.exp(-salida_obtenida))
        return sig

np_matrix_pesos=np.array([[0.9,0.66,-0.2],[0.9,0.66,-0.2],[0.9,0.66,-0.2],[0.9,0.66,-0.2]])
np_matrix_entradas=np.array([[1,0,1],[1,1,1],[0,1,0],[0,1,1]])
np_matrix_salidas=np.array([0,1,0,0])
and_perceptor=Perceptron(np_matrix_pesos,np_matrix_entradas,np_matrix_salidas)
if __name__=="__main__":
    contador=0
    pesos=[]
    peso1=[]
    peso2=[]
    peso3=[]
    while contador<500:
        pesos_balanceados=and_perceptor.balanceo_peso()
        pesos.append(pesos_balanceados)
        contador+=1
        
    for peso in pesos:
        for j in peso:
            count=0
            for k in j:
                if count==0:
                    peso1.append(k)
                if count==1:
                    peso2.append(k)
                if count==2:
                    peso3.append(k)
                count+=1 
    # print(peso1)
    # print(peso2) 
    plt.plot(peso1,'g')
    plt.plot(peso2,'r')
    plt.plot(peso3,'k')
    plt.show()