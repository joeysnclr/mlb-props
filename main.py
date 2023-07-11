from flask import Flask, jsonify
import os
import json

app = Flask(__name__)
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True



@app.route('/')
def index():
    return jsonify({"Choo Choo": "Welcome to your Flask app 🚅"})

@app.route('/api/mlb-props/today')
def today():
    fake_data = [
        {
            "date": "2023-07-09",
            "player_name": "Mike Trout",
            "prop_name": "Hits",
            "prop_line": "2.5",
            "player_team": "Los Angeles Angels",
            "opposing_team": "Houston Astros",
            "opposing_starter": "Zack Greinke",
            "over_probability": 0.6,
            "under_probability": 0.4
        },
        {
            "date": "2023-07-09",
            "player_name": "Mookie Betts",
            "prop_name": "Home Runs",
            "prop_line": "0.5",
            "player_team": "Los Angeles Dodgers",
            "opposing_team": "San Francisco Giants",
            "opposing_starter": "Kevin Gausman",
            "over_probability": 0.3,
            "under_probability": 0.7
        },
        {
            "date": "2023-07-10",
            "player_name": "Aaron Judge",
            "prop_name": "RBIs",
            "prop_line": "1.5",
            "player_team": "New York Yankees",
            "opposing_team": "Boston Red Sox",
            "opposing_starter": "Chris Sale",
            "over_probability": 0.5,
            "under_probability": 0.5
        }
        ]

    # format the data nicely with jsonify
    return jsonify(fake_data)


if __name__ == '__main__':
    app.run(debug=True, port=os.getenv("PORT", default=8888))
