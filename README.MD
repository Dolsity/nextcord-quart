<p align="center">
    <img width="100px" src="static/img/logo.png" />
</p>

<h1 align="center">
    Discord Bot using Nextcord and Quart
</h1>

<p align="center">
    Discord leveling made easy
</p>

</p>
<p align="center">
    <a href="https://github.com/dolsity/discord-leveling/issues">
        <img alt="Issues" src="https://img.shields.io/github/issues/dolsity/nextcord-quart?color=0088ff" />
    </a>
<a href="https://github.com/dolsity/discord-leveling/pulls">
    <img alt="GitHub pull requests" src="https://img.shields.io/github/issues-pr/dolsity/nextcord-quart?color=0088ff" />
</a>
<br />
<br />
<a href="https://discord.com">
    <img src="https://img.shields.io/badge/Platform%20-Discord%20%E2%86%92-gray.svg?colorA=5865F2&colorB=4552d9&style=for-the-badge"/>
</a>
<a href="https://www.python.org/downloads/release/python-3101/">
    <img src="https://img.shields.io/badge/Python%20-v3.10.1%20%E2%86%92-gray.svg?colorA=Ffd43b&colorB=306998&style=for-the-badge"/>
</a>
 <a href="https://docs.nextcord.dev/en/stable/">
    <img src="https://img.shields.io/badge/Library%20-Nextcord%20%E2%86%92-gray.svg?colorA=eed142&colorB=fed142&style=for-the-badge"/>
</a>
<a href="https://www.mongodb.com">
    <img src="https://img.shields.io/badge/Database%20-MongoDB%20%E2%86%92-gray.svg?colorA=10821b&colorB=065e0f&style=for-the-badge"/>
</a>

<p align="center">
    <a href="https://github.com/dolsity/nextcord-quart/issues/new/choose">Report Bug</a>
    ·
    <a href="https://github.com/dolsity/nextcord-quart/issues/new/choose">Request Feature</a>
</p>

<h2>Setting up</h2>

**<p>1. Install the requirements</p>**

```python
python3 -m pip install -r requirements.txt
```

**<p>2. Rename `.example_env` to `.env`</p>**

**<p>3. We need to edit the `.env` file now</p>**
- Paste your a secret key of your own where `SECRET_KEY=`
- Paste your mongo uri where `MONGO_URI=`
- Paste your Discord Client ID where `DISCORD_CLIENT_ID=`
- Paste your Discord Client Secret where `DISCORD_CLIENT_SECRET=`

**<p>Make sure to paste the callback url in the redirects of your Discord bot:</p>**
<img width="500px" src="static/img/redirects.png" />


<h2>Preview:</h2>
<img width="500px" src="static/img/preview.png" />
