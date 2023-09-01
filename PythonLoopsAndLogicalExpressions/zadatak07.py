### Zadatak 7. Napiši program za registrovanje novih proizvoda u prodavnici. Kada se program pokrene
### prodavcu omogućuje jedino da se prijavi na sistem. Prilikom prijavljivanja na sistem prodavac unosi
### korisničko ime i lozinku. Nakon što se uspešno prijavio na sitem, prodavac može da doda novi proizvod,
### pri čemu unosi naziv, cenu i raspoloživu količinu proizvoda. Nakon što je dodat novi proizvod ispisuje se
### spisak svih proizvoda u prodavnici. Dodavanje proizvoda se ponavlja dok prodavac ne unese „quit“.
### Ukoliko prodavac unese „quit“ bilo za naziv, cenu ili količinu proizvoda, prekida se izvršavanje programa.
### Korisnička imena i lozinke čuvaju se u fajlu prodavci.txt, a nazivi, cene i količine proizvoda čuvaju se u
### fajlu proizvodi.txt.
import csv

# funkcija za prijavljivanje na sistem
def prijava():
    with open('prodavci.txt', mode='r') as f:
        reader = csv.reader(f)
        korisnici = {rows[0]:rows[1] for rows in reader}
    while True:
        korisnicko_ime = input('Unesite korisnicko ime: ')
        lozinka = input('Unesite lozinku: ')
        if korisnicko_ime in korisnici and korisnici[korisnicko_ime] == lozinka:
            print('Uspesno ste se prijavili na sistem.')
            return True
        else:
            print('Pogresno korisnicko ime ili lozinka. Pokusajte ponovo.')

# funkcija za dodavanje novog proizvoda
def dodaj_proizvod():
    with open('proizvodi.txt', mode='a', newline='') as f:
        writer = csv.writer(f)
        while True:
            naziv = input('Unesite naziv proizvoda (ili "quit" za prekid): ')
            if naziv == 'quit':
                break
            cena = input('Unesite cenu proizvoda (ili "quit" za prekid): ')
            if cena == 'quit':
                break
            kolicina = input('Unesite kolicinu proizvoda (ili "quit" za prekid): ')
            if kolicina == 'quit':
                break
            writer.writerow([naziv, cena, kolicina])
    print('Novi proizvod je uspesno dodat.')

# funkcija za ispisivanje spiska svih proizvoda
def ispisi_proizvode():
    with open('proizvodi.txt', mode='r') as f:
        reader = csv.reader(f)
        for row in reader:
            print(row[0] + ', ' + row[1] + ' din, ' + row[2] + ' kom')

# glavni program
if prijava():
    while True:
        print('Izaberite opciju:')
        print('1. Dodaj novi proizvod')
        print('2. Ispisi spisak svih proizvoda')
        print('3. Izlaz')
        opcija = input('Unesite opciju (1, 2 ili 3): ')
        if opcija == '1':
            dodaj_proizvod()
        elif opcija == '2':
            ispisi_proizvode()
        elif opcija == '3':
            break
        else:
            print('Pogresna opcija. Pokusajte ponovo.')
            print('Hvala na koriscenju programa.')
            quit()