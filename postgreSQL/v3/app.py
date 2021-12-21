from flask import Flask, render_template, Markup
import sys
# a = sys.getrecursionlimit
# print(a)
sys.setrecursionlimit(2227)

app = Flask(__name__, template_folder= "templates")

@app.route('/')
def home():
    """Landing page."""
    # return "hey" # works
    # return Markup("<h1>Hello World!</h1>") # works too
    return render_template('/contact.html', title="Lame Site") # strich richtung ist korrekt so # index.html doch found


if __name__ == "__main__":
    app.run()