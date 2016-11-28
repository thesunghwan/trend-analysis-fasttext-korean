from flask import Flask, render_template, jsonify

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')

@app.route('/list/<word>')
def get_words(word):
    bashCommand = "python3 find_closest_words.py result/model.vec " + word
    import subprocess
    process = subprocess.Popen(bashCommand.split(), stdout=subprocess.PIPE)
    output, error = process.communicate()

    import json

    with open('static/result.json') as json_data:
        d = json.load(json_data)


    return jsonify(**d)

if __name__ == "__main__":
    app.debug = True
    app.run()
