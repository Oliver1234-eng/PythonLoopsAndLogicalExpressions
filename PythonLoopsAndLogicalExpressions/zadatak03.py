### Zadatak 3. Sekvenca Sirakuza se računa počevši od prirodnog broja x kao:
### xi+1 = xi/2 ako je xi parno, a xi+1 = 3xi + 1 ako xi je neparno.
### Napiši funkciju koja prima inicijalnu vrednost x i vraća listu sa Sirakuza sekvencom za tu vrednost.
### Primer izvršavanja programa:
### >>> print(sirakuza(5))
### [5, 16, 8, 4, 2, 1]
def sirakuza(x):
    sirakuza_lista = [x] 
    
    while x != 1: 
        if x % 2 == 0:
            x = x // 2  
        else:
            x = 3 * x + 1 
        sirakuza_lista.append(x)  
    
    return sirakuza_lista

print(sirakuza(5))  