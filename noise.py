#!/usr/bin/env python3
#-*- encoding: utf-8 -*-

import random
import math
import atexit as _atexit
import os as _os

output_style = 'text'
if 'ORG_BXML' in _os.environ: output_style = 'svg'
mapsize = 60


def text_chart(array, min_y=None, max_y=None):
    BARS = "▁▂▃▄▅▇█"
    if min_y is None: min_y = min(array)
    if max_y is None: max_y = max(array)
    array = [int(6 * (y-min_y) / (max_y-min_y)) for y in array]
    return "".join([BARS[y] for y in array])

    
def svg_chart(array, min_y=None, max_y=None):
    W = 9
    if min_y is None: min_y = min(array)
    if max_y is None: max_y = max(array)
    array = [(1.5 + 14 * (y - min_y) / (max_y - min_y)) for y in array]
    def line(x, y):
        return """L %.1f %.1f l %d 0 """ % (
            1 + W*x, 17-y, W
        )

    y0 = 1.5 + 14 * (-min_y) / (max_y - min_y) # fill to y=0 position
    y0 = 1.5 # fill to bottom of diagram
    
    return """<svg width="%d" height="17"><path d="M 1 %.1f %s L %.1f %.1f"/></svg><br />""" % (
        2 + W*len(array),
        17 - y0,
        "".join([line(x, array[x]) for x in range(len(array))]),
        1 + W*len(array), 17 - y0
    )


chart = {'text': text_chart, 'svg': svg_chart}[output_style]

if output_style == 'svg':
    print('<figure>')
    _atexit.register(lambda: print('</figure>'))

    
def print_chart(i, array):
    print(i, chart(array))

    
def weighted_sum(amplitudes, noises):
    output = [0.0] * mapsize  # make an array of length mapsize
    for k in range(len(noises)):
        for x in range(mapsize):
            output[x] += amplitudes[k] * noises[k][x]
    return output

    
def noise(freq):
    phase = random.uniform(0, 2*math.pi)
    return [math.sin(2*math.pi * freq*x/mapsize + phase) for x in range(mapsize)]

    
def random_ift(rows, amplitude):
    for i in range(rows):
        random.seed(i)
        frequencies = range(1, mapsize//2)
        amplitudes = [amplitude(f) for f in frequencies]
        noises = [noise(f) for f in frequencies]
        sum_of_noises = weighted_sum(amplitudes, noises)
        print_chart(i, sum_of_noises)
