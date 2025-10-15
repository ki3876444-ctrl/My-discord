import io
import aiohttp
import discord
from discord.ext import commands

# ====== CẤU HÌNH BOT ======
TOKEN = ""  # Thay bằng token bot của bạn
COMMAND_PREFIX = "!"
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix=COMMAND_PREFIX, intents=intents)

# ====== SỰ KIỆN READY ======
@bot.event
async def on_ready():
    print(f"[READY] {bot.user} đã đăng nhập ✅")

# ====== LỆNH CHECK BAN ======
@bot.command()
async def check(ctx, uid: str):
    """Kiểm tra tài khoản có bị ban không"""
    url = f"http://87.106.82.84:13522/check?uid={uid}"
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as resp:
            if resp.status != 200:
                await ctx.send(f"❌ Không thể check UID {uid} — lỗi {resp.status}")
                return
            data = await resp.json()
            status = data.get("is_banned", "Không rõ")
            await ctx.send(f"✅ UID `{uid}` trạng thái: {status}")

# ====== LỆNH AVATAR ======
@bot.command()
async def avatar(ctx, uid: str):
    """Gửi avatar Free Fire của UID"""
    url = f"https://profile.thug4ff.com/api/profile?uid={uid}"
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as resp:
            data = await resp.read()
            if len(data) < 100:
                await ctx.send(f"❌ UID `{uid}` không có avatar hoặc API trả trống")
                return
            await ctx.send(file=discord.File(io.BytesIO(data), filename=f"{uid}_avatar.png"))

# ====== LỆNH PROFILE CARD ======
@bot.command()
async def profile(ctx, uid: str):
    """Gửi profile card Free Fire của UID"""
    url = f"https://profile.thug4ff.com/api/profile_card?uid={uid}"
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as resp:
            data = await resp.read()
            if len(data) < 100:
                await ctx.send(f"❌ UID `{uid}` không có profile card")
                return
            await ctx.send(file=discord.File(io.BytesIO(data), filename=f"{uid}_card.png"))

# ====== LỆNH LIKE ======
@bot.command()
async def like(ctx, uid: str):
    """Gửi like đến UID"""
    url = f"https://ff.mlbbai.com/like/?key=emon&uid={uid}"
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as resp:
            try:
                data = await resp.json()
                await ctx.send(f"📦 Phản hồi API: ```{data}```")
            except:
                text = await resp.text()
                await ctx.send(f"📦 Phản hồi API (không phải JSON): ```{text}```")

# ====== CHẠY BOT ======
bot.run(TOKEN)