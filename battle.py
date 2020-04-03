import pokebase as pb
import json
import math

def weakness(attack, defense):
    if type(defense) == list:
      total = 0
      y = []
      #print(defense) 3##333#
      for x in defense:
        #print(x)
        atk_type = pb.type_(attack)
        #print(atk_type)

        # Check which damage_relation list the defense is in. Matches by name
        if x in [t["name"] for t in atk_type.damage_relations.no_damage_to]:
            return 0.0
        elif x in [t["name"] for t in atk_type.damage_relations.half_damage_to]:
            total += 0.5
            y.append(0.5)
        elif x in [t["name"] for t in atk_type.damage_relations.double_damage_to]:
            total += 2.0
            y.append(2.0)
        else:
            total += 1.0
            y.append(1.0)
        #print(total)
      if total == 3.0 or 2.5:
        total = 2.0
      if y[0] == 1.0 and y[1] == 1.0:
        total = 1.0
      elif y[0] == 0.5 and y[1] == 0.5:
        total = 0.25
      if y[0] == 2.0 and y[1] == 2.0:
        total = 4.0
      if(
        y[0] == 1.0 and y[1] == 0.5 or
        y[0] == 0.5 and y[1] == 1.0
      ):
        total = 0.5
      if(
        y[0] == 2.0 and y[1] == 0.5 or
        y[0] == 0.5 and y[1] == 2.0
      ):
        total = 1.0
      
      return total
    else:

      atk_type = pb.type_(attack)


      if defense in [t["name"] for t in atk_type.damage_relations.no_damage_to]:
          return 0.0
      elif defense in [t["name"] for t in atk_type.damage_relations.half_damage_to]:
          return 0.5
      elif defense in [t["name"] for t in atk_type.damage_relations.double_damage_to]:
          return 2.0
      else:
          return 1.0

def damageCalc(attack, defense, level, movePower, stab, param, targets, weather=None):
  import random
  def conditions():
    payload = {
      'fire':{
        'good':'sun',
        'bad': 'rain',
        'immune': 'heavy rain'
      },
      'water':{
        'good':'rain',
        'bad': 'sun',
        'immune': 'harsh sun'
      }
    }
    if weather:
      if payload[param['moveType']]['bad'] == weather:
        return 0.5
      elif payload[param['moveType']]['immune'] == weather:
        return 0
      elif payload[param['moveType']]['good'] == weather:
        return 1.5
      else:
        return 1
    else:
      return 1

        
    
  def crit():
    if random.randint(int(10),int(15)) == 15:
      return 1.5
    else:
      return 1

  floor = math.floor
  # Stab is a boolean
  if stab:
    stab = 1.5
  else:
    stab = 1
  def ran():
    ye = str(random.randint(85, 100))
    if len(ye) == 3:
      return 1.0
    else:
      return float('0.'+ye)

  mods = targets*conditions()*crit()*ran()*stab*weakness(param['moveType'], param['defenseType'])


  """=damage = floor(
    (((((2 * level / 5)+2) 
    * movePower * attack/defense)/50)+2)*mods
  )
  return damage"""



#attack, defense, level, movePower, stab, param, targets, weather=None

"""print(damageCalc(
  317,
  207,
  100,
  110,
  True,
  {
    'moveType': 'fire',
    'defenseType': [
      'grass',
      'ice'
    ]
  },
  1,
  'sun'
))


"""