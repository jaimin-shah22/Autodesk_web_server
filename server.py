import requests
from flask import Flask

app = Flask(__name__)

@app.route("/<debug>")
def get_all_data(debug):
    if debug.lower() == 'true':
        print('Debugging')
    response = requests.get("https://6god8pgyzf.execute-api.us-west-2.amazonaws.com/databases").json()
    return f"<p> Total Number of Databases in us-west-2 is: {len(response['databases'])}</p>"

@app.route("/get_databases/<int:count>")
def get_databases(count):
    response = requests.get("https://6god8pgyzf.execute-api.us-west-2.amazonaws.com/databases").json()
    log = f"Printing {count} databases"
    return f"<p> <h1>{log}</h1> Total Number of Databases in us-west-2 is: {response['databases'][:count]}</p>"
