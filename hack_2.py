"""
generic script

text: "fooziman" output => "fzmn" 
text: "barziman" output => "brzmn" 
text: "qux" output => "qx" 
"""


def fn_hack_2(result):
    resultado = ""
    for vocal in result:
        if vocal in "aeiou":
            pass
        else:
            resultado += vocal
            
    return resultado