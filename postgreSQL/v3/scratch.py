from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired

class MyForm(FlaskForm):
    name = StringField('name', validators=[DataRequired()])

ob = MyForm()


from flask import Flask
app = Flask(__name__)

@app.route("/")
def test0():
    return "11"


if __name__ == "__main__":
    app.run()