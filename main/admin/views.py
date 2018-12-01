# -*- coding: utf-8 -*-
"""User views."""
from flask import Blueprint, render_template,jsonify,request,url_for,flash,redirect,session
from flask_login import login_required
from flask_login_multi import login_required, login_user, logout_user

from main.user.models import Admin,User
from main.public.models import Product
from main.admin.models import SystenConfig
from main.extensions import csrf_protect
from main.helpers import templated
from .routes import reg_url

bp = Blueprint('admin', __name__, url_prefix='/admin')
reg_url(bp)

@bp.before_request
def before_request():
    if not session.get('system_config'):
        sc = SystenConfig.query.first()
        sc_json = {
            'name':sc.name,
            'title':sc.title,
            'enable':sc.enable,
            'enable_msg':sc.enable_msg,
            'blank_name':sc.blank_name,
            'minwith':sc.minwith,
            'withwas':sc.withwas,
            'withtax':sc.withtax,
            'mintransfer':sc.mintransfer,
            'max_buy_product':sc.max_buy_product,
            'default_send_product':sc.default_send_product
        }
        session['system_config'] = sc_json
                        
    

@login_required
@templated()
def index():
    return dict()


@login_required
@templated()
def home():
    return dict()


@csrf_protect.exempt
@templated()
def login():
    if request.method == 'POST':
        admin = Admin.query.filter_by(username=request.form['username']).first()
        if not admin:
            return jsonify({'code':0,'msg':'没有该用户。','url':url_for('.login',_external=True)})
        if not admin.check_password(request.form['password']):
            return jsonify({'code':0,'msg':'密码不正确。','url':url_for('.login',_external=True)})
        login_user(admin)
        return jsonify({'code':1,'url':url_for('.index',_external=True),'msg':'登录成功。'})
    return dict()


@login_required
def logout():
    """Logout."""
    logout_user()
    flash('您已退出登录.', 'info')
    return redirect(url_for('admin.index'))


@csrf_protect.exempt
@login_required
@templated()
def user_add():
    if not request.method == 'POST':
        return dict()
    #推荐人
    rename = request.form['rename']
    #会员名称
    truename = request.form['truename']
    #手机号
    mobile = request.form['mobile']
    #注册购币
    signmoney = request.form['signmoney']


    rename = User.query.filter_by(username=rename).first()
    if not rename:
        return jsonify({'code':0,'url':'','msg':'没有该推荐人。'})

    user = User.query.filter_by(username=mobile).first()
    if user:
        return jsonify({'code':0,'url':'','msg':'该手机号已被注册。'})

    if not rename.repath:
        rename.repath = ''

    User.create(
        username = mobile,
        phone = mobile,
        first_name = truename,
        password = '123456',
        passcheck = '123456',
        reid = rename.id,
        repath = rename.repath+','+str(rename.id),
        regmoney = float(signmoney)
    )

    return jsonify({'code':1,'url':'','msg':'注册完成'})



@login_required
@templated()
def user_index():
    userall = User.query.filter_by(active=False).all()
    return dict(userall=userall)


@login_required
@templated()
def user_list():
    userall = User.query.filter_by(active=True).order_by(User.id.desc()).all()
    return dict(userall=userall)


@login_required
@templated()
def retree():
    return dict()


@login_required
@templated()
def cash_monenychange():
    return dict()

@login_required
@templated()
def cash_list():
    return dict()


@login_required
@templated()
def cash_transfer():
    return dict()


@login_required
@templated()
def withcashlist():
    return dict()


@login_required
@templated()
def miner_list():
    return dict()


@login_required
@templated()
def system_config():
    sc = session.get('system_config')
    return dict(sc=sc)



@login_required
@templated()
def bonus_config():
    product = Product.query.all()
    max_buy_product = session['system_config']['max_buy_product']
    df = session['system_config']['default_send_product']
    p = Product.query.get(int(df))
    return dict(product=product,max=max_buy_product,p=p)


