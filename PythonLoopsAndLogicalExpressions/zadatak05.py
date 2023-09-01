### Zadatak 5. Napiši funkciju koja prima prirodni broj n, a vraća listu koja sadrži sve proste brojeve koji su manji od n.
### Primer izvršavanja programa:
### >>> print(prostiBrojevi(20))
### [1, 2, 3, 5, 7, 11, 13, 17, 19]
import math

def prostBroj(x):
    for i in range(2, int(math.sqrt(x))+1):
        if x % i == 0:
            return False
    return True

def prostiBrojevi(n):
    prosti = []
    for i in range(2, n):
        if prostBroj(i):
            prosti.append(i)
    
    return prosti

print(prostiBrojevi(20))