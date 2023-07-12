#!/bin/sh

# Importiere Daten in die MongoDB-Datenbank sammlung
# Verwende das JSON-Array-Format für die Importdatei /data/data.json
mongoimport --jsonArray --db sammlung --collection countries --file /data/data.json
