from PIL import Image, ImageOps, ImageEnhance

def apply_grayscale(image: Image.Image) -> Image.Image:
    """Convierte una imagen a escala de grises"""
    return ImageOps.grayscale(image)

def apply_invert(image: Image.Image) -> Image.Image:
    """Invierte los colores de la imagen"""
    if image.mode != 'RGB':
        image = image.convert('RGB')
    return ImageOps.invert(image)

def apply_mirror(image: Image.Image) -> Image.Image:
    """Devuelve la imagen en espejo horizontal"""
    return ImageOps.mirror(image)

def apply_rotate(image: Image.Image, angle: int = 90) -> Image.Image:
    """Rota la imagen el ángulo especificado (por defecto 90°)"""
    return image.rotate(angle, expand=True)

def apply_brightness(image: Image.Image, factor: float = 1.2) -> Image.Image:
    """Ajusta el brillo de la imagen (1.0 = normal, >1 = más brillante)"""
    enhancer = ImageEnhance.Brightness(image)
    return enhancer.enhance(factor)
