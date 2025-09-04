import time
import sys

def barra_descargas_recursivas(progreso=0, total=100):
    # Caso base
    if progreso > total:
        print("\nDescarga completada")
        return

    barra = f"[{'#' * progreso}{'.' * (total - progreso)}] {progreso}%"
    sys.stdout.write('\r' + barra)
    sys.stdout.flush()
    time.sleep(0.1)

    barra_descargas_recursivas(progreso + 1, total)

if __name__ == "__main__":
    barra_descargas_recursivas()
