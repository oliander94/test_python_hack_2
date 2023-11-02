"""
generic script

["1","-"] => type string
["0"] => type string

text: ["a","b","c","d","e"] output => ["1","-","3","-","5"]
text: [] output => ["0"] 
"""


def fn_hack_6(result):
    if result == []: return ["0"]
    for k in range(len(result)):
        if (k+1) % 2 == 0: result[k] = "-" 
        else: result[k] = str(k+1)
    return result
print(fn_hack_6(["a","b","c","d","e"]))