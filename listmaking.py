import json

def main():
    data = json.loads(open('rip.json').read().split('\n')[0])
    with open('nr_matriculare.txt', 'w') as f:
        for transport in data:
            print("Plate number registered.")
            f.write(transport['nrIdentificare'] + "\n")


main()