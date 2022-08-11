import requests
from datetime import datetime, timezone


def main():
    mainurl = 'https://inspectorulpadurii.ro/api/aviz/'
    ids = ["AP21005095000300505212010929", "DC21000489000700665912021258", "AP21002598002601401412031343",
           "DC21007682000701690012021512", "AP21005095000300505212010929"]

    for id in ids:
        url = mainurl + id
        req = requests.get(url)
        data = req.json()
        data_emitere = data['valabilitate']['emitere']
        data_finalizare = data['valabilitate']['finalizare']

        utc_time = datetime.fromtimestamp(float(data_emitere) / 1000, timezone.utc)
        local_time = utc_time.astimezone()
        print(local_time.strftime("Data emiterii: %d-%m-%Y %H:%M:%S (%Z)"))

        utc_time = datetime.fromtimestamp(float(data_finalizare) / 1000, timezone.utc)
        local_time = utc_time.astimezone()
        print(local_time.strftime("Data finalizarii: %d-%m-%Y %H:%M:%S (%Z)"))

        new_aviz = Aviz.objects.create()


main()
