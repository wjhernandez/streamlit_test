from PIL import Image
import argparse

# Crear parser
parser = argparse.ArgumentParser()

# Argumentos principales
parser.add_argument('input_file', help='Ruta del archivo de entrada')
parser.add_argument('output_file', help='Ruta del archivo de salida')

# Opciones para ancho y alto
parser.add_argument('--width', type=int, help='Ancho deseado')
parser.add_argument('--height', type=int, help='Alto deseado')

# Flag opcional para mostrar info
parser.add_argument('-i', '--info', action='store_true', help='Mostrar dimensiones originales')

# Parsear argumentos
args = parser.parse_args()

# Abrir imagen
im = Image.open(args.input_file)

# Mostrar dimensiones si se activa el flag -i
if args.info:
    print('Dimensiones originales:', im.size)

# Cambiar tamaño si se indican width y height
if args.width and args.height:
    resized = im.resize((args.width, args.height))
else:
    resized = im

# Guardar imagen redimensionada
resized.save(args.output_file)
