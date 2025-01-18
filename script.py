import requests
import time
import os
from dotenv import load_dotenv

# Cargar variables del archivo .env
load_dotenv()

WEBHOOK_URL = os.getenv("DISCORD_WEBHOOK_URL")

def obtener_ip_publica():
    try:
        respuesta = requests.get("https://api.ipify.org?format=json")
        respuesta.raise_for_status()
        datos = respuesta.json()
        return datos["ip"]
    except requests.RequestException as e:
        print(f"Error al obtener la IP pública: {e}")
        return None

def enviar_ip_a_discord(webhook_url, ip):
    if not webhook_url:
        print("URL del webhook no proporcionada.")
        return

    mensaje = {
        "content": f"Mi dirección IP pública ha cambiado: {ip}"
    }

    try:
        respuesta = requests.post(webhook_url, json=mensaje)
        respuesta.raise_for_status()
        print("Nueva IP enviada exitosamente a Discord.")
    except requests.RequestException as e:
        print(f"Error al enviar la IP a Discord: {e}")

def monitorear_ip(webhook_url, intervalo=60):
    ip_actual = None

    while True:
        nueva_ip = obtener_ip_publica()
        if nueva_ip and nueva_ip != ip_actual:
            print(f"IP cambiada: {nueva_ip}")
            enviar_ip_a_discord(webhook_url, nueva_ip)
            ip_actual = nueva_ip
        else:
            print("IP sin cambios.")

        time.sleep(intervalo)  # Espera antes de la próxima verificación

if __name__ == "__main__":
    if not WEBHOOK_URL:
        print("Error: DISCORD_WEBHOOK_URL no está configurado en el archivo .env.")
    else:
        monitorear_ip(WEBHOOK_URL, intervalo=300)
