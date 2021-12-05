import requests
import json
from datetime import *
from django.shortcuts import render
from django.http import HttpResponse

from harta.models import *


def populate_aviz(request):
    mainurl = 'https://inspectorulpadurii.ro/api/aviz/'
    ids = ["AP21005095000300505212010929", "DC21000489000700665912021258", "AP21002598002601401412031343",
           "DC21007682000701690012021512", "AP21005095000300505212010929"]

    for id in ids:
        url = mainurl + id
        req = requests.get(url)
        data = req.json()
        count = 1
        data_emitere = data['valabilitate']['emitere']
        data_finalizare = data['valabilitate']['finalizare']
        nume_sortiment = data['volum']['volumSpecie'][0]['volumSortiment'][0]['numeSortiment']
        volum = data['volum']['total']

        utc_time = datetime.fromtimestamp(float(data_emitere) / 1000, timezone.utc)
        local_time = utc_time.astimezone()
        print(local_time.strftime("Data emiterii: %d-%m-%Y %H:%M:%S (%Z)"))

        utc_time = datetime.fromtimestamp(float(data_finalizare) / 1000, timezone.utc)
        local_time = utc_time.astimezone()
        print(local_time.strftime("Data finalizarii: %d-%m-%Y %H:%M:%S (%Z)"))

        lemne = Lemne.objects.filter(tipul_lemnului=nume_sortiment)
        lemn = lemne[len(lemne) - 1]

        print(volum)
        print(lemn.densitate)

        masa_calculata = volum * lemn.densitate

        camioane = Camioane.objects.filter(id=count)
        camion = camioane[len(camioane) - 1]

        new_aviz = Aviz.objects.create(id_camion=camion, data_emiterii=data_emitere,
                                       data_finalizarii=data_finalizare, id_lemne=lemn,
                                       volum=volum, masa_calculata=masa_calculata)

        new_aviz.save()

        count += 1

        return HttpResponse(b"")


def render_map(request):
    trucks = Camioane.objects.all()
    data = {}
    data_truck = {}
    count = 1

    for truck in trucks:
        print(truck.nr_matriculare)
        data_truck["nr_matriculare"] = truck.nr_matriculare
        data_truck["latitudine"] = truck.latitudine
        data_truck["longitudine"] = truck.longitudine
        data[f"truck{count}"] = data_truck
        count += 1

    print(data)

    with open("data.json", "w+") as f:
        json.dump(data, f)

    return render(request, "index.html", data)
