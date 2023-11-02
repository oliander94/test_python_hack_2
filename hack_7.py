"""
generic script

["1",2] => type string & type int
[0] => type int

text: ["a","b","c","d","e"] output => ["1",2,"3",4,"5"]
text: [] output => [0] 
"""


def fn_hack_7(result):
    if result == [0]: return result
    for k in range(len(result)):
        if (k+1) % 2 == 0: result[k] = k+1 
        else: result[k] = str(k+1)
    return result