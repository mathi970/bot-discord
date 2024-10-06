import discord
import random
import os
from bot_logic import get_duck_image_url
from bot_logic import gen_pass
from discord.ext import commands 
# La variable intents almacena los privilegios del bot
intents = discord.Intents.default()
# Activar el privilegio de lectura de mensajes
intents.message_content = True
# Crear un bot en la variable cliente y transferirle los privilegios
bot = commands.Bot(command_prefix = "$" , intents=intents)
@bot.event
async def on_ready():
    print(f'Hemos iniciado sesión como {bot.user}')
@bot.command ()
async def hello(ctx):
    await ctx.send("Hi!")
@bot.command ()
async def bye(ctx):
    await ctx.send("😞")
@bot.command ()
async def password(ctx):
    await ctx.send(gen_pass(10))
@bot.command()
async def joined(ctx, member: discord.Member):
    await ctx.send(f'{member.name} joined {discord.utils.format_dt(member.joined_at)}')
@bot.command()
async def bien(ctx):
    await ctx.send("👍")
@bot.command()
async def add(ctx, left: int, right: int):
    await ctx.send(left + right)
@bot.command()
async def dato(ctx):
    datos_curiosos = [
        "las huellas dactilares de los koalas son muy similares a las de los humanos", "el corazon de los camarones se encuentra en la cabeza", "las medusas de la especie turritopsis dohrnii pueden revertir su ciclo joven, es decir son potencialmente inmortales"
    ]
    await ctx.send(random.choice(datos_curiosos))
@bot.command()
async def mem(ctx):
    meme_alet = random.choice(os.listdir("image"))
    with open(f'image/{meme_alet}.jpg', 'rb') as f:
        # ¡Vamos a almacenar el archivo de la biblioteca Discord convertido en esta variable!
        picture = discord.File(f)
    # A continuación, podemos enviar este archivo como parámetro.
    await ctx.send(file=picture)
@bot.command()
async def meme_aleatorio(ctx):
    with open('image/mem1.jpg', 'rb') as f:
        # ¡Vamos a almacenar el archivo de la biblioteca Discord convertido en esta variable!
        picture = discord.File(f)
    # A continuación, podemos enviar este archivo como parámetro.
    await ctx.send(file=picture)

@bot.command('duck')
async def duck(ctx):
    '''Una vez que llamamos al comando duck, 
    el programa llama a la función get_duck_image_url'''
    image_url = get_duck_image_url()
    await ctx.send(image_url)


bot.run("MTI4Nzc1NDQ5NzQxMzc0MjY2Mg.GZ68IL.VaZieXjOx0plhKYxVx5UUpRcHrWq5aG4ISX2xMttt")
