from project import app
from flask import render_template,redirect,url_for,flash,get_flashed_messages
from project.models import Item2,User

from project import location
from project.forms import RegisterForm
from project import db

@app.route('/')


@app.route('/home')
def hello_world():
    return render_template('home.html')
@app.route('/maps')
def map():
    markers = [
        {
            'lat': location.latitude,
            'lon': location.longitude,
            'popup': 'chennai'
        },
        {
          'lat':12.965965,
            'lon':80.125860,
            'popup':'stany home'
        },
        {
            'lat': 12.964696,
            'lon': 80.109803,
            'popup': 'my home'

        },
        {
            'lat':13.022554,
            'lon':80.167631,
            'popup':'rams home'
        }
    ]
    return render_template('map.html', markers=markers)


@app.route('/find vip')
def find_vip():
    items = Item2.query.all()
    # items = [
    # {'id': 1, 'name': 'parvesh', 'place': 'chennai'},
    # {'id': 2, 'name': 'sureshi', 'place': 'mumbai'},
    # {'id': 3, 'name': 'raaaa', 'place': 'delhi'}
    # ]
    return render_template('findvip.html', items=items)


@app.route('/register', methods=['GET', 'POST'])
def register_page():
    form = RegisterForm()
    if form.validate_on_submit():
        user_to_create = User(username=form.username.data,
                              email_address=form.email_address.data,
                              password_hash=form.password1.data)
        db.session.add(user_to_create)
        db.session.commit()
        return redirect(url_for('map'))
    if form.errors != {}: #If there are not errors from the validations
        for err_msg in form.errors.values():
            flash(f'There was an error with creating a user: {err_msg}',category='danger')

    return render_template('register.html', form=form)
