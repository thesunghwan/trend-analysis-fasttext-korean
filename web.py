from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    bashCommand = "python3 find_closest_words.py result/model.vec 박근혜"
    import subprocess
    process = subprocess.Popen(bashCommand.split(), stdout=subprocess.PIPE)
    output, error = process.communicate()

    print(output, error)

    return "Hello World!"

if __name__ == "__main__":
    app.run()
