"Python Lists Basic Comands"
"_______________________________________________________________________________________________________________________"
"Normale list"
x = [3, 4, 5, 6, 7, 8, 9, 10]
print(x)
"Lengte list"
print(len(x))
"Ranges"
x = list(range(3,11))
print(x)
"Optellen of concateneren"
y = x + [11, 12, 13]
print(y)
"Vermenigvuldigen = herhalen"
x = [1, 2, 3]
print(x * 3)
"Lists mogen verschillende waarden van verschillende types bevatten"
x = [42, 3.14, "hallo", True]
print(x)
"_______________________________________________________________________________________________________________________"
"Info uit lists halen"
print(x[0])
"Eerste element"
print(x[-1])
"Laatste element"
"_______________________________________________________________________________________________________________________"
'Slicing'
print(x[1:4])
"elementen 1 tot en met 3"
print(x[1:4:2])
"1 tot en met 3, maar we vergeten 2"
print(x[::2])
"elementen 0 en 2"
print(x[::-1])
"Print alles achterstevoren"
