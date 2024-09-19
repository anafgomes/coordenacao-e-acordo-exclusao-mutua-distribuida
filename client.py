import rpyc
import time
import random
import sys

class Cliente:
    def __init__(self, numero):
        self.numero = numero
        self.conn = rpyc.connect("localhost", 18861)
    
    def solicitar_servico(self):
        for i in range(20):
            print(f"O cliente {self.numero} está solicitando um corte de cabelo.")
            self.conn.root.cortarCabelo(self.numero)
            
            time.sleep(random.uniform(0.5, 1.5))  
            
            print(f"O cliente {self.numero} está solicitando um corte de barba.")
            self.conn.root.cortarBarba(self.numero)
            
            time.sleep(random.uniform(0.5, 1.5)) 
            
            print(f"O cliente {self.numero} está solicitando um corte de bigode.")
            self.conn.root.cortarBigode(self.numero)
            
            time.sleep(random.uniform(0.5, 1.5))

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Uso: python client.py <numero_cliente>")
        sys.exit(1)
    
    cliente_numero = int(sys.argv[1])
    cliente = Cliente(cliente_numero)
    cliente.solicitar_servico()