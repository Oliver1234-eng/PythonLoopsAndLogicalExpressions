### Zadatak 2. Koristeći while petlju napiši funkciju koji određuje koliko godina treba da prođe dok se u
### uloženi novac u banku ne udvostruči. Funkcija kao parametar prima kamatnu stopu na godišnjem nivou,
### a vraća broj godina.
### Primer izvršavanja programa:
### >>> print(brojGodina(0.04))
### 18
def brojGodina(kamatna_stopa):
    ulog = 1 
    godine = 0 

    while ulog < 2:  
        ulog = ulog * (1 + kamatna_stopa) 
        godine += 1  

    return godine

print(brojGodina(0.04))