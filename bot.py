import os

import discord
from discord.ext import commands
from dotenv import load_dotenv


# Cargar variables del archivo .env
load_dotenv()

TOKEN = os.getenv("DISCORD_TOKEN")


# Intents básicos
intents = discord.Intents.default()


# Crear el bot
bot = commands.Bot(
    command_prefix="!",
    intents=intents
)


@bot.event
async def on_ready():
    print("=" * 40)
    print(f"Bot conectado como: {bot.user}")
    print(f"ID del bot: {bot.user.id}")
    print("El bot está listo.")
    print("=" * 40)


# Comprobar que existe el token
if not TOKEN:
    raise ValueError(
        "No se encontró DISCORD_TOKEN en el archivo .env"
    )


# Iniciar el bot
bot.run(TOKEN)