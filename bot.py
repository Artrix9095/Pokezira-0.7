import discord
import sqlite3
from discord.ext import commands
from passlib.hash import sha256_crypt as crypt

bot = commands.Bot(command_prefix=["@", ";"])


def getUserId(discord_id):
  db = sqlite3.connect("discord.db")
  c = db.cursor()
  c.execute(f"SELECT zira_id FROM discord WHERE discord_id = '{discord_id}'")
  return c.fetchone()[0]


@bot.event
async def on_ready():
  print("up and running")


@bot.command()
async def login(ctx, username, password):
  print(password)
  if password == None:
    await ctx.send("Error: Password must be a spoiler")
    return
  password = password.replace("||", "")
  db = sqlite3.connect("user.db")
  c = db.cursor()
  c.execute("SELECT user_id, password FROM user WHERE username = ?",(username,))
  payload = c.fetchone()
  if payload == None:
    await ctx.send("No user with that username!")
    return 
  else:
    if crypt.verify(password, payload[1]):
      con = sqlite3.connect("discord.db")
      conn = con.cursor()
      conn.execute("INSERT INTO discord(discord_id, zira_id) VALUES(?,?)",(ctx.author.id, payload[0]))
      con.commit()
      con.close()
      db.close()
      await ctx.send("You logged in!")
    else:
      await ctx.send("Invalid Password!")
@bot.command()
async def pokemon(ctx):
  ID = getUserId(str(ctx.author.id))
  db = sqlite3.connect("user.db")
  c = db.cursor()
  c.execute("SELECT pokemon FROM userpoke WHERE user_id = ?",(ID,))
  pokes = c.fetchall()
  msg = ""
  for x in pokes:
    msg += x[0]+"\n"
  await ctx.send(msg)

  

def run():
  import os 
  bot.run(os.environ["BOT_TOKEN"])