![PYTHON](https://img.shields.io/badge/Python-FFD43B?style=for-the-badge&logo=python&logoColor=blue)

# IP Monitor con Webhook de Discord

Este proyecto monitorea tu dirección IP pública y envía un mensaje a un canal de Discord usando un webhook cada vez que detecta un cambio en la IP.


## Requisitos

- Docker instalado en tu máquina.
- Una URL de webhook de Discord configurada. Para obtenerla:
  1. Ve a la configuración de un canal de tu servidor de Discord.
  2. Crea un webhook y copia la URL.

## Configuración

1. Clona este repositorio:
   ```bash
   git clone https://github.com/tu-usuario/ip-monitor.git
   cd ip-monitor
   ```

2. Crea un archivo `.env` en la raíz del proyecto con el siguiente contenido:

   ```bash
   cp  example.env .env
   ```

   ```plaintext
   DISCORD_WEBHOOK_URL=https://discord.com/api/webhooks/TU_WEBHOOK_ID/TU_WEBHOOK_TOKEN
   ```

3. Asegúrate de que Docker esté instalado y funcionando en tu sistema.

## Uso

### Construir y ejecutar el contenedor

1. Construye la imagen de Docker:
   ```bash
   docker build -t ip-monitor .
   ```

2. Ejecuta el contenedor:
   ```bash
   docker run --env-file .env ip-monitor
   ```

El script monitoreará tu IP pública y enviará un mensaje al webhook de Discord si detecta un cambio.

### Salida esperada

Si la IP cambia, recibirás un mensaje en Discord como este:

```
Mi dirección IP pública ha cambiado: 123.123.123.123
```