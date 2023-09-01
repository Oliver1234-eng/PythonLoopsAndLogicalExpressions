### Zadatak 1. Subjektivni osećaj hladnoće se računa po formuli:
### 3.74+0.6215T-35.75(V0.16)+0.4275T(V0.16)
### gde je T temperatura u stepenima Farenhajta, a V brzina vetra u miljama na sat. Napiši program koji
### ispisuje tabelu subjektivnog osećaja hladnoće za interval temperature i brzine vetra koje unosi korisnik.
### Primer izvršavanja programa:
### >>> napraviTabelu(0,10,5,10)
###           t = 5   t = 6   t = 7   t = 8   t = 9   t = 10
### v = 0     6.848   7.469   8.091   8.712   9.334   9.955
### v = 1   -26.765 -25.716 -24.667 -23.618 -22.569 -21.520
### v = 2   -30.707 -29.608 -28.509 -27.410 -26.311 -25.212
### v = 3   -33.224 -32.093 -30.962 -29.831 -28.700 -27.569
### v = 4   -35.112 -33.957 -32.802 -31.647 -30.491 -29.336
### v = 5   -36.637 -35.463 -34.288 -33.113 -31.939 -30.764
### v = 6   -37.924 -36.733 -35.542 -34.352 -33.161 -31.970
### v = 7   -39.042 -37.837 -36.632 -35.427 -34.222 -33.017
### v = 8   -40.033 -38.816 -37.598 -36.380 -35.162 -33.945
### v = 9   -40.925 -39.696 -38.467 -37.238 -36.009 -34.780
### v = 10  -41.737 -40.498 -39.258 -38.019 -36.780 -35.540
def napraviTabelu(t_min, t_max, t_korak, v_min, v_max, v_korak):
    print("  ", end="")
    for t in range(t_min, t_max+1, t_korak):
        print("t={:<3}".format(t), end="")
    print()
    for v in range(v_min, v_max+1, v_korak):
        print("v={:<2}".format(v), end="")
        for t in range(t_min, t_max+1, t_korak):
            subjektivni_osecaj_hladnoce = 3.74 + 0.6215*t - 35.75*(v**0.16) + 0.4275*t*(v**0.16)
            print("{:>6.3f}".format(subjektivni_osecaj_hladnoce), end="")
        print()

napraviTabelu(0, 10, 1, 0, 10, 1)