import json
import csv
from sets import Set

li = Set()

if __name__ == '__main__':

    with open('names22.csv', 'w') as csvfile:
        fieldnames = ['source', 'target']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()

        with open("./data/urban-dictionary-corpus.json", mode='r') as in_file:
            for l in in_file.readlines():
                data = json.loads(l)
                if "list" in data:
                    if len(data["list"]) > 0:
                        tmp = data["list"][0]["word"].lower().replace(",","").replace("/","").replace(" ","-")
                        if "list" in data:
                            if len(data["list"]) > 0:
                                for w in data["tags"]:
                                    if len(w) > 0 and len(data["list"][0]["word"]) > 0:
                                        try:
                                            tm = w.lower().replace(",","").replace("/","").replace(" ","-")
                                            writer.writerow({"source": tmp,"target":tm})
                                        except Exception as e:
                                            print e
