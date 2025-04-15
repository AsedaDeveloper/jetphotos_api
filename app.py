
from flask import Flask, request, jsonify
from scraper import scrape_jetphotos

app = Flask(__name__)

@app.route('/search', methods=['GET'])
def search():
    reg = request.args.get('reg')
    aircraft_type = request.args.get('type')
    airline = request.args.get('airline')
    serial = request.args.get('serial')

    results = scrape_jetphotos(reg, aircraft_type, airline, serial)
    return jsonify({'results': results})

if __name__ == '__main__':
    app.run(debug=True)
