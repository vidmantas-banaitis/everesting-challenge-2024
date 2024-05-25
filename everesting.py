from __future__ import annotations

import math
from typing import TypedDict, NotRequired

# Description: Everesting challenge
f = 'duomenys.txt'
everest = 8848  # Everestas


class Data(TypedDict):
    name: str
    elevation: int  # aukštis nuo jūros lygio
    length: int  # atkarpos ilgis
    ascending: NotRequired[int]  # skirtumas nuo sekančios atkarpos
    angle: NotRequired[int]  # pakilimo kampas


class Node(TypedDict):
    data: Data
    next: Node


class Result(TypedDict):
    A: int  # Vieno rato bendras vertikalus pakilimas
    B: int  # Ratų skaičius įveikti dvigubą Everestą
    Cl: int  # viso rato ilgis
    Ck: int  # kilimo atkarpų ilgis
    Dn: str  # stačiausios atkarpos pavadinimas
    Dk: int  # stačiausios atkarpos pakilimo kampas laipsniais


def read_data(filename) -> Node:
    top: Node | None = None
    it = top

    with open(filename, 'r') as file:
        for line in file:
            row = line.split()
            # print(row)
            n = {'data': {'name': row[0],
                          'elevation': int(row[1]),
                          'length': int(row[2])
                          }, 'next': top}
            if top is None:
                top = n
                it = top
            else:
                it['next'] = n
                it = n

    assert top is not None, "File is empty"
    return top


def calculate(head):
    A = 0  # Vieno rato bendras vertikalus pakilimas
    B = None  # Ratų skaičius įveikti dvigubą Everestą
    Cl = 0  # viso rato ilgis
    Ck = 0  # kilimo atkarpų ilgis
    Dn = ''  # stačiausios atkarpos pavadinimas
    Dk = 0  # stačiausios atkarpos pakilimo kampas laipsniais
    it = head
    while True:
        Cl += it['data']['length']
        it['data']['ascending'] = it['next']['data']['elevation'] - it['data']['elevation']
        it['data']['angle'] = round(math.degrees(math.asin(it['data']['ascending'] / it['data']['length'])))
        if it['data']['ascending'] > 0:
            A += it['data']['ascending']
            Ck += it['data']['length']
        if it['data']['angle'] > Dk:
            Dk = it['data']['angle']
            Dn = it['data']['name']
        # print(it['data'])
        if it['next'] is head:
            break
        it = it['next']
    B = math.ceil((2 * everest) / A)
    return Result(A=A, B=B, Cl=Cl, Ck=Ck, Dn=Dn, Dk=Dk)


def main():
    head = read_data(f)

    data = calculate(head)

    print(f"A: {data['A']}")
    print(f"B: {data['B']}")
    print(f"C: {data['Cl']} {data['Ck']}")
    print(f"D: {data['Dn']} {data['Dk']}")


if __name__ == "__main__":
    main()
