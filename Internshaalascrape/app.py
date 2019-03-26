import os
import operator

from flask import Flask, render_template, url_for, json

app = Flask(__name__)

@app.route('/')
def index():
    SITE_ROOT = os.path.realpath(os.path.dirname(__file__))

    profile_url = os.path.join(SITE_ROOT, "static/data", "intern_count.json")
    profile = json.load(open(profile_url))
    sorted_profile = sorted(profile.items(), key=operator.itemgetter(1), reverse=True)

    location_url = os.path.join(SITE_ROOT, "static/data", "location_count.json")
    locations = json.load(open(location_url))
    sorted_locations = sorted(locations.items(), key=operator.itemgetter(1), reverse=True)

    return render_template('index.html',profiles=sorted_profile,locations=sorted_locations)

if __name__ == '__main__':
    app.run(debug=True)
