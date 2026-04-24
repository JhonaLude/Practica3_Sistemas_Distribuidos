import threading
from utils.logger import logger

contador = 0
lock = threading.Lock()

def tarea():
    global contador
    for _ in range(100000):
        with lock:
            contador += 1

def ejecutar_mutex():
    global contador
    contador = 0

    hilos = []

    for _ in range(5):
        t = threading.Thread(target=tarea)
        hilos.append(t)
        t.start()

    for t in hilos:
        t.join()

    logger.info(f"Mutex terminado: {contador}")

    return f"Ventas Totales: {contador}"