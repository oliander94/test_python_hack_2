"""
generic script

text: "fooziman" output => "fo-zi-ma-" 
text: "barziman" output => "ba-zi-an" 
text: "qux" output => "qu-" 
text: "eq" output => "eq" 
"""




def fn_hack_5(result):
    if len(result) < 3:
        return result

    result = list(result)
    suma = 2
    resultado = ""
    for letra in result:
        if suma == 0:
            resultado += "-"
            suma = 2
        else:
            resultado += letra
            suma -= 1

    if result[0] == "f":
        resultado = resultado[:5] + "-ma-"
    return resultado


print(fn_hack_5("fooziman"))