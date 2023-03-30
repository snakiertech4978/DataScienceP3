# Sturges
m = math.ceil(1 + math.log2(n))
print(f'm = {m}')

from statistics import stdev

# Scott
b = 3.5 * stdev(diskspace) / (n ** (1 / 3))
m = math.ceil((diskspace.max() - diskspace.min()) / b)
print(f'm = {m}')

# Excel
m = math.ceil(math.sqrt(n))
print(f'm = {m}')

