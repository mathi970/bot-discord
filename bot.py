import discord
import random
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



bot.run("MTI4Nzc1NDQ5NzQxMzc0MjY2Mg.GZ68IL.VaZieXjOx0plhKYxVx5UUpRcHrWq5aG4ISX2xMttt")
