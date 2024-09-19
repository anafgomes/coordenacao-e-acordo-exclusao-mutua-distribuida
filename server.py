import rpyc
from rpyc.utils.server import ThreadedServer
import time
import threading

class BarbeiroService(rpyc.Service):
    def on_connect(self, conn):
        pass
    
    def on_disconnect(self, conn):
        pass

    def __init__(self):
        self.lock = threading.Lock()

    def exposed_cortarCabelo(self, cliente_num):
        with self.lock:
            print(f"Barbeiro: Cliente [{cliente_num}] iniciando corte de cabelo.")
            time.sleep(3)
            print(f"Barbeiro: Cliente [{cliente_num}] corte de cabelo concluído!")

    def exposed_cortarBarba(self, cliente_num):
        with self.lock:
            print(f"Barbeiro: Cliente [{cliente_num}] iniciando corte de barba.")
            time.sleep(4)
            print(f"Barbeiro: Cliente [{cliente_num}] corte de barba concluído!")

    def exposed_cortarBigode(self, cliente_num):
        with self.lock:
            print(f"Barbeiro: Cliente [{cliente_num}] iniciando corte de bigode.")
            time.sleep(5)
            print(f"Barbeiro: Cliente [{cliente_num}] corte de bigode concluído!")

if __name__ == "__main__":
    server = ThreadedServer(BarbeiroService(), port=18861)
    print("A barbearia está aberta!")
    server.start()