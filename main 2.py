import numpy as np
import math
import matplotlib.pyplot as plt
class Perceptron:
    def __init__(self,pesos,entradas,salidas):
        self.pesos=pesos
        self.entradas=entradas
        self.salidas=salidas
        self.lr=0.1

    def balance(self):
        salidas=self.obtener_salidas()
        print(salidas)

    def obtener_salidas(self):
        iteraciones=0
        i=0
        fallos=4
        while True:
            errores=[]
            for entrada in self.entradas:
                
                deltas_peso=[]
                producto_escalar=np.dot(entrada,self.pesos)
                salida_obtenida=self.sigmoidea(producto_escalar)
                error=self.salidas[i]-salida_obtenida
                delta=salida_obtenida*(1-salida_obtenida)*error
                errores.append(error)
                for value in entrada:
                    delta_peso=self.lr*value*delta
                    deltas_peso.append(delta_peso)
                    
                self.pesos+=deltas_peso
                if abs(error)<=0.15:
                    fallos=fallos-1
                    if fallos==0:
                        print(self.pesos)
                        print("cantidad de iteraciones: ", iteraciones)
                        break
                else:
                    fallos=4  
                iteraciones+=1
        # print("nuevos pesos")
        # print(self.pesos)

                                              
    def sigmoidea(self,salida_obtenida):
        sig = 1/(1 + math.exp(-salida_obtenida))
        return sig

np_matrix_pesos=np.array([0.9,0.66,-0.2])
np_matrix_entradas=np.array([[1,0,1],[1,1,1],[0,1,0],[0,1,1]])
np_matrix_salidas=np.array([0,1,0,0])
and_perceptor=Perceptron(np_matrix_pesos,np_matrix_entradas,np_matrix_salidas)
if __name__=="__main__":
    
    print(and_perceptor.balance())
    
    # contador=0
    # pesos=[]
    # peso1=[]
    # peso2=[]
    # peso3=[]
    # while contador<100:
    #     print(and_perceptor.balanceo_peso())
    #     # pesos_balanceados=and_perceptor.balanceo_peso()
    #     # pesos.append(pesos_balanceados)
    #     contador+=1
        
        
    # for peso in pesos:
    #     for j in peso:
    #         count=0
    #         for k in j:
    #             if count==0:
    #                 peso1.append(k)
    #             if count==1:
    #                 peso2.append(k)
    #             if count==2:
    #                 peso3.append(k)
    #             count+=1 
    # print(peso1)
    # print(peso2) 
    # plt.plot(peso1,'g')
    # plt.plot(peso2,'r')
    # plt.plot(peso3,'k')
    # plt.show()