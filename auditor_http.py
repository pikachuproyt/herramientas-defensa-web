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