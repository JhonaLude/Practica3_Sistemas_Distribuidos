Proyecto desarrollado en Python + Flask + Bootstrap para demostrar mecanismos de sincronización y concurrencia mediante una aplicación web interactiva.


**Ejercicios implementados**


**1. Mutex (Exclusión Mutua)**


Simula múltiples hilos incrementando un contador compartido. Se utiliza un mutex para evitar condiciones de carrera y garantizar resultados correctos.



**2. Semáforo (Recursos Limitados)**


Representa un gimnasio con tres máquinas disponibles y varios atletas. El semáforo controla el acceso concurrente a recursos limitados.



**3. Productor-Consumidor**


Simula una panadería con buffer limitado. Se emplean dos semáforos (espacios_vacios, panes_listos) y un mutex para sincronizar producción y consumo.



**4. Lectores-Escritores**


Modela acceso concurrente a un tablón de notas. Varios lectores pueden acceder simultáneamente, mientras que la escritura es exclusiva.



**5. Barrera**


Varios hilos ejecutan una primera fase y esperan hasta que todos lleguen para continuar juntos a la segunda fase.



**Objetivo**


Comprender y aplicar técnicas de sincronización para coordinar hilos, proteger recursos compartidos y evitar errores de concurrencia.
