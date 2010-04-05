from itertools import combinations 

import pyximport; pyximport.install()
import titan_helpers

iterations = 1000000

creatures = {
             'archangel': (9, 4),
             'angel/titan/unicorn': (6, 4),
             'behemoth': (8, 3),
             'centaur': (3, 4),
             'colossus': (10, 4),
             'cyclops': (9, 2),
             'dragon': (9, 3),
             'gargoyle': (4, 3),
             'giant': (7, 4),
             'gorgon/warbear': (6, 3),
             'griffon/warlock': (5, 4),
             'guardian':  (12, 2),
             'hydra': (10, 3),
             'lion': (5, 3),
             'minotaur/ranger': (4, 4),
             'ogre': (6, 2),
             'serpent': (18, 2),
             'troll': (8, 2),
             'wyvern': (7, 3),
}

for c1, c2 in list(combinations(sorted(creatures), 2)) + list(zip(sorted(creatures), sorted(creatures))):
  c1v = creatures[c1]
  c2v = creatures[c2]
  kills, deaths = titan_helpers.titan_battle_simulate(c1v[0], c1v[1], c2v[0], c2v[1], iterations)
  print c1, c2, (100.0 * kills / float(iterations)), (100.0 * deaths / float(iterations))


