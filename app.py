from flask import Flask, render_template, request
from chat import get_response



app = Flask(__name__)
app.static_folder = 'static'


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/get")
def get_bot_response():
    userText = request.args.get('msg').lower().strip()
    if userText.startswith('my name is'):
        name = userText[11:]
        res1 = get_response(userText)
        res =res1.replace("{n}",name)
    elif userText.startswith('hi my name is'):
        name = userText[14:]
        res1 = get_response(userText)
        res =res1.replace("{n}",name)
    elif userText.startswith(("i'm", "I'm")):
        name = userText[3:].strip().lower()
        if name in ["fine", "great", "awesome", "good"]:
            res1 = get_response(userText)
            res = res1.replace("{n}",'')
            return res
        res1 = get_response(userText)
        res =res1.replace("{n}",name)
    else:
        res = get_response(userText)
    return res



if __name__ == "__main__":
    app.run(debug=True)
