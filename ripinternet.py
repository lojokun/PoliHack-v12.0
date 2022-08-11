import requests
import json


def main():
    ids = requests.get('https://inspectorulpadurii.ro/api/aviz/locations').json()['codAviz']
    mainurl = 'https://inspectorulpadurii.ro/api/aviz/'
    filename = 'rip.json'
    listthing = []
    num = 1
    for code in ids[::-1]:
        try:
            url = mainurl + code
            data = requests.get(url).json()
            listthing.append(data)
            open(filename, 'w+').write(json.dumps(listthing))
            print('wrote new truck: ' + str(num))
            num += 1
        except Exception as e:
            print(str(e))
            pass

main()
