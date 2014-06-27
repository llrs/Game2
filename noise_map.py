# This module will provide the functions needed to generate a good map
# It is used in Place.Maping()
# The initial idea come from:
# http://stackoverflow.com/a/23879739/2886003

# Problems
# I need that some set of options to be more common than other
# I need to set some rules that two rivers together canno't be (in parallel)
# I need a 2D map not a 1D map

#mapsize  =  20
#noise_  =  list(range(1,10))
from noise import * # Some functions to plot like maps
from numpy import mean
import random
import math

# Functions to generate noise in 1D
# TODO: Generate noise functions for 2D
# FROM http://gamedev.stackexchange.com/a/23705/41425
# Addresses to generate images

##perm = list(range(256))
##random.shuffle(perm)
##perm += perm
##dirs = [(math.cos(a * 2.0 * math.pi / 256),
##         math.sin(a * 2.0 * math.pi / 256))
##         for a in range(256)]

def noise(x, y, per):
    def surflet(gridX, gridY):
        distX, distY = abs(x-gridX), abs(y-gridY)
        polyX = 1 - 6*distX**5 + 15*distX**4 - 10*distX**3
        polyY = 1 - 6*distY**5 + 15*distY**4 - 10*distY**3
        
        if int(gridX)%per >= len(perm):
            hashed = perm[perm[int(gridX)%per-1] + int(gridY)%per]
            if perm[int(gridX)%per] + int(gridY)%per >= len(perm):
                hashed = perm[perm[int(gridX)%per-1] + int(gridY)%per-1]
        else:
            hashed = perm[perm[int(gridX)%per] + int(gridY)%per]
        grad = (x-gridX)*dirs[hashed][0] + (y-gridY)*dirs[hashed][1]
        return polyX * polyY * grad
    intX, intY = int(x), int(y)
    return (surflet(intX+0, intY+0) + surflet(intX+1, intY+0) +
            surflet(intX+0, intY+1) + surflet(intX+1, intY+1))

def fBm(x, y, per, octs):
    val = 0
    for o in range(octs):
        val += 0.5**o * noise(x*2**o, y*2**o, per*2**o)
    return val

##size = 128
##freq = 1/32.0
##octs = 5
##data = []
##for y in range(size):
##    for x in range(size):
##        value=fBm(x*freq, y*freq, int(size*freq), octs)
##        data.append(value)
##print(data)
# From: http://www.redblobgames.com/articles/noise/introduction.html
# Code is in python
def adjacent(noise):
    """Given a list of values return the integer of the mean between two
       contigous values"""
    output  =  []
    for i in range(len(noise) - 1):
        output.append(int(mean([noise[i],noise[i+1]])))
    return output

def wave(iterations, length):
    """Creates an array of length length with coherent random integers numbers, minimum iterations 2"""
    if iterations ==  None:
        iterations  =  0
    noise  =  [int(random.gauss(8, 4)) for i in range(length+iterations+1)]
    a  =  adjacent(noise)
    if iterations ==  None or iterations == 1:
        return(a)
    for i in range(iterations-1):
        a  =  adjacent(a)
    return(a)

def rougher(noise):
   output  =  []
   for i in range(len(noise) - 1):
      output.append(0.5 * (noise[i] - noise[i+1]))
   return output

def weighted_sum(amplitudes, noises):
   output  =  [0.0] * mapsize  # make an array of length mapsize
   for k in range(len(noises)):
      for x in range(mapsize):
         output[x] +=  amplitudes[k] * noises[k][x]
   return output

##amplitudes  =  [0.2, 0.5, 1.0, 0.7, 0.5, 0.4]
##frequencies  =  [1, 2, 4, 8, 16, 32]

def noise(freq):
   phase  =  random.uniform(0, 2*math.pi)
   return [math.sin(2*math.pi * freq*x/mapsize + phase)
         for x in range(mapsize)]

##for i in range(10):
##   noises  =  [noise(f) for f in frequencies]
##   sum_of_noises  =  weighted_sum(amplitudes, noises)
##   print_chart(i, sum_of_noises)

def random_ift(rows, amplitude):
   for i in range(rows):
      amplitudes  =  [amplitude(f) for f in frequencies]
      noises  =  [noise(f) for f in frequencies]
      sum_of_noises  =  weighted_sum(amplitudes, noises)
      print_chart(i, sum_of_noises)

##random_ift(10, lambda f: 1/f)

##for i in range(8):
##   random.seed(i)
##   noise  =  [random.uniform(-1, +1) for i in range(mapsize)]
##   print_chart(i, rougher(noise))

# From: http://www.fundza.com/c4serious/noise/perlin/perlin.html
##p = list(range(256))
##p += p

def lerp(t, a, b):
    return a + t * (b - a)
  
def fade(t):
    return(t * t * t * (t * (t * 6 - 15) + 10))
  
def grad(hash, x, y, z):
    h = hash & 15
    if h < 8:
        u = x
    else:
        u = y
    if h < 4:
        v = y
    elif h == 12 or h == 14:
        v = x
    else:
        v = z
    if h & 1 != 0:
        u = -u
    if h & 2 != 0:
        v = -v
    return(u + v)
  
def pnoise(x, y, z):
    global p
    X = int(math.floor(x)) & 255
    Y = int(math.floor(y)) & 255
    Z = int(math.floor(z)) & 255
    x -= math.floor(x)
    y -= math.floor(y)
    z -= math.floor(z)
    
    u = fade(x)
    v = fade(y)
    w = fade(z)
    
    A =  p[X] + Y
    AA = p[A] + Z
    AB = p[A + 1] + Z
    B =  p[X + 1] + Y
    BA = p[B] + Z
   BB = p[B + 1] + Z
    
    pAA = p[AA]
    pAB = p[AB]
    pBA = p[BA]
    pBB = p[BB]
    pAA1 = p[AA + 1]
    pBA1 = p[BA + 1]
    pAB1 = p[AB + 1]
    pBB1 = p[BB + 1]
    
    gradAA =  grad(pAA, x,   y,   z)
    gradBA =  grad(pBA, x-1, y,   z)
    gradAB =  grad(pAB, x,   y-1, z)
    gradBB =  grad(pBB, x-1, y-1, z)
    gradAA1 = grad(pAA1,x,   y,   z-1)
    gradBA1 = grad(pBA1,x-1, y,   z-1)
    gradAB1 = grad(pAB1,x,   y-1, z-1)
    gradBB1 = grad(pBB1,x-1, y-1, z-1)
    return lerp(w,
                lerp(v, lerp(u, gradAA, gradBA), lerp(u, gradAB, gradBB)),
                lerp(v, lerp(u, gradAA1,gradBA1),lerp(u, gradAB1,gradBB1)))

# TODO: Check: https://www.6by9.net/simplex-noise-for-c-and-python/
# From: https://code.google.com/p/battlestar-tux/source/browse/procedural/simplexnoise.py
# And the son: https://code.google.com/p/battlestar-tux/source/browse/procedural/simplextextures.py

# From: https://github.com/caseman/noise

# From: https://code.google.com/p/fractalterraingeneration/wiki/Perlin_Noise
