"""
text: {"foo":"fookziman","bar":"barziman"} output => {"Foo":"Fooziman"}
"""


def fn_hack_9(result):
    return solution(result)

def solution(dic):
    dic.pop("bar")
    dic["Foo"] = delete_letter(dic["foo"], "k").capitalize()
    dic.pop("foo")
    return dic

def delete_letter(string, letter):
    newString = ''.join([letra for letra in string if letra != letter])
    return newString