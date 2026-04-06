#!/usr/bin/env python3
# vim: foldmethod=marker foldmarker={{{,}}}

import runpod

ROMAN_DIGITS = ( # {{{
   (1000, "M" ),
   ( 900, "CM"),
   ( 500, "D" ),
   ( 400, "CD"),
   ( 100, "C" ),
   (  90, "XC"),
   (  50, "L" ),
   (  40, "XL"),
   (  10, "X" ),
   (   9, "IX"),
   (   5, "V" ),
   (   4, "IV"),
   (   1, "I" ),
) # }}}

def to_roman(value):  # {{{
    if value < 1 or value > 3999:
       raise ValueError("val must be between 1 and 3999")

    remainder = value
    numerals = []
    for arabic, roman in ROMAN_DIGITS:
        count, remainder = divmod(remainder, arabic)
        numerals.append(roman * count)
        if remainder == 0:
           break
    return ''.join(numerals)
# }}}

def handler(job):  # {{{
    global cnt
    cnt = cnt + 1
    dat = job.get('input', {})
    val = dat.get('val')
    rom = to_roman(val)
    return {
       'roman': rom,
       'cnt'  : cnt
    }
# }}}

cnt = 0
runpod.serverless.start({'handler': handler})
