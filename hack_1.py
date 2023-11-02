"""
generic script

text: "fooziman" output => "fOozIman" 
text: "qux" output => "qUx" 
text: "eq" output => "eq" 
"""


def fn_hack_1(palabra):
    if len(palabra) <= 2:
        return palabra
    else:
        palabra = palabra[0] + palabra[1].upper() + palabra[2:]
        if len(palabra) >= 5:
            palabra = palabra[:4] + palabra[4].upper() + palabra[5:]
            return palabra
        else:
            return palabra