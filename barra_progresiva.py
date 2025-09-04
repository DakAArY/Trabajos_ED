import time
import sys

def barra_descargas():
    total = 100
    for i in range(total + 1):
        barra = f"[{'#' * i}{'.' * (total - i)}] {i}%"
        sys.stdout.write('\r' + barra)
        sys.stdout.flush()
        time.sleep(0.1)

    print("\nDescarga completada")


if __name__ == "__main__":
    barra_descargas()
