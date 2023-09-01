### Zadatak 4. Pozitivan ceo broj x veći od 2 je prost ako u intevalu [2, x ] ne postoji ni jedan broj koji x
### deli bez ostatka. Napiši funkciju koja proverava da li je broj prost. Funkcija treba da primi broj za koji se
### proverava da li je prost, a da vrati True ako jeste, a False ako nije.
### Primer izvršavanja programa:
### >>> print(prostBroj(127))
### True
### >>> print(prostBroj(123))
### False
import math

def prostBroj(x):
    for i in range(2, int(math.sqrt(x))+1):
        if x % i == 0:
            return False
    return True

print(prostBroj(127))
print(prostBroj(123)) 