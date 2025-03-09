import discord
from discord.ext import commands
from mycode import gen_pass

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Hi! I am a bot {bot.user}!')

@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)

@bot.command()
async def generate_password(ctx):
    await ctx.send('ini password untukmu:')
    await ctx.send(gen_pass(10))

@bot.command()
async def pangkatkan(ctx):
    await ctx.send('coba kirim angka yang ingin di pangkatkan')
    angka = await bot.wait_for('message', check=lambda m: m.author == ctx.author and m.channel == ctx.channel)
    angka = int(angka.content)

    await ctx.send('berikut pangkat dua dari {angka}')
    await ctx.send(angka**2)

@bot.command()
async def tebak_angka(ctx):
    angka_rahasia = random.randint(1, 10)
    await ctx.send("Aku memikirkan angka antara 1 sampai 10. Coba tebak!")

    def check(m):
        return m.author == ctx.author and m.channel == ctx.channel

    for i in range(3):  # Memberikan 3 kesempatan
        tebakan = await bot.wait_for('message', check=check)
        if int(tebakan.content) == angka_rahasia:
            await ctx.send("Benar! Kamu menang! 🎉")
            return
        else:
            await ctx.send("Salah! Coba lagi.")

    await ctx.send(f"Kesempatan habis! Angka yang benar adalah **{angka_rahasia}**.")

@bot.command()
async def ramalan(ctx):
    ramalan = [
        "Besok kamu akan ketemu kucing belang tiga, itu pertanda kamu akan dapat jodoh!",
        "Hati-hati, besok kamu akan kehabisan kuota internet!",
        "Ramalan saya: kamu akan makan nasi hari ini. Wow, luar biasa!"
    ]
    await ctx.send(random.choice(ramalan))

@bot.command()
async def joke(ctx):
    jokes = [
        "Kenapa ayam menyebrang jalan? Untuk sampai ke seberang!",
        "Apa yang dikatakan kertas ke gunting? Kamu selalu memotong aku!",
        "Kenapa buku nggak bisa naik tangga? Karena dia punya banyak lembaran!"
    ]
    await ctx.send(random.choice(jokes))

@bot.command()
async def help(ctx):
    help_message = """
    **🤖 Daftar Perintah Bot 🤖**
    Berikut adalah beberapa hal yang bisa aku lakukan:

    - `$hello`: Aku akan menyapamu!
    - `$heh [jumlah]`: Aku akan mengirim "he" sebanyak yang kamu minta.
    - `$generate_password`: Aku akan membuatkan password acak untukmu.
    - `$pangkatkan`: Aku akan menghitung pangkat dua dari angka yang kamu berikan.
    - `$tebak_angka`: Ayo tebak angka yang aku pikirkan!
    - `$ramalan`: Aku akan memberikan ramalan lucu untukmu.
    - `$joke`: Aku akan menceritakan dad joke yang bikin kamu geleng-geleng.

    Gunakan perintah di atas dan bersenang-senanglah! 🎉
    """
    await ctx.send(help_message)



bot.run("Masukkan kode token anda") 
