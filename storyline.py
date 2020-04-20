import json
from theading import Thread

class storyline:
  def __init__(self):
    self.cdn = "./UltraDB/"
    with open(self.cdn+"npc.json") as self.jsonOBJ:
      self.npc = json.load(self.jsonOBJ)
      del self.jsonOBJ

    def write(self):
      while True:
        with open(self.cdn+"npc.json") as fp:
          json.dump(fp, self.npc, indent=4)

  class npc:
    def makeNpc(self, data, npcId):
      """ Data should look something like this name, X, Y, Map, team(list format with json ojects inside, stats must be preCalced), ID or in json format Example: {\n\t
        \tName: "Random Pokemon Name"\n
        \tX: 0,\n
        \tY: 0,\n
        \tmovementType: "randomMove/autoAttack/None"\n
        \tMap: "Random town/route/map name",\n
        \tteam: [\t
          \t\t{\n\t\t\t\tName: "Lugia", Stats: {} Etc Etc\n\t\t\t}\n
        \t],

      }
      """
      if npcId in self.npc:
        return KeyError
      else:
        self.npc[npcId] = {
          'Name': data['Name'],
          'PosistionData': {
            'X': data['X'],
            'Y': data['Y'],
            'Movement': {
              'Name': data['movementType'],
              'maxSteps': None if not 'maxSteps' in data else data['maxSteps']
            },
            'Contact': {
              'Message': data['msg'],
              'Question?': None if not 'question' in data else {
                
              }
          }
        }

      
      
      

  class story:
    def __init__(self, user):
      self.user = dict(user)
    

