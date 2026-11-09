
import pyotp
import qrcode

def sistema_2fa():
    print("--- Autenticación de Dos Factores (2FA) ---")

    # 1. Generar la clave secreta
    clave_secreta = pyotp.random_base32()
    print(f"Clave secreta generada: {clave_secreta}")

    # 2. Configurar la URL para la aplicacion de aunteticacion
    uri = pyotp.TOTP(clave_secreta).provisioning_uri(
        name="admin@proyecto.local",
        issuer_name="Sistema de Seguridad Web"
    )

    # 3. Generar el codigo QR
    img = qrcode.make(uri)
    img.save("codigo_qr_2fa.png")
    print("Se ha generado 'codigo_qr_2fa.png'. Abrelo y escanealo con Google Authenticator o Authy.")

    # 4. Validar el token ingresado por el usuario 
    totp = pyotp.TOTP(clave_secreta)
    token_usuario = input("\nIngresa el codigo de 6 digitos de tu aplicacion: ")

    if totp.verify(token_usuario):
        print("[EXITO] Acceso concedido. Token válido.")
    else:
        print("[ERROR] Acceso denegado. Token invalido o expirado.")

if __name__ == "__main__":
    sistema_2fa()