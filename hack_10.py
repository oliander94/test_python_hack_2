"""
text: [{"a":"b"},{"c","d"},{"e":"f"}] output => [{"1":"2"},{"3","4"},{"5":"6"}]
"""


from pluggy import Result


def fn_hack_10(result):
    return solution(result)


def solution(arrayElements):
    letters = "abcdef"
    answer = []
    for dic in arrayElements:
        if isinstance(dic, dict):
            key = dic.keys()
            for k in key:
                value = dic[k]
                answer.append({str(letters.index(str(k)) + 1): str(letters.index(str(value)) + 1)})
        else:
            data1,data2 = dic
            answer.append({str(letters.index(str(data1)) + 1) , str(letters.index(str(data2)) + 1)})
    return answer