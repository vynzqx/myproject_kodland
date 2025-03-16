import discord
from discord.ext import commands
import random, os

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

organik = ['daun', 'kulit pisang', 'makanan sisa',
           'sayur busuk', 'nasi basi', 'tulang ikan', 
           'ampas kopi', 'kulit telur', 'batang pisang', 
           'kotoran hewan', 'ranting kayu', 'serbuk kayu', 
           'rumput', 'teh celup bekas', 'tisu bekas', 
           'jerami', 'sabut kelapa', 'biji buah', 
           'cangkang udang', 'cangkang kepiting'
] 

anorganik =  [
    'plastik', 'botol plastik', 'kaca', 'kaleng', 'besi', 'aluminium', 
    'styrofoam', 'kardus bekas', 'baterai', 'kertas aluminium', 
    'sedotan', 'bungkus makanan', 'tutup botol', 'helm rusak', 
    'ban bekas', 'elektronik bekas', 'lampu neon', 'cd bekas', 
    'dvd bekas', 'kabel', 'paku', 'baut', 'pipa pvc'
]

b3 = [
    'oli bekas', 'aki bekas', 'obat kadaluarsa', 'cat tembok', 
    'deterjen', 'pestisida'
]

@bot.command()
async def sampah(ctx, *, item: str=None):
    if item is None:
        await ctx.send('Tolong sebut **nama sampah** setelah command')
        await ctx.send('misal: $sampah plastik')
        return

    if item.lower() in organik:
        await ctx.send(f'{item} adalah Sampah Organik')
        await ctx.send(f'Cara menyikapi sampah{item} ini adalah: ')
        await ctx.send('Sampah organik dapat diolah menjadi kompos')
    elif item.lower() in anorganik:
        await ctx.send(f'{item} adalah Sampah Anorganik')
        await ctx.send(f'Cara menyikapi Sampah{item} ini adalah: ')
        await ctx.send('Sampah anorganik dapat didaur ulang menjadi produk baru.')
    elif item.lower() in b3:
        await ctx.send(f'{item} adalah Sampah b3')
        await ctx.send(f'Cara menyikapi Sampah{item} ini adalah: ')
        await ctx.send('Simpan sampah B3 di tempat yang aman, jauh dari jangkauan anak-anak dan hewan peliharaan.')
    else:
        await ctx.send(f'{item} sepertinya bukan sampah')

bot.run('masukkan token anda')
