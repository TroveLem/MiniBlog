from flask import Blueprint, render_template, request, url_for, redirect, \
    flash
from flask.ext.login import login_user, login_required, logout_user
from .forms import LoginForm, RegistrationForm
from project.models import Users, bcrypt
from project import db

####                ####
####    config      ####
####	            ####

# change the 'main' to more accurate name
main_blueprint = Blueprint(
    'main', __name__,
    template_folder='templates'
)


####                ####
####    routes      ####
####	            ####

# main page for all registered/non-registered users
@main_blueprint.route('/')
def home():
    return render_template('home.html')


# Login, session key enabled
@main_blueprint.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    form = LoginForm(request.form)
    if request.method == 'POST':
        if form.validate_on_submit():
            user = Users.query.filter_by(username=request.form['username']).first()
            if user is not None and bcrypt.check_password_hash(
                    user.password, request.form['password']
            ):
                login_user(user)
                flash('You successfully logged in!')
                # return redirect(url_for('.profile', user=user))
                return redirect(url_for('.home'))
            else:
                error = 'Invalid username or password.'
    return render_template('login.html', error=error, form=form)


@main_blueprint.route('/logout')
def logout():
    # session.pop('logged_in', None)
    logout_user()
    flash('You were logged out.')
    return redirect(url_for('.home'))


@main_blueprint.route('/register', methods=['GET', 'POST'])
def registration():
    error = None
    form = RegistrationForm(request.form)
    if form.validate_on_submit():
        user = Users(
            username=form.username.data,
            email=form.email.data,
            password=form.password.data
        )
        db.session.add(user)
        db.session.commit()
        flash('Registration was successful!')
        return redirect(url_for('.registration'))
    return render_template('registration.html', form=form, error=error)


@main_blueprint.route('/profile/<user>', methods=['GET', 'POST'])
@login_required
def profile(user):
    user = Users.query.filter_by(username=username).first()
    if user == None:
        flash('User %s not found.' % user)
        return redirect(url_for('.home'))
    return render_template('profile.html', user=user)
