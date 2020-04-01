class storyline:
  def __init__(self):
    self.cdn = "./UltraDB/"
    import json
    with open(self.cdn+"npc.json") as self.jsonOBJ:
      self.npc = json.load(self.jsonOBJ)
      del self.jsonOBJ

    def write(self):
      with open(self.cdn+"npc.json") as fp:
        json.dump(fp, self.npc, indent=4)

  class npc:
    def makeNpc(self, data):
      """ Data should look something like this name, X, Y, Map, team(list format with json ojects inside, stats must be preCalced), ID or in json format Example: {\n\t
        \tName: "Random Pokemon Name"\n
        \tX: 0,\n
        \tY: 0,\n
        \tMap: "Random town/route/map name",\n
        \tteam: [\n\t
          
        \t]

      }
      """
      
      
      

  class story:
    def __init__(self, user):
      self.user = dict(user)
      if self.user['Region']
    

