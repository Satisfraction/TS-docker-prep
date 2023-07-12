import os
from pymongo import MongoClient
from flask import Flask, jsonify, render_template
from dotenv import load_dotenv

load_dotenv()

# Verbindung zur MongoDB herstellen
def get_mongo_connection():
    # MongoDB URL und Datenbankname aus der Umgebungsvariable lesen
    mongo_url = os.getenv("MONGO_URL")
    database_name = os.getenv("DATABASE_NAME")

    # Verbindung zur MongoDB herstellen
    client = MongoClient(mongo_url)
    db = client[database_name]
    collection = db['countries']
    return collection

app = Flask(__name__)

@app.route('/')
def index():
    # Die Startseite rendern
    return render_template('index.html')

@app.route('/informationen', methods=['GET'])
def get_informationen():
    # Informationen aus der Datenbank abrufen
    collection = get_mongo_connection()
    dokumente = collection.find()

    # Informationen in JSON-Format konvertieren und zurückgeben
    informationen = [{
        'name': dokument['name'],
        'bronze': dokument['bronze'],
        'silber': dokument['silber'],
        'gold': dokument['gold'],
        'gesamt': dokument['gesamt']
    } for dokument in dokumente]

    return jsonify(informationen)

if __name__ == '__main__':
    # Die Flask-Anwendung starten
    app.run(debug=True, host='0.0.0.0', port=3000)
