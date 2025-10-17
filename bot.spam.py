import io
import aiohttp
import discord
from discord.ext import commands

# ---------------- CONFIG ----------------
TOKEN = ""
PREFIX = "!"
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix=PREFIX, intents=intents)

# ---------------- EVENTS ----------------
@bot.event
async def on_ready():
    print(f"✅ Bot {bot.user} đã đăng nhập thành công!")

# ---------------- LỆNH INFO ----------------
@bot.command()
async def info(ctx, uid: str):
    """Hiển thị JSON gốc, banner & outfit"""
    wait_msg = await ctx.send(f"⏳ Đang tải dữ liệu UID `{uid}`...")

    info_api = f"http://217.154.239.23:13984/info={uid}"
    banner_api = f"http://212.227.65.132:13521/bnr?uid={uid}&key=AlliFF_BOT_V1"
    outfit_api = f"https://danger-outfit-info.vercel.app/outfit-image?uid={uid}&key=DANGER-OUTFIT"

    async with aiohttp.ClientSession() as session:
        # JSON gốc
        async with session.get(info_api) as resp:
            try:
                info_json = await resp.json()
            except:
                info_json = {"error": f"Không đọc được JSON ({resp.status})"}

        # Avatar góc phải
        async with session.get(banner_api) as resp:
            avatar_data = await resp.read()

        # Outfit
        async with session.get(outfit_api) as resp:
            outfit_data = await resp.read()

    embed = discord.Embed(
        title=f"🧩 Info UID {uid}",
        description="JSON gốc:",
        color=discord.Color.blurple()
    )

    for k, v in info_json.items():
        embed.add_field(name=str(k), value=str(v), inline=True)

    embed.set_footer(text="Dev: Sikibidi 🚀")

    files = []
    if avatar_data and len(avatar_data) > 100:
        files.append(discord.File(io.BytesIO(avatar_data), filename=f"{uid}_avatar.png"))
        embed.set_thumbnail(url=f"attachment://{uid}_avatar.png")
    if outfit_data and len(outfit_data) > 100:
        files.append(discord.File(io.BytesIO(outfit_data), filename=f"{uid}_outfit.png"))
        embed.set_image(url=f"attachment://{uid}_outfit.png")

    await wait_msg.edit(content=None, embed=embed, attachments=files)

# ---------------- LỆNH LIKE ----------------
@bot.command()
async def like(ctx, uid: str):
    """Gửi like đến UID"""
    wait_msg = await ctx.send(f"⏳ Đang gửi like đến UID `{uid}`...")

    url = f"https://ff.mlbbai.com/like/?key=emon&uid={uid}"

    async with aiohttp.ClientSession() as session:
        async with session.get(url) as resp:
            try:
                data = await resp.json()
            except:
                data = {"error": f"Không đọc được JSON ({resp.status})"}

    embed = discord.Embed(
        title=f"❤️ Like UID {uid}",
        description="JSON gốc từ API like:",
        color=discord.Color.red()
    )
    for k, v in data.items():
        embed.add_field(name=str(k), value=str(v), inline=True)
    embed.set_footer(text="Dev: Sikibidi 🚀")

    await wait_msg.edit(content=None, embed=embed)

# ---------------- LỆNH CHECKBAN ----------------
@bot.command()
async def checkban(ctx, uid: str):
    """Kiểm tra trạng thái ban của UID"""
    wait_msg = await ctx.send(f"🔍 Đang kiểm tra UID `{uid}`...")

    api = f"http://87.106.82.84:13522/check?uid={uid}"

    async with aiohttp.ClientSession() as session:
        async with session.get(api) as resp:
            try:
                data = await resp.json()
            except:
                data = {"error": f"Không đọc được JSON ({resp.status})"}

    embed = discord.Embed(
        title=f"🚫 Check Ban UID {uid}",
        description="JSON gốc từ API check ban:",
        color=discord.Color.orange()
    )
    for k, v in data.items():
        embed.add_field(name=str(k), value=str(v), inline=True)
    embed.set_footer(text="Dev: Sikibidi 🚀")

    await wait_msg.edit(content=None, embed=embed)

# ---------------- LỆNH VISIT ----------------
@bot.command()
async def visit(ctx, uid: str):
    """Gửi lượt visit và hiển thị JSON gốc"""
    wait_msg = await ctx.send(f"⏳ Đang gửi visit cho UID `{uid}`...")

    url = f"https://api-visit-alliff-v2.vercel.app/visit?uid={uid}"

    async with aiohttp.ClientSession() as session:
        async with session.get(url) as resp:
            try:
                data = await resp.json()
            except:
                data = {"error": f"Không đọc được JSON ({resp.status})"}

    embed = discord.Embed(
        title=f"🚀 Visit UID {uid}",
        description="JSON gốc từ API visit:",
        color=discord.Color.green()
    )
    for k, v in data.items():
        embed.add_field(name=str(k), value=str(v), inline=True)
    embed.set_footer(text="Dev: Sikibidi 🚀")

    await wait_msg.edit(content=None, embed=embed)

# ---------------- RUN BOT ----------------
bot.run(TOKEN)