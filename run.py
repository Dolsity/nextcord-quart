from quart import Quart, render_template, redirect, url_for
from quart_discord import DiscordOAuth2Session
from nextcord.ext import ipc
import os
from dotenv import load_dotenv
from pymongo import MongoClient

load_dotenv()
mongo_uri = os.getenv('MONGO_URI')
cluster = MongoClient(mongo_uri)
db = cluster["name"]
database = db["database"]

app = Quart(__name__)
ipc_client = ipc.Client()

app.secret_key = os.getenv('SECRET_KEY')
app.config["DISCORD_CLIENT_ID"] = os.getenv('DISCORD_CLIENT_ID')
app.config["DISCORD_CLIENT_SECRET"] = os.getenv('DISCORD_CLIENT_SECRET')
app.config["DISCORD_REDIRECT_URI"] = "http://127.0.0.1:5000/callback"

discord = DiscordOAuth2Session(app)

@app.route("/")
@app.route("/home")
async def home():
    if await discord.authorized:
        user_name = (await discord.fetch_user()).name
        user_avatar = (await discord.fetch_user()).avatar_url
                
        return await render_template("index.html", authorized = await discord.authorized, username = user_name, user_avatar = user_avatar)
    
    return await render_template("index.html", authorized = await discord.authorized)

@app.route("/callback")
async def callback():
	try:
		await discord.callback()
	except Exception:
		pass
	return redirect(url_for("home"))

@app.route("/login")
async def login():
	return await discord.create_session()

@app.route("/logout")
async def logout():
    discord.revoke()
    return redirect(url_for("home"))

if __name__ == "__main__":
    app.debug = False
    app.run()