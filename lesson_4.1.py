'''def strcounter(string): # сложность O(n**2)
    for symbol in string:
        counter = 0
        for sub_symbol in string:
            if symbol == sub_symbol:
                counter += 1
        print(symbol, '-',counter)

strcounter('abaxcvcxccvcde')

def strcounter(string): # сложность O(n*m)
    for symbol in set(string):
        counter = 0
        for sub_symbol in string:
            if symbol == sub_symbol:
                counter += 1
        print(symbol, '-', counter)

 strcounter('abaxcvcxccvcde')'''

# def strcounter(string): #сложность O(n)
#     syms_counter = {}
#     for symbol in string:
#         syms_counter[symbol] = syms_counter.get(symbol, 0)+1
#     print(syms_counter)
# strcounter('abeaxcvcxccvcd')


word = str(input('Введите слово:'))
a = word[::-1]
if word == a:
    print("True")
else:
    print("False")ls