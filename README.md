# Telegram Bot IA

Este es un bot de Telegram con funcionalidades de inteligencia artificial para moderar y analizar conversaciones en grupos.

## Funcionalidades

- **Captura y almacenamiento de mensajes**: Guarda los mensajes de los usuarios en una base de datos para su análisis.
- **Análisis de intenciones y sentimientos**: Clasifica los mensajes según su intención y sentimiento.
- **Moderación automática**: Responde automáticamente a mensajes con sentimiento negativo.
- **Conclusiones del grupo**: Genera un resumen de los temas más hablados en el grupo.
- **Mensajes de bienvenida**: Da la bienvenida a nuevos miembros del grupo.
- **Comandos de administración**:
  - `/toggle_moderation`: Activa o desactiva la moderación.
  - `/list_users`: Lista todos los usuarios en el grupo.
  - `/warn @usuario`: Advierte a un usuario específico.
  - `/kick @usuario`: Expulsa a un usuario específico.
  - `/stats`: Muestra estadísticas del grupo.

## Configuración

1. Clona el repositorio:
   ```sh
   git clone https://github.com/Lean031110/Telegram_bot_IA.git
   cd Telegram_bot_IA
   ```

2. Instala las dependencias:
   ```sh
   pip install -r requirements.txt
   ```

3. Configura el token del bot en el archivo `.env`:
   ```
   TELEGRAM_BOT_TOKEN=your-telegram-bot-token
   ```

4. Inicializa la base de datos:
   ```sh
   python -c "from database import init_db; init_db()"
   ```

## Ejecución

Inicia el bot:
```sh
python main.py
```

## Notas

- Asegúrate de que el archivo `config.py` tiene los nombres de usuario de los administradores.
- El bot se reentrenará automáticamente después de capturar un cierto número de mensajes nuevos.
