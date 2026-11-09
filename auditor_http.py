import requests 

def auditar_cabeceras():
    print("--- Auditor de Cabeceras de Seguridad HTTP ---")

    url = input("Ingresa la URL completar a auditar (ej. https://www.google.com ):")

    cabeceras_esperadas = [
        "Content-Security-Policy",
        "Strict-Transport-Security",
        "X-Content-Type-Options",
        "X-Frame-Options",
    ]

    try:
        respuesta = requests.get(url, timeout=5)
        cabeceras_sitio = respuesta.headers

        print(f"\nResultado para {url}:")
        print("-" * 40)

        for cabecera in cabeceras_esperadas:
            if cabecera in cabeceras_sitio:
                print(f"[SEGURO] La cabecera {cabecera} esta configurada.")
            else:
                print(f"[VULNERABLE] Falta la cabecera {cabecera}.")

    except requests.exceptions.RequestException as error:
        print(f"[ERROR] No se pudo conectar al sitio. Detalles: {error} ")

if __name__ == "__main__":
    auditar_cabeceras()