from flask import Flask, render_template, jsonify

app = Flask(__name__)
FREIGHTS = [{
    'id': 1,
    'title': 'Local-Local',
    'location': 'Pennsylvania',
    'destination': 'Anywhere in this area'
}, {
    'id':
    2,
    'title':
    'Regional',
    'location':
    'From State to State',
    'destination':
    'New York, California, Florida, Texas, Washington DC, Ohio'
}, {
    'id':
    3,
    'title':
    'air freight, ground freight, ocean freight, and rail  freight',
    'location':
    'International',
    'destination':
    'Affrican Countries, United State of America, European'
}]


@app.route("/")
def hello_world():
  return render_template('home.html',
                         freights=FREIGHTS,
                         compagny_name='BACHIR FREIGHT LLC')


@app.route("/api/freights")
def list_freights():
  return jsonify(FREIGHTS)


if __name__ == '__main__':
  app.run(host='0.0.0.0', debug=True)
