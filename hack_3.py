"""
generic script

a = @
e = 3
i = ¡
o = 0
u = v

text: "fooziman" output => "F00z¡m@N" 
text: "barziman" output => "B@rz¡m@N" 
text: "3q" output => "3Q" 
text: "qu" output => "Qv" 
text: "qux" output => "QvX" 
"""


def fn_hack_3(result):
     result = result.capitalize()[:-1] + result[-1].upper()
     result = result.replace("a", "@").replace("e", "3").replace("i", "¡").replace("o", "0").replace("U","v").replace("u", "v")
     return result

print(fn_hack_3("qu"))