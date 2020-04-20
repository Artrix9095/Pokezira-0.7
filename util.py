import random
import sqlite3 as sql
import requests


natures = [{"name":"Adamant","hp":1,"atk":1.1,"def":1,"spa":0.9,"spd":1,"spe":1,"summary":"+Atk, -SpA","genfamily":["RS","DP","BW","XY"]},{"name":"Bashful","hp":1,"atk":1,"def":1,"spa":1,"spd":1,"spe":1,"summary":"","genfamily":["RS","DP","BW","XY"]},{"name":"Bold","hp":1,"atk":0.9,"def":1.1,"spa":1,"spd":1,"spe":1,"summary":"+Def, -Atk","genfamily":["RS","DP","BW","XY"]},{"name":"Brave","hp":1,"atk":1.1,"def":1,"spa":1,"spd":1,"spe":0.9,"summary":"+Atk, -Spe","genfamily":["RS","DP","BW","XY"]},{"name":"Calm","hp":1,"atk":0.9,"def":1,"spa":1,"spd":1.1,"spe":1,"summary":"+SpD, -Atk","genfamily":["RS","DP","BW","XY"]},{"name":"Careful","hp":1,"atk":1,"def":1,"spa":0.9,"spd":1.1,"spe":1,"summary":"+SpD, -SpA","genfamily":["RS","DP","BW","XY"]},{"name":"Docile","hp":1,"atk":1,"def":1,"spa":1,"spd":1,"spe":1,"summary":"","genfamily":["RS","DP","BW","XY"]},{"name":"Gentle","hp":1,"atk":1,"def":0.9,"spa":1,"spd":1.1,"spe":1,"summary":"+SpD, -Def","genfamily":["RS","DP","BW","XY"]},{"name":"Hardy","hp":1,"atk":1,"def":1,"spa":1,"spd":1,"spe":1,"summary":"","genfamily":["RS","DP","BW","XY"]},{"name":"Hasty","hp":1,"atk":1,"def":0.9,"spa":1,"spd":1,"spe":1.1,"summary":"+Spe, -Def","genfamily":["RS","DP","BW","XY"]},{"name":"Impish","hp":1,"atk":1,"def":1.1,"spa":0.9,"spd":1,"spe":1,"summary":"+Def, -SpA","genfamily":["RS","DP","BW","XY"]},{"name":"Jolly","hp":1,"atk":1,"def":1,"spa":0.9,"spd":1,"spe":1.1,"summary":"+Spe, -SpA","genfamily":["RS","DP","BW","XY"]},{"name":"Lax","hp":1,"atk":1,"def":1.1,"spa":1,"spd":0.9,"spe":1,"summary":"+Def, -SpD","genfamily":["RS","DP","BW","XY"]},{"name":"Lonely","hp":1,"atk":1.1,"def":0.9,"spa":1,"spd":1,"spe":1,"summary":"+Atk, -Def","genfamily":["RS","DP","BW","XY"]},{"name":"Mild","hp":1,"atk":1,"def":0.9,"spa":1.1,"spd":1,"spe":1,"summary":"+SpA, -Def","genfamily":["RS","DP","BW","XY"]},{"name":"Modest","hp":1,"atk":0.9,"def":1,"spa":1.1,"spd":1,"spe":1,"summary":"+SpA, -Atk","genfamily":["RS","DP","BW","XY"]},{"name":"Naive","hp":1,"atk":1,"def":1,"spa":1,"spd":0.9,"spe":1.1,"summary":"+Spe, -SpD","genfamily":["RS","DP","BW","XY"]},{"name":"Naughty","hp":1,"atk":1.1,"def":1,"spa":1,"spd":0.9,"spe":1,"summary":"+Atk, -SpD","genfamily":["RS","DP","BW","XY"]},{"name":"Quiet","hp":1,"atk":1,"def":1,"spa":1.1,"spd":1,"spe":0.9,"summary":"+SpA, -Spe","genfamily":["RS","DP","BW","XY"]},{"name":"Quirky","hp":1,"atk":1,"def":1,"spa":1,"spd":1,"spe":1,"summary":"","genfamily":["RS","DP","BW","XY"]},{"name":"Rash","hp":1,"atk":1,"def":1,"spa":1.1,"spd":0.9,"spe":1,"summary":"+SpA, -SpD","genfamily":["RS","DP","BW","XY"]},{"name":"Relaxed","hp":1,"atk":1,"def":1.1,"spa":1,"spd":1,"spe":0.9,"summary":"+Def, -Spe","genfamily":["RS","DP","BW","XY"]},{"name":"Sassy","hp":1,"atk":1,"def":1,"spa":1,"spd":1.1,"spe":0.9,"summary":"+SpD, -Spe","genfamily":["RS","DP","BW","XY"]},{"name":"Serious","hp":1,"atk":1,"def":1,"spa":1,"spd":1,"spe":1,"summary":"","genfamily":["RS","DP","BW","XY"]},{"name":"Timid","hp":1,"atk":0.9,"def":1,"spa":1,"spd":1,"spe":1.1,"summary":"+Spe, -Atk","genfamily":["RS","DP","BW","XY"]}]


class other(object):
  """Other useful functions to keep main.py smaller"""


  def newConn():
    """Saves a few button presses by opening a database and returning the output as a dict"""
    g = sql.connect('user.db')
    e = g.cursor()
    return {
      "close": g.close,
      "commit": g.commit,
      "cursor": e
    }


  def reqJSON(url):
    return requests.get(url).json()


  def checkDB(table):
    g = other.newConn()
    c = g['cursor']
    c.execute('SELECT * FROM {s}'.format(s=table))
    return c.fetchall()

  def success(a):
    """Success function to verify the script was successful"""
    print(f'\n\n{a} successfully completed its mission\n\n')
    return f'{a} successfully completed its mission'


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


  def naturegen(synch=False):
    c = []
    for nature in natures:
      c.append(nature['name'])
      l = random.choice(c)
    if not synch:
      return l
    else:
      random.choice((l, synch)) #synch is the actual nature




class pokeManage(object):
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
  



  def statsCalc(ev, iv, BaseStat, nat, stat, lvl, pokeId):
    import math as Math
    def convert(s):
      if s in ['hp','atk','def','spa','spd','spe']:
        return s 
      else:
        conv = {
          'HP': s.lower(),
          'attack': 'atk',
          'defense': 'def',
          'special-attack': 'spa',
          'special-defense': 'spd',
          'speed': 'spe',
          'Atk': s.lower(),
          'Def': s.lower(),
          'SpAtk': 'spa',
          'SpDef': 'spd',
          'Speed': 'spe'
        }
        return conv[s]
    _stat = convert(stat)
    for x in natures:
      if x['name'] == nat.capitalize():
        nature = x
      else:
        pass
    if not stat in ['hp', 'HP']:
      statss = Math.floor(Math.floor((((iv + (2 * BaseStat) + (ev / 4)) * lvl) / 100) + 5) * nature[_stat])
    else:
      statss = Math.floor(Math.floor((((iv + (2 * BaseStat) + (ev / 4) + 100) * lvl) / 100) + 10) * nature[_stat])
    h = other.newConn()
    close = h['close']
    commit = h['commit']
    c = h['cursor']
    del h
    c.execute(f"""
      INSERT INTO pokedata({_stat}) VALUES (
        ?
      )
    """,(statss,))
    commit()
    close()
    return other.success("statsCalc")
    


  def abilitygen(p):
    payload = []
    hidden = ""
    g = other.reqJSON("https://pokeapi.co/api/v2/pokemon/"+p)["abilities"]
    for x in g:
      cur = x["ability"]
      if x["is_hidden"]:
        hidden = cur["name"]
        payload.append(cur["name"])
      else:
        payload.append(cur["name"])
    return [payload, hidden]
    

  def createPokemon(lvl, owner_id, pokemon, idgen, synch=False):
    pokeId = owner_id+idgen()+idgen()
    other.ivgen(pokeId)
    h = other.newConn()
    close = h['close']
    commit = h['commit']
    c = h['cursor']
    del h
    #     'Atk': s.lower(),
    #     'Def': s.lower(),
    #     'SpAtk': 'spa',
    #     'SpDef': 'spd',
    #     'Speed': 'spe'
    conv = {
          'HP': 'hp',
          'Atk':'attack',
          'Def': 'defense',
          'SpAtk': 'special-attack',
          'SpDef': 'special-defense',
          'Speed': 'speed'
        }
    def getStat(payload, stat):
      stat = conv[stat]
      for o in payload:
        if o['stat']['name'] == stat:
          return { "base": o['base_stat'], "name": o['stat']['name'] }
        else:
          pass
    for stat in ['HP','Atk','Def','SpAtk','SpDef','Speed']:
      c.execute(f"SELECT {stat+'iv'} FROM pokeiv WHERE ID = ?",(pokeId,))
      iv = c.fetchone()[0]
      l = other.reqJSON("https://pokeapi.co/api/v2/pokemon/"+pokemon)['stats']
      baseStat = getStat(l, stat)["base"]
      pokeManage.statsCalc(0, iv, baseStat, other.naturegen(synch), stat, lvl, pokeId)
    ability = pokeManage.abilitygen(pokemon)
    o = ability
    ability = random.choice(ability[0])
    ability = random.choice((ability, pokeManage.abilitygen(pokemon)[1], random.choice(o[0]))).capitalize()
    c.execute("""
      INSERT INTO userpoke(
        user_id,
        pokemon,
        mon_id
      ) VALUES (
        ?,?,?
      )
    """,(owner_id,pokemon,pokeId)) 
    commit()
    c.execute("""
      INSERT INTO pokestats(
        ID,
        Nature,
        Ability,
        Level,
        EXP,
        Moves
      ) VALUES (
        ?,?,?,
        ?,?,?
      )
    """,(pokeId, other.naturegen(synch), ability, lvl, int((50*50)/2)^(3)*int((lvl/2)), str(
      [
        "Tackle",
        "Tackle",
        "Tackle",
        "Tackle"
      ]
    )))
    commit()
    close()
    return other.success("createPokemon")

    



