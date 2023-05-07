#Drooxingj 
#(Dr3amyB3rry)

import os
import zipfile
import time

def compress_roms():
    roms = [f for f in os.listdir('.') if f.endswith('.n64') or f.endswith('.z64')]

    # Crear las carpetas si no existen
    if not os.path.exists('comprimidos'):
        os.makedirs('comprimidos')
    if not os.path.exists('vanilla'):
        os.makedirs('vanilla')

    for rom in roms:
        print(f"Comprimiendo {rom}...")
        start_time = time.time()

        # Definir el nombre del archivo ZIP y la ruta de destino
        zip_name = os.path.splitext(rom)[0] + '.zip'
        zip_path = os.path.join('comprimidos', zip_name)

        # Crear el archivo ZIP y agregar el archivo ROM
        with zipfile.ZipFile(zip_path, mode='w', compression=zipfile.ZIP_LZMA) as zip_file:
            zip_file.write(rom)

        # Mover el archivo ROM a la carpeta 'vanilla'
        os.rename(rom, os.path.join('vanilla', rom))

        # Imprimir el tiempo de compresión y el tamaño del archivo resultante
        elapsed_time = time.time() - start_time
        zip_size = os.path.getsize(zip_path) / (1024 * 1024)
        print(f"{rom} comprimido en {elapsed_time:.2f} segundos. Tamaño: {zip_size:.2f} MB")

    # Preguntar si se desean borrar los archivos ROM originales
    while True:
        respuesta = input("¿Desea borrar los archivos ROM originales? (y/n): ")
        if respuesta.lower() == 'y':
            for rom in roms:
                os.remove(os.path.join('vanilla', rom))
            break
        elif respuesta.lower() == 'n':
            break
        else:
            print("Respuesta inválida. Intente de nuevo.")

compress_roms()
