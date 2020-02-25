from flask import Flask, render_template, request
from wtforms.validators import DataRequired
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
import get_friends


app = Flask(__name__)
app.config.from_object(__name__)
app.config['SECRET_KEY'] = 'Very secret key'


class ScreenForm(FlaskForm):
    screen_name = StringField('Screen name', validators=[DataRequired()])
    button = SubmitField('Build map')


@app.route('/', methods=['GET','POST'])
def main():
    form = ScreenForm()
    print(request.method)
    if request.method == 'POST':
        print('HERE')
        return get_friends.get_location(request.form.get('screen_name'))
    else:
        return render_template('index.html', form=form)


if __name__ == '__main__':
    app.run(port=3000)