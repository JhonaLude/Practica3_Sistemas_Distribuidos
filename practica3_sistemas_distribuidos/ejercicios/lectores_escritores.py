import threading
import time
from utils.logger import logger

mutex = threading.Lock()
recurso = threading.Semaphore(1)

lectores = 0
salida = []

def lector(i):
    global lectores

    with mutex:
        lectores += 1
        if lectores == 1:
            recurso.acquire()

    salida.append(f"Lector {i} leyendo")
    logger.info(f"Lector {i} leyendo")

    time.sleep(1)

    with mutex:
        lectores -= 1
        if lectores == 0:
            recurso.release()

def escritor():
    salida.append("Escritor esperando")
    logger.info("Escritor esperando")

    recurso.acquire()

    salida.append("Escritor escribiendo")
    logger.info("Escritor escribiendo")

    time.sleep(2)

    recurso.release()

def ejecutar_le():
    global salida, lectores
    salida = []
    lectores = 0

    hilos = []

    for i in range(1,4):
        hilos.append(threading.Thread(target=lector, args=(i,)))

    hilos.append(threading.Thread(target=escritor))

    for h in hilos:
        h.start()

    for h in hilos:
        h.join()

    return "\n".join(salida)