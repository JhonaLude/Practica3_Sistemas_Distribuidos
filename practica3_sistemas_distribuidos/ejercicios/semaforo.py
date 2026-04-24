import threading
import time
from utils.logger import logger

sem = threading.Semaphore(3)
salida = []

def atleta(i):
    salida.append(f"Atleta {i} esperando")
    logger.info(f"Atleta {i} esperando")

    sem.acquire()

    salida.append(f"Atleta {i} usando máquina")
    logger.info(f"Atleta {i} usando máquina")

    time.sleep(1)

    salida.append(f"Atleta {i} libera máquina")
    logger.info(f"Atleta {i} libera máquina")

    sem.release()

def ejecutar_semaforo():
    global salida
    salida = []

    hilos = []

    for i in range(1,9):
        t = threading.Thread(target=atleta, args=(i,))
        hilos.append(t)
        t.start()

    for t in hilos:
        t.join()

    return "\n".join(salida)