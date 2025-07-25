import sys
from PIL import Image

if len(sys.argv) != 4:
    print("Uso: python image_rotator.py <imagen_entrada> <imagen_salida> <grados>")
    sys.exit(1)

input_path = sys.argv[1]
output_path = sys.argv[2]
angle = int(sys.argv[3])

try:
    with Image.open(input_path) as im:
        print(im.size)  # Imprime el tamaño original
        rotated = im.rotate(angle, expand=True)  # expand=True para ajustar el tamaño
        rotated.save(output_path)
        print(rotated.size)  # Imprime el tamaño de la imagen rotada
except Exception as e:
    print(f"Ocurrió un error: {e}")
