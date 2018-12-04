# -*- coding: utf-8 -*-
"""Public section, including homepage and signup."""
from flask import Blueprint, flash, redirect, render_template, request, url_for
from flask_login_multi import login_required, login_user, logout_user

from main.extensions import login_manager
from main.public.forms import LoginForm
from main.user.forms import RegisterForm
from main.user.models import User,Admin
from main.utils import flash_errors
from main.helpers import templated
from .routes import reg_url

from main.models import SmUser

bp = Blueprint('public', __name__, static_folder='../static')
reg_url(bp)


@login_manager.user_loader
def load_user(user_id,endpoint='user'):
    """Load user by ID."""
    if request.blueprint == 'admin':
        return Admin.query.get(int(user_id))
    else:
        # return User.get_by_id(int(user_id))
        return SmUser.query.get(int(user_id))


@login_required
@templated()
def home():
    """Home page."""
    form = LoginForm(request.form)
    return dict(form=form)


@login_required
def logout():
    """Logout."""
    logout_user()
    flash('You are logged out.', 'info')
    return redirect(url_for('public.home'))


# @blueprint.route('/register/', methods=['GET', 'POST'])
# def register():
#     """Register new user."""
#     form = RegisterForm(request.form)
#     if form.validate_on_submit():
#         User.create(username=form.username.data, email=form.email.data, password=form.password.data, active=True)
#         flash('Thank you for registering. You can now log in.', 'success')
#         return redirect(url_for('public.home'))
#     else:
#         flash_errors(form)
#     return render_template('public/register.html', form=form)


@templated()
def about():
    """About page."""
    form = LoginForm(request.form)
    return dict(form=form)


@templated()
def login():
    """login."""
    try:
        form = LoginForm(request.form)
        print('login')
        if request.method == 'POST':
            if form.validate_on_submit():
                login_user(form.user)
                flash('登录成功.', 'success')
                redirect_url = request.args.get('next') or url_for('user.index')
                return redirect(redirect_url)
            else:
                # form.verification_code.data = ''
                # flash_errors(form)
                return 'error'


    except Exception as e:
        print(str(e))
    

    return dict(form=form)



