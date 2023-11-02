"""
generic script

text: ["a","b","c","d","e"] output => ["e-5","d-4","c-3","b-2","a-1"]
text: ["a","b","c"] output => ["c-3","b-2","a-1"]
text: ["a","b","c","d"] output => ["4","3","2","1"]
text: ["a","b"] output => ["2","1"]
"""


def fn_hack_8(result):
    if len(result) % 2 == 0:
        result = [str(k) for k in range(len(result), 0, -1)]
    else:
        result = [(result[k-1] + "-" + str(k)) for k in range(len(result), 0, -1)]
    return result