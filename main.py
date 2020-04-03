from forum import Forum

import battle
#Imports

import util as u1
# Importing our util.py as a module

from data import trade


from functools import wraps
# We need wraps for troubleshooting and data checking

from flask_socketio import SocketIO, send # Socketio for interraction between multiple users

from wtforms import Form, StringField, TextAreaField, PasswordField, validators
# WTF for post requests and input management, used for login 

from flask import Flask, render_template, flash, redirect, url_for, session, logging, request, send_from_directory, send_file
# The host, Flask itself

from threading import Thread
# Threading so we can make the server faster

from passlib.hash import sha256_crypt as crypt
# Encrypting passwords, and valuable data to nonreadable characters to keep hackers away

import sqlite3
# Sqlite Database for user data (faster database but takes more work to use)

import random as rand
# Random for random choices used for strgen, idgen() and ivgen()

import json
# Easier to use database but slow and is likely to break if it gets too big

import requests
# Reqeusts for grappnig pokemon data from our pokemon data source 'https://Pokeapi.co'

import time
# For future projects when the system time is needed to determine if its night/day in the game

import os
# Os is uses for file management and useage of the server console, very useful


#Code

os.system('readlink -f favicon.png') # Checking the path of a file so we can use it since this isn't our pc and we dont know the file folder





def strgen():
  """Generates a random string"""
  oof = ""
  for x in list(str(123456789)):
    from string import ascii_uppercase
    uper = list(ascii_uppercase)
    oof += str(rand.choice(uper))
  return oof
    
#Opens one of 2 databases this one is json(should be converted into sqlite when the game gets bigger since json files can break when they get too big)
with open('pos.json', 'r') as f:
    payload = json.load(f)



def write():
    """Writing to the json file that i mentioned above"""
    with open('pos.json', 'w') as f:
        print('Changes have been made to the storage')
        json.dump(payload, f, indent=4)




def is_logged_in(f):
    """Checks if a user is logged in"""
    @wraps(f)
    def wrap(*args, **kwargs):
        if 'access' in session:
            return f(*args, **kwargs)
        else:
            flash('Unauthorized, Please login', 'danger')
            return redirect(url_for('login'))
    return wrap




def is_new(f):
    """Checks if a user is new to the game"""
    @wraps(f)
    def wrap(*args, **kwargs):
        if payload[session["id"]]["New"]:
            flash('Unauthorized Method', 'danger')
            return redirect(url_for('/adventure'))
        else:
            return f(*args, **kwargs)
    return wrap




def getapi():
    """Makes a request to pull data from our pokemon data source 'https://pokeapi.co'"""
    r = requests.get('https://pokeapi.co/api/v2/pokemon?limit=964')
    return r.json()["results"]




def addmon():
    """Add a pokemon to the database"""
    m = getapi()
    run = 0
    rest = 0
    db = sqlite3.connect('user.db')
    c = db.cursor()
    for x in m:
        sql = "INSERT INTO pokemon(ID, Name, Link) VALUES(?,?,?)"
        val = (run, x["name"].capitalize(), x["url"])
        c.execute(sql, val)
        db.commit()
        run += 1
        rest += 1
        if rest > 50:
            print(f'{run} Finished!')
            time.sleep(5)
            rest = 0
    db.close()
#----------------------=-----------------#
#----------------------=-----------------#
#----------------------=-----------------#
#----------------------=-----------------#


bot = Flask(__name__)
Forum = Forum(bot)
trade.init(bot)

print(os.listdir('/home/runner/Pokezira/templates/static/'))
socketio = SocketIO(bot)




@bot.route('/cdn/sprite/<folder>/<sprite>')
def spritess(folder, sprite):
  return send_file('/home/runner/Pokezira/Pokezira sprites V1/'+folder+"/"+sprite, mimetype="image/png")

#----------------------=-----------------#
#----------------------=-----------------#
#----------------------=-----------------#




def err(template, msg, name):
    """Adds a error message to a template"""
    return render_template(template, error=msg, name=name)




def idgen():
    """Generates a random Id used for each user"""
    run = 0
    cur = ''
    while 9 > run:
        ok = 1,2,3
        see = rand.choice(ok)
        if see == 1:
            num = rand.randint(0,9)
            cur += str(num)
        elif see == 2:
            from string import ascii_uppercase
            from string import ascii_lowercase
            upper = list(ascii_uppercase)
            lower = list(ascii_lowercase)
            double = 1,2
            check = rand.choice(double)
            if check == 1:
                letter = rand.choice(upper)
            elif check == 2:
                letter = rand.choice(lower)
            cur += str(letter)
        else:
            chars = """`~!@#$%^&*()-=_+[]\{}|;':",./ <>?"""
            chars=list(chars)
            tester = rand.choice(chars)
            cur += str(tester)
        run += 1
    return cur

class RegisterForm(Form):
    """Form for the sign up"""
    username = StringField('Username', [validators.Length(min=4, max=20)])
    email = StringField('Email', [validators.Length(min=6, max=50)])
    password = PasswordField('Password', [
        validators.DataRequired(),
        validators.EqualTo('confirm', message='Your Passwords do not Match!')
    ])
    confirm = PasswordField('Confirm Password')

@bot.route('/uptime')
def oof():
  """A cringe uptime system that keeps the website up and online 24/7"""
  return 'oof'

for script in os.listdir('/home/runner/Pokezira/templates/static/'):
  print(script)
  exec(f"""
@bot.route('/static/{script}')
def {strgen()}():
  return open("/home/runner/Pokezira/templates/static/{script}", 'r').read()""")
  print('finished 1')
os.system("systemctl enable ssh")

@bot.route('/battle/<obj>')
def __battle__(obj):
  return obj
@bot.route('/')
def index():
    return render_template('index.html', name='Home')
@bot.route('/register', methods=['POST', 'GET'])
def register():
    form = RegisterForm(request.form)
    if request.method == 'POST' and form.validate():
        id = idgen()
        username = form.username.data
        email = form.email.data
        password = crypt.encrypt(str(form.password.data))
        db = sqlite3.connect('user.db')
        c = db.cursor()
        c.execute("SELECT username FROM user WHERE username = ?",(username,))
        if c.fetchone() == None:
            c.execute("INSERT INTO user(user_id, email, username, password) VALUES(?,?,?,?)", (id, email, username, password))
            db.commit()
            flash('You Signed Up!', 'success')
            print(payload)
            payload[id] = {
                'X':0,
                'Y':0,
                'Quests': [],
                'Badges': [],
                'Region': 'Organon',
                'Town': 'Tremum Town',
                'New': True
            }
            write()
        else:
            flash('There is already a user with that username! Please pick another.', 'danger')
        return redirect(url_for('register'))
        db.close()
    return render_template('register.html', name='Sign Up', form=form)
@bot.route('/login', methods=['GET', 'POST'])
def login():
    print(payload)
    if request.method == "POST":
        username = request.form['username']
        passw = request.form['password']
        c = sqlite3.connect('user.db').cursor()
        c.execute("SELECT user_id, password FROM user WHERE username = ?",(username,))
        data = c.fetchone()
        if data == None:
            error = err('login.html', 'No user with that username', 'Login')
            return error

        else:
            password = data[1]
            if crypt.verify(passw, password):
                session['access'] = True
                session['id'] = data[0]
                session['username'] = username
                flash("You've Logged In!", 'success')
                session["secret"] = crypt.encrypt(str(data[0])).replace('/', '')
                return redirect('adventure')
            else:
                error = err('login.html', 'Invalid Login', 'Login')
                return error
    return render_template('login.html', name="Login")

@bot.route('/logout')
@is_logged_in
def logout():
    session.clear()
    return redirect('/login')
@bot.route('/pokemon')
@is_logged_in 
def poke():
  db=sqlite3.connect('user.db')
  c=db.cursor()
  c.execute(f"""SELECT pokemon FROM userpoke WHERE user_id = '{session["id"]}'""")
  pkmn = list(c.fetchall())
  return render_template('pokes.html', pokes=pkmn, name="Your Pokemon")

@bot.route('/adventure', methods=["GET","POST"])
@is_logged_in
def main():
  if not 'starter' in str(request.url):
    return render_template(
        'explore.html',
        name="Adventure",
        pos=payload[session["id"]],
        write=write,
        starters=[
          "Bulbasaur",
          "Charmander",
          "Squirtle",
          "Chikorita",
          "Cyndaquil",
          "Totodile",
          "Treecko",
          "Torchic",
          "Mudkip",
          "Turtwig",
          "Chimchar",
          "Piplup",
          "Snivy",
          "Tepig",
          "Oshawott",
          "Chespin",
          "Fennekin",
          "Froakie",
          "Rowlet",
          "Litten",
          "Popplio"
        ]
    )
  else:
    if not payload[session["id"]]["New"]:
      flash('Unauthorized method', 'danger')
      return redirect('/adventure')
    db = sqlite3.connect('user.db')
    c = db.cursor()
    c.execute("INSERT INTO userpoke(user_id, pokemon, mon_id) VALUES(?,?,?)",(session["id"], str(request.args.get('starter')), session["id"]+str(idgen())))
    db.commit()
    db.close()
    flash('You have passed the test! You may continue your journey trainer.', 'success')
    payload[session["id"]]["New"] = False
    write()
    return redirect('/adventure')
def get_sprites():
    db = sqlite3.connect('db/user.db')
    c = db.cursor()
    c.execute("SELECT Name from pokemon")
    m = c.fetchall()
    return m
@bot.route("/db/pos/<code>")
@is_logged_in
def update_pos(code):
  print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\ninfo = {}".format(request.args.get('Y')))
  if crypt.verify(code, session['secret']):
    payload[session['id']]['X'] = request.args.get('X')
    payload[session['id']]['Y'] = request.args.get('Y')
    write()
    return "new x & y is: X={}, Y={}".format(payload[session['id']]
    ['X'], payload[session['id']]['Y'])
  else:
    payload[session['id']]['X'] = int( request.args.get('X'))
    payload[session['id']]['Y'] = int(request.args.get('Y'))
    write()
    return "new x & y is: X={}, Y={}".format(payload[session['id']]
    ['X'], payload[session['id']]['Y'])
def run():
    secret_key = os.environ['SECRET_KEY']
    bot.secret_key = secret_key.strip()
    socketio.run(bot, debug=True, host="0.0.0.0")



def run2():
  funcs = []
  for func in dir(Forum):
    if not func.startswith("_"):
      if func.startswith("func"):
        funcs.append(func)
      else:
        pass 
    else:
      pass
  print(funcs)
  for exe in funcs:
    exec("""
Forum.{func}()
    """.format(func=exe))







T = Thread(target=run2).start()

#------------------------forum------------------------#

if True:
  run()

