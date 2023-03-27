import math
"Simpele wiskundige berekeningen"
"_______________________________________________________________________________________________________________________"
"Vermenigvuldigen"
print(7 * 6)
"Machtsverheffing"
print(2 ** 3)
"haakjes"
print((2+4)*(9-2))
"Goneometrische functies: hier 60 keer de sinus van pi op 4"
print(60 * math.sin(math.pi / 4))
"_______________________________________________________________________________________________________________________"
"Soorten variabelen"
a = "bla"
print((type(a)))
a = 42.5
print((type(a)))
a = True
print((type(a)))
"Getal dat niet een integer vormt tot een integer omvormen"
mijn_variabele = 127 / 3
print(mijn_variabele)
mijn_variabele = 127 // 3
print(mijn_variabele)
"_______________________________________________________________________________________________________________________"
"Speciale waarden"
a = math.inf
print(a)
a = math.nan
print(a)
"_______________________________________________________________________________________________________________________"
"Vergelijkingsoperatoren"
print(5 == 5)
print(5 != 5)
print(5 > 5)
print(5 < 5)
print(5 >= 5)
print(5 <= 5)
"_______________________________________________________________________________________________________________________"
"If statements"
if 5 == 5:
    print('5 is gelijk aan 5')

if 5 != 5:
    print('5 is niet gelijk aan 5')
else:
    print('5 is gelijk aan 5')

if 5 > 5:
    print('5 is groter dan 5')
elif 5 < 5:
    print('5 is kleiner dan 5')
else:
    print('5 is gelijk aan 5')
"_______________________________________________________________________________________________________________________"
"For loops"
# [a, b, c] is een list. Een list is een iterable zoals in Java.
for i in ['a', 'b', 'c']:
    print(i, end=' ')

print()
for i in range(5):
    print(i, end=' ')

print()
for i in range(5, 10):
    print(i, end=' ')

print()
for i in range(5, 10, 2):
    print(i, end=' ')

print()
for i in range(10, 5, -1):
    print(i, end=' ')


