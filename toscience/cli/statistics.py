#!/usr/bin/env python3

# dateibasierte Statistik für frl
# 1. Elasticsearch index abfragen
# curl "https://frl.publisso.de/search/frl2/file/_search?size=1000&from=0" -o frl2_file_00.json
# curl "https://frl.publisso.de/search/frl2/file/_search?size=1000&from=1000" -o frl2_file_01.json
# ...
# curl "https://frl.publisso.de/search/frl2/file/_search?size=1000&from=18000" -o frl2_file_18.json
# curl "https://frl.publisso.de/search/frl2/file/_search?size=1000&from=19000" -o frl2_file_19.json
#
# 2. aus den json-Dateien Dateiname, -format und -größe in eine CSV-Datei dumpen
# ./statistics.py ~/Dokumente/FRL/statistics/*.json
#
# 3. CSV in Excel/Librecalc laden und pivot-Tabelle erstellen

import sys
import json
import csv

with open('statistics.csv', 'w', newline='') as csvfile:
    fieldnames = ['id', 'fileLabel', 'format', 'size']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()

    for es in sys.argv[1:]:

        with open(es, "r") as raw:
            data = json.load(raw)
            for hit in data["hits"]["hits"]:
                id = hit["_id"]
                if "hasData" in hit["_source"]:
                    details = hit["_source"]["hasData"]
                    
                    writer.writerow({
                        'id': id,
                        'fileLabel': details["fileLabel"],
                        'format': details["format"],
                        'size': details["size"]
                        })
                else:
                    print("no details for id %s" % id)