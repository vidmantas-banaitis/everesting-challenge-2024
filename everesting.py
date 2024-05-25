import math

# Description: Everesting challenge
f = 'duomenys.txt'
everest = 8848  # Everestas

A = 0  # Vieno rato bendras vertikalus pakilimas
B = 0  # Ratų skaičius įveikti dvigubą Everestą
Cl = 0  # viso rato ilgis
Ck = 0  # kilimo atkarpų ilgis
Dn = ''  # stačiausios atkarpos pavadinimas
Dk = 0  # stačiausios atkarpos pakilimo kampas laipsniais

first = None
it = first

with open(f, 'r') as file:
    for line in file:
        row = line.split()
        # print(row)
        n = {'data': {'name': row[0],
                      'elevation': int(row[1]),
                      'length': int(row[2])
                      }, 'next': first}
        if first is None:
            first = n
            it = first
        else:
            it['next'] = n
            it = n

it = first
while True:
    Cl += it['data']['length']
    it['data']['ascending'] = it['next']['data']['elevation'] - it['data']['elevation']
    it['data']['angle'] = math.degrees(math.atan(it['data']['ascending'] / it['data']['length']))
    if it['data']['ascending'] > 0:
        A += it['data']['ascending']
        Ck += it['data']['length']
    if it['data']['angle'] > Dk:
        Dk = math.ceil(it['data']['angle'])
        Dn = it['data']['name']
    # print(it['data'])
    if it['next'] is first:
        break
    it = it['next']

B = math.ceil((2*everest) / A)
print(f"A: {A}")
print(f"B: {B}")
print(f"C: {Cl} {Ck}")
print(f"D: {Dn} {Dk}")
