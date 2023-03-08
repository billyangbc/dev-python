from flask import Flask
from flask import Markup
from flask import render_template

app = Flask(__name__)

@app.route("/")
def test():
    result = Markup('<span style="color: green;">PASS</span>')

    # Return the page with the result.
    return render_template('index.html', result=result)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)