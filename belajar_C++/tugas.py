GPegawai = 2
GPok = 5000000
TjAnak = 10/100
TjSuami = 15/100

def hitung(GPok,TjAnak,TjSuami):
    return GPok+(GPok+TjAnak)+(GPok*TjSuami)

print(f'Total = {hitung(GPok,TjAnak,TjSuami)}')