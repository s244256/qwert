#Задание3, вариант 2.
def maximum(mas):
    return mas.index(max(mas))
f = open("text.txt","r")
n = f.readline()
mas = []
while n!="":
    mas.append(float(n))
    n = f.readline()
print(str(min(mas)+max(mas)))
f.close()
print(maximum(mas))