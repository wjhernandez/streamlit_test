from PIL import Image

# Abre la imagen PNG
img = Image.open("tripleten_logo.jpeg.png")

# Convierte y guarda como JPEG
rgb_img = img.convert('RGB')  # JPEG no admite transparencia
rgb_img.save("tripleten_logo.jpeg", format="JPEG")
