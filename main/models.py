# coding: utf-8
from sqlalchemy import Column, Integer, Numeric, SmallInteger, String, Text
from sqlalchemy.schema import FetchedValue
from flask_login import UserMixin


from main.database import db 


class SmAdmin(db.Model):
    __tablename__ = 'sm_admin'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(25))
    password = db.Column(db.String(50))
    passcheck = db.Column(db.String(50))
    token = db.Column(db.String(25))
    status = db.Column(db.Integer, server_default=db.FetchedValue())
    addtime = db.Column(db.Integer, server_default=db.FetchedValue())
    last_login_time = db.Column(db.Integer, server_default=db.FetchedValue())
    last_login_ip = db.Column(db.String(25))


class SmArticle(db.Model):
    __tablename__ = 'sm_article'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50), nullable=False)
    keyword = db.Column(db.String(255))
    thumb = db.Column(db.String(150), server_default=db.FetchedValue())
    abstract = db.Column(db.String(255), nullable=False, server_default=db.FetchedValue())
    author = db.Column(db.String(25))
    content = db.Column(db.Text, nullable=False)
    view_count = db.Column(db.Integer, server_default=db.FetchedValue())
    status = db.Column(db.Integer, server_default=db.FetchedValue())
    sort = db.Column(db.SmallInteger, server_default=db.FetchedValue())
    addtime = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    adminname = db.Column(db.String(50))


class SmAuthGroup(db.Model):
    __tablename__ = 'sm_auth_group'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50))
    rules = db.Column(db.Text)
    addtime = db.Column(db.Integer, server_default=db.FetchedValue())
    status = db.Column(db.Integer, server_default=db.FetchedValue())


class SmAuthGroupAcces(db.Model):
    __tablename__ = 'sm_auth_group_access'

    id = db.Column(db.Integer, primary_key=True)
    uid = db.Column(db.Integer, server_default=db.FetchedValue())
    group_id = db.Column(db.Integer, server_default=db.FetchedValue())


class SmAuthRule(db.Model):
    __tablename__ = 'sm_auth_rule'

    id = db.Column(db.Integer, primary_key=True)
    classid = db.Column(db.Integer, server_default=db.FetchedValue())
    name = db.Column(db.String(255))
    title = db.Column(db.String(50))
    type = db.Column(db.Integer, server_default=db.FetchedValue())
    status = db.Column(db.Integer, server_default=db.FetchedValue())
    addtime = db.Column(db.Integer, server_default=db.FetchedValue())
    condition = db.Column(db.String(255))


class SmAuthRuleClas(db.Model):
    __tablename__ = 'sm_auth_rule_class'

    classid = db.Column(db.Integer, primary_key=True)
    classname = db.Column(db.String(25))
    addtime = db.Column(db.Integer, server_default=db.FetchedValue())


class SmCashprice(db.Model):
    __tablename__ = 'sm_cashprice'

    id = db.Column(db.Integer, primary_key=True)
    price = db.Column(db.String(10))
    float = db.Column(db.String(10))
    addtime = db.Column(db.Integer, server_default=db.FetchedValue())


class SmCoinTran(db.Model):
    __tablename__ = 'sm_coin_trans'

    id = db.Column(db.Integer, primary_key=True)
    uid = db.Column(db.Integer, server_default=db.FetchedValue())
    type = db.Column(db.String(10))
    referer = db.Column(db.String(50))
    amount = db.Column(db.Numeric(20, 4), server_default=db.FetchedValue())
    tax = db.Column(db.Numeric(20, 4), server_default=db.FetchedValue())
    valamount = db.Column(db.Numeric(20, 4), server_default=db.FetchedValue())
    intime = db.Column(db.Integer, server_default=db.FetchedValue())


class SmConfig(db.Model):
    __tablename__ = 'sm_config'

    id = db.Column(db.Integer, primary_key=True)
    sitename = db.Column(db.String(50))
    sitetitle = db.Column(db.String(50))
    levelname = db.Column(db.String(255))
    signamount = db.Column(db.String(255))
    bankname = db.Column(db.String(255))
    companybank = db.Column(db.String(255))
    systemswitch = db.Column(db.Integer, server_default=db.FetchedValue())
    note = db.Column(db.String(255))
    minwith = db.Column(db.String(8), server_default=db.FetchedValue())
    withwas = db.Column(db.String(8), server_default=db.FetchedValue())
    withtax = db.Column(db.String(6), server_default=db.FetchedValue())
    withtype = db.Column(db.String(50))
    withweek = db.Column(db.String(25))
    minrechge = db.Column(db.String(8), server_default=db.FetchedValue())
    rechgewas = db.Column(db.String(8), server_default=db.FetchedValue())
    rechgetype = db.Column(db.String(50))
    exchangetype = db.Column(db.String(255))
    shopcash = db.Column(db.String(255))
    transcash = db.Column(db.String(50))
    mintransfer = db.Column(db.String(50))
    smsurl = db.Column(db.String(255))
    smsuser = db.Column(db.String(255))
    smsapikey = db.Column(db.String(255))
    smssignature = db.Column(db.String(25))
    smscointrans = db.Column(db.Integer, server_default=db.FetchedValue())
    smsexchange = db.Column(db.Integer, server_default=db.FetchedValue())
    minername1 = db.Column(db.String(25))
    minername2 = db.Column(db.String(25))
    minername3 = db.Column(db.String(25))
    minername4 = db.Column(db.String(25))
    minername5 = db.Column(db.String(25))
    minerprice1 = db.Column(db.String(10))
    minerprice2 = db.Column(db.String(10))
    minerprice3 = db.Column(db.String(10))
    minerprice4 = db.Column(db.String(10))
    minerprice5 = db.Column(db.String(10))
    minerout1 = db.Column(db.String(10))
    minerout2 = db.Column(db.String(10))
    minerout3 = db.Column(db.String(10))
    minerout4 = db.Column(db.String(10))
    minerout5 = db.Column(db.String(10))
    minerhour1 = db.Column(db.String(10))
    minerhour2 = db.Column(db.String(10))
    minerhour3 = db.Column(db.String(10))
    minerhour4 = db.Column(db.String(10))
    minerhour5 = db.Column(db.String(10))
    minerswitch1 = db.Column(db.Integer, server_default=db.FetchedValue())
    minerswitch2 = db.Column(db.Integer, server_default=db.FetchedValue())
    minerswitch3 = db.Column(db.Integer, server_default=db.FetchedValue())
    minerswitch4 = db.Column(db.Integer, server_default=db.FetchedValue())
    minerswitch5 = db.Column(db.Integer, server_default=db.FetchedValue())
    minerbuymax = db.Column(db.String(10))
    signgive = db.Column(db.String(10))
    jdbonus = db.Column(db.String(255))


class SmExchange(db.Model):
    __tablename__ = 'sm_exchange'

    id = db.Column(db.Integer, primary_key=True)
    uid = db.Column(db.Integer, server_default=db.FetchedValue())
    ztype = db.Column(db.String(25))
    amount = db.Column(db.Numeric(20, 4), server_default=db.FetchedValue())
    valamount = db.Column(db.Numeric(20, 4), nullable=False, server_default=db.FetchedValue())
    addtime = db.Column(db.Integer, server_default=db.FetchedValue())


class SmHistory(db.Model):
    __tablename__ = 'sm_history'

    id = db.Column(db.Integer, primary_key=True)
    uid = db.Column(db.Integer, server_default=db.FetchedValue())
    htype = db.Column(db.String(25))
    amount_q = db.Column(db.Numeric(20, 4), server_default=db.FetchedValue())
    amount = db.Column(db.Numeric(20, 4), server_default=db.FetchedValue())
    amount_h = db.Column(db.Numeric(20, 4), server_default=db.FetchedValue())
    note = db.Column(db.String(255))
    oid = db.Column(db.Integer, server_default=db.FetchedValue())
    addtime = db.Column(db.Integer, server_default=db.FetchedValue())
    actionname = db.Column(db.String(25))


class SmMessage(db.Model):
    __tablename__ = 'sm_message'

    id = db.Column(db.Integer, primary_key=True)
    send_uid = db.Column(db.Integer, server_default=db.FetchedValue())
    receive_uid = db.Column(db.Integer, server_default=db.FetchedValue())
    mid = db.Column(db.Integer, server_default=db.FetchedValue())
    content = db.Column(db.String(255))
    status = db.Column(db.Integer, server_default=db.FetchedValue())
    addtime = db.Column(db.Integer, server_default=db.FetchedValue())
    updatetime = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())


class SmMiner(db.Model):
    __tablename__ = 'sm_miner'

    id = db.Column(db.Integer, primary_key=True)
    uid = db.Column(db.Integer, server_default=db.FetchedValue())
    minertype = db.Column(db.Integer, server_default=db.FetchedValue())
    minerlife = db.Column(db.String(10))
    minerout = db.Column(db.String(10))
    buytime = db.Column(db.Integer, server_default=db.FetchedValue())
    status = db.Column(db.Integer, server_default=db.FetchedValue())
    source = db.Column(db.String(10))
    totalout = db.Column(db.Numeric(10, 2), server_default=db.FetchedValue())


class SmSl(db.Model):
    __tablename__ = 'sm_sl'

    id = db.Column(db.Integer, primary_key=True)
    uid = db.Column(db.Integer, server_default=db.FetchedValue())
    type = db.Column(db.String(25))
    amount = db.Column(db.Numeric(20, 4), server_default=db.FetchedValue())
    suanli = db.Column(db.Numeric(20, 4), server_default=db.FetchedValue())
    up = db.Column(db.Numeric(20, 4), server_default=db.FetchedValue())
    addtime = db.Column(db.Integer, server_default=db.FetchedValue())
    day = db.Column(db.String(20))


class SmUser(db.Model,UserMixin):
    __tablename__ = 'sm_user'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(25))
    truename = db.Column(db.String(25))
    password = db.Column(db.String(50))
    passcheck = db.Column(db.String(50))
    token = db.Column(db.String(25))
    mobile = db.Column(db.String(20))
    reid = db.Column(db.Integer, server_default=db.FetchedValue())
    re_path = db.Column(db.Text)
    relevel = db.Column(db.Integer, server_default=db.FetchedValue())
    fatherid = db.Column(db.Integer, server_default=db.FetchedValue())
    p_path = db.Column(db.Text)
    plevel = db.Column(db.Integer, server_default=db.FetchedValue())
    l = db.Column(db.Integer, server_default=db.FetchedValue())
    r = db.Column(db.Integer, server_default=db.FetchedValue())
    signmoney = db.Column(db.Numeric(10, 2), server_default=db.FetchedValue())
    level = db.Column(db.Integer, server_default=db.FetchedValue())
    recount = db.Column(db.Integer, server_default=db.FetchedValue())
    agentname = db.Column(db.String(50), server_default=db.FetchedValue())
    openid = db.Column(db.Integer, server_default=db.FetchedValue())
    signtime = db.Column(db.Integer, server_default=db.FetchedValue())
    opentime = db.Column(db.Integer, server_default=db.FetchedValue())
    status = db.Column(db.Integer, server_default=db.FetchedValue())
    is_login = db.Column(db.Integer, server_default=db.FetchedValue())
    transcash = db.Column(db.Numeric(20, 4), server_default=db.FetchedValue())
    wkcash = db.Column(db.Numeric(20, 4), server_default=db.FetchedValue())
    usercode = db.Column(db.String(25))
    address = db.Column(db.String(50))
    bankname = db.Column(db.String(25))
    bankcard = db.Column(db.String(25))
    bankaccount = db.Column(db.String(25))
    bankaddress = db.Column(db.String(50))
    alipay = db.Column(db.String(25))
    wechat = db.Column(db.String(25))
    area = db.Column(db.Integer, server_default=db.FetchedValue())
    answer = db.Column(db.String(50))
    newl = db.Column(db.Numeric(10, 2), server_default=db.FetchedValue())
    newr = db.Column(db.Numeric(10, 2), server_default=db.FetchedValue())
    lyj = db.Column(db.Numeric(20, 2), server_default=db.FetchedValue())
    ryj = db.Column(db.Numeric(20, 2), server_default=db.FetchedValue())
    scday = db.Column(db.String(10))
    is_ft = db.Column(db.Integer, server_default=db.FetchedValue())
    code1 = db.Column(db.String(255))
    code2 = db.Column(db.String(255))
    code3 = db.Column(db.String(255))
    is_active = db.Column(db.SmallInteger, server_default=db.FetchedValue())
    is_admin = db.Column(db.SmallInteger, default=0)


class SmWithcash(db.Model):
    __tablename__ = 'sm_withcash'

    id = db.Column(db.Integer, primary_key=True)
    uid = db.Column(db.Integer, server_default=db.FetchedValue())
    hid = db.Column(db.Integer, server_default=db.FetchedValue())
    wtype = db.Column(db.String(25))
    amount = db.Column(db.Numeric(10, 2), server_default=db.FetchedValue())
    tax = db.Column(db.Numeric(10, 2), server_default=db.FetchedValue())
    note = db.Column(db.String(255))
    status = db.Column(db.Integer, server_default=db.FetchedValue())
    addtime = db.Column(db.Integer, server_default=db.FetchedValue())
    updatetime = db.Column(db.Integer, server_default=db.FetchedValue())
    adminname = db.Column(db.String(25))
    qrcode = db.Column(db.String(50))
