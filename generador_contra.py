import string
import random

# Solicitar la longitud de la contraseña al usuario
try:
    longitud = int(input("Tamaño de la contraseña: "))
    if longitud <= 0:
        raise ValueError("El tamaño debe ser un número positivo.")
except ValueError as e:
    print(f"Entrada inválida: {e}")
    exit()

# Definir los caracteres permitidos
caracteres = string.ascii_letters + string.digits + string.punctuation

# Generar la contraseña
contrasena = ''.join(random.choices(caracteres, k=longitud))

print("La contraseña es: " + contrasena)
