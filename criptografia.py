from cryptography.fernet import Fernet

def criptografia_aes():
    print("--- Herramienta de Criptografia Bidireccional (AES)---")

    # 1. Generar la llave maestra 
    llave = Fernet.generate_key()
    f = Fernte(llave)
    print(f"Lllave maestrra generada (mantener en secreto): {llave.decode()}")

    # 2. Datos a proteger 
    datos_sensibles = "Contrseña de la base de datos de produccion: root123"
    print(f"\nTexto original: {datos_sensibles}")

    # 3. cifrar los datos 
    datos_cifrados = f.encrypt(datos_sensibles.encode())
    print(f"Texto cifrado: (lo que veria un atacante): {datos_cifrados.decode()}")

    # 4. Descifrar los datos
    datos_descifrados = f.decrypt(datos_cifrados).decode()
    print(f"Texto descrifrado con la llave maestra: {datos_descifrados}")

if __name__ == "__main__":
    criptografia_aes()