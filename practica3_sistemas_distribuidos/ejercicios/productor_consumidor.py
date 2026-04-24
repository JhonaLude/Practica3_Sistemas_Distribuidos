import threading
import time
from utils.logger import logger

buffer = []
salida = []

espacios_vacios = threading.Semaphore(10)
panes_listos = threading.Semaphore(0)
mutex = threading.Lock()

def productor():
    for i in range(20):
        pan = f"Pan {i+1}"

        espacios_vacios.acquire()

        with mutex:
            buffer.append(pan)
            salida.append(f"Produce {pan} -> {buffer}")
            logger.info(f"Produce {pan}")

        panes_listos.release()
        time.sleep(0.5)

def consumidor():
    for _ in range(20):
        panes_listos.acquire()

        with mutex:
            pan = buffer.pop(0)
            salida.append(f"Consume {pan} -> {buffer}")
            logger.info(f"Consume {pan}")

        espacios_vacios.release()
        time.sleep(1)

def ejecutar_pc():
    global salida, buffer
    salida = []
    buffer = []

    t1 = threading.Thread(target=productor)
    t2 = threading.Thread(target=consumidor)

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    return "\n".join(salida)