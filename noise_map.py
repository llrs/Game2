
# Code from the web: http://www.redblobgames.com/articles/noise/introduction.html
mapsize  =  20
noise_  =  list(range(1,10))
from noise import * # Some functions to plot like maps
from numpy import mean
import random

# Functions to generate noise in 1D
# TODO: Generate noise functions for 2D
# TODO: See this answer http://gamedev.stackexchange.com/a/23705/41425
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
