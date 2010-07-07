import random

# fancy new Python 2.7 type
from collections import Counter

def test(dice, dormant, magician):
  if magician:
    assert dice + len(dormant) == 6
  else:
    assert dice + len(dormant) == 7

  rolling = dice
  
  # now roll, with an optimal strategy
  aside = Counter()
  while rolling or dormant:
    # roll some dice
    rolled = [random.randint(1, 6) for i in xrange(rolling)]

    # if we have some dice set aside, try for the most common of those
    if len(aside) > 0:
      best = aside.most_common(1)[0][0]
    else:
      best = None

    # if we rolled any best set-aside dice, set those aside and roll again
    if best in rolled:
      cnt = sum(1 for r in rolled if r == best)
      rolling -= cnt
      aside[best] += cnt
    # if we haven't set any aside, and we can set aside a dice
    # that we can bring in later, do that
    elif len(aside) == 0 and set(rolled) & set(dormant):
      s = set(rolled) & set(dormant)
      counter = Counter()
      for x in rolled:
        if x in s:
          counter[x] += 1
      x, cnt = counter.most_common(1)[0]
      aside[x] += cnt
      rolling -= cnt
    # if we can bring in a die that is the best, do that
    elif best in dormant:
      aside[best] += 1
      rolling += sum(1 for r in dormant if r != best)
      dormant = []
    # if we have to set something aside but have nothing, and
    # we still have a magician, then use the magician
    elif best is not None and magician:
      magician = False
      aside[best] += 1
      rolling -= 1
    # we are screwed... set something random aside
    else:
      aside[rolled[0]] += 1
      rolling -= 1

    # if we have something set aside, then just start
    # rolling the other set-aside dice (that aren't
    # the same as that set aside
    best = aside.most_common(1)[0][0]
    rolling += sum(1 for r in dormant if r != best)
    if best in dormant:
      dormant = [best]
    else:
      dormant = []

  # how many of-a-kind did we get?
  score = aside.most_common(1)[0][1] 
  return score

# how many of-a-kind are we going for
target = 6
# tests per configuration
iters = 100000

results = {}
# is a magician better than another named die?
for magician in (False, True):
  # is a farmer better than a named die?
  for farmer in (False, True):
    # we always start with two dice
    # assume we have one more dice than we need
    maxcards = target + 1 - 2
    dice = 2
    # if we have a magician, we take away a die
    if magician:
      maxcards -= 1
    # if we have a farmer, we roll one extra die from the
    # start, but can't bring in a good one later
    if farmer:
      maxcards -= 1
      dice += 1
    dormant = range(1, maxcards + 1)
    trials = []
    for i in xrange(iters):
      score = test(dice, dormant, magician)
      trials.append(score)
    score = sum(1 for s in trials if s == target) / float(len(trials))
    results[(magician, farmer)] = score

# sort the results
for score, (magician, farmer) in sorted([(v,k) for k, v in results.items()]):
  print "Magician = %5s, Farmer = %5s: %.3f%%" % (magician, farmer, score * 100.0)


