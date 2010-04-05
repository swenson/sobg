import numpy as np

def titan_battle_simulate(int strength1,
                           int level1,
                           int strength2,
                           int level2,
                           int iterations):
  cdef int kills = 0
  cdef int deaths = 0
  cdef int hp1
  cdef int hp2
  cdef int dice1
  cdef int dice2
  cdef int needed1
  cdef int needed2
  # monte carlo simulation
  for i in range(iterations):
    hp1 = strength1
    hp2 = strength2
    dice1 = strength1
    dice2 = strength2
    if level2 == level1:
      needed1 = 4
      needed2 = 4
    elif level2 - level1 == 1:
      needed1 = 5
      needed2 = 3
    elif level2 - level1 >= 2:
      needed1 = 6
      needed2 = 2
    elif level1 - level2 == 1:
      needed1 = 3
      needed2 = 5
    else:
      needed1 = 2
      needed2 = 6
   
    while hp1 > 0 and hp2 > 0:
      for d in np.random.randint(1, 7, dice1):
        if d >= needed1:
          hp2 -= 1
      for d in np.random.randint(1, 7, dice2):
        if d >= needed2:
          hp1 -= 1

    if hp1 <= 0:
      deaths += 1
    if hp2 <= 0:
      kills += 1
  return kills, deaths

