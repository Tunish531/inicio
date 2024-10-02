import random
caracteres="+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
longitud=int(input("Por favor ingresa la longitud de tu contraseña;"))
contrasenia=""
for i in range(longitud):
    contrasenia+=random.choice(caracteres)
print(f"esta es tu contraseña: {contrasenia}")    
