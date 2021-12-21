


from flask import Flask, url_for, render_template, redirect
from forms import ContactForm
import config

# app = Flask(__name__, instance_relative_config=False)
app = Flask(__name__, template_folder= "templates") #, static_folder="static"
app.config.from_object('config.Config')
# app = Flask(__name__)

@app.route('/', methods=('GET', 'POST'))
def contact():
    form = ContactForm()
    if form.validate_on_submit():
        return redirect(url_for('success'))
    # print(form.name.data)
    return render_template('/contact.html', form=form)

@app.route('/test', methods=('GET', 'POST'))
def test():
    form = ContactForm()
    if form.validate_on_submit():
        return redirect(url_for('success'))
    # print(form.name.data)
    return render_template('/index1.html', form=form)

# @app.route('/test2', methods=('GET', 'POST'))
# def test2()



#
# @app.route('/test')
# def test():
#        return render_template('/index1.html')


if __name__ == "__main__":
    app.run()