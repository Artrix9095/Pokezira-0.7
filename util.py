import random
import sqlite3 as sql
import requests


class other(object):
  """Other useful functions to keep main.py smaller"""
  def reqJSON(url):
    return requests.get(url).json()
  def checkDB(table):
    g = newConn()
    c = g['cursor']
    c.execute('SELECT * FROM {s}'.format(s=table))
    return c.fetchall()

def success(a):
  """Success function to verify the script was successful"""
  print(f'\n\n{a} successfully completed its mission\n\n')
  return f'{a} successfully completed its mission'


def newConn():
  """Saves a few button presses by opening a database and returning the output as a dict"""
  g = sql.connect('user.db')
  e = g.cursor()
  return {
    "close": g.close,
    "commit": g.commit,
    "cursor": e
  }



  def ivgen(pokeId):
    """Generates a fresh new iV set and inserts it into the database"""
    h = other.newConn()
    close = h['close']
    commit = h['commit']
    c = h['cursor']
    c.execute("""
      INSERT INTO pokeiv
      (ID,
      HPiv,
      Atkiv,
      Defiv,
      SpAtkiv,
      SpDefiv,
      Speediv)
      VALUES(?,?,?,?,?,?,?)
    """, (

        pokeId,
        random.randint(0,31),
        random.randint(0,31),
        random.randint(0,31),
        random.randint(0,31),
        random.randint(0,31),
        random.randint(0,31)

    ))

    commit()
    close()
    return other.success('ivgen')



class pokeManage(object):
  def ivgen(pokeId):
    """Generates a fresh new iV set and inserts it into the database"""
    h = newConn()
    close = h['close']
    commit = h['commit']
    c = h['cursor']
    c.execute("""
      INSERT INTO pokeiv
      (ID,
      HPiv,
      Atkiv,
      Defiv,
      SpAtkiv,
      SpDefiv,
      Speediv)
      VALUES(?,?,?,?,?,?,?)
    """, (

        pokeId,
        random.randint(0,31),
        random.randint(0,31),
        random.randint(0,31),
        random.randint(0,31),
        random.randint(0,31),
        random.randint(0,31)

    ))

    commit()
    close()
    return success('ivgen')


  def validMoves(pokeId, Lvl):
    payload = other.reqJSON("https://pokeapi.co/api/v2/pokemon/"+str(pokeId))
    valid = []
    for x in payload['moves']:
      base = x['version_group_details']
      lvlReq = base[0]['level_learned_at']
      if lvlReq >= Lvl:
        pass
      else:
        if base[0]["move_learn_method"]["name"] == "level-up":
          valid.append(x['move']['name'])
        else:
          pass
    return valid


  """def statsCalc(ev, iv, pokeId):
    import math
    payload = other.reqJSON("https://pokeapi.co/api/v2/pokemon/"+str(pokeId))
    for in payload['stats']:

    #math.floor(math.floor((((iv + (2 * base[stat]) + (ev / 4) + 100) * lvl) / 100) + 10) * nat)
    """
      



