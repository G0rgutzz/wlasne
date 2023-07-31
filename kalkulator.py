"""lista1=[1,2,3]
lista2=[1,2,3]
lista3=[]
i=0
while i <len(lista1):
    suma=lista1[i]+lista2[i]
    lista3.append(suma)
    i=i+1
print(lista3)"""

"iterowanie po słowniku"
d = {"key1": "1", "key2":"2", "key3":"3", "key4":"4", "key5":"5"}

for key, val in d.items():
    print("{} ma wartość {}".format(key, val))

elements = ['first', 'second', 'third']

for i, element in enumerate(elements):
    print(i, element)