import pygame
import networkx as nx

# graph = {1 : [2,3,6], 2:[1], 3:[1], 4:[5], 5:[7,6], 6:[1,5,7], 7:[6]}
# marked = ()
a = ['##########',
     '#00000000#',
     '#00000000#',
     '###000000#',
     '#00000000#',
     '#000##000#',
     '#00000000#'
     '##########']

class Map:
     def __init__(self, map):
          self.map = map
          self.width = len(self.map[0])
          self.height = len(self.map)
          self.G = nx.Graph()

     def init_graph(self):
          for y in range(1, self.height):
               for x in range(1, self.width - 1):
                    if self.map[y][x] == '#' and self.map[y-1][x] == self.map[y-2][x] == '0':
                         pos = (y, x)
                         if pos not in self.G.nodes:
                              self.G.add_node(pos)
          nodes = self.G.nodes
          for node in self.G.nodes:
               x, y = node[1], node[0]

               if (x-1, y) in nodes:
                    self.G.add_edge((y, x), (y, x - 1), {'air_connected' : False})
               else:

               if (x+1, y) in nodes:
                    self.G.add_edge((y, x), (y, x + 1), {'air_connected' : False})

