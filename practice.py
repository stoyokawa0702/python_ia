
dic = {
    '水':'water',
    '火':'fire',
    '風':'wind',
    1:'one',
    (1,1,1):6,
    (6,6,6):3
}

dic['水'] = 'abc'

print(dic['水'])
print(dic[1])
print(dic[(1,1,1)])



