import threading
import time
from utils.logger import logger

salida = []
barrier = threading.Barrier(5)

def hilo(i):
    salida.append(f"Hilo {i} Fase 1")
    logger.info(f"Hilo {i} Fase 1")

    time.sleep(1)

    barrier.wait()

    salida.append(f"Hilo {i} Fase 2")
    logger.info(f"Hilo {i} Fase 2")

def ejecutar_barrera():
    global salida, barrier
    salida = []
    barrier = threading.Barrier(5)

    hilos = []

    for i in range(1,6):
        t = threading.Thread(target=hilo, args=(i,))
        hilos.append(t)
        t.start()

    for t in hilos:
        t.join()

    return "\n".join(salida)