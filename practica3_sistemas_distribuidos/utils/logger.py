import logging
import os

os.makedirs("logs", exist_ok=True)

logger = logging.getLogger("practica")
logger.setLevel(logging.INFO)

if not logger.handlers:
    archivo = logging.FileHandler("logs/practica.log")
    formato = logging.Formatter("%(asctime)s - %(message)s")
    archivo.setFormatter(formato)
    logger.addHandler(archivo)