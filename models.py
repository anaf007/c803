# coding: utf-8
from sqlalchemy import Column, DECIMAL, String, Text, text
from sqlalchemy.dialects.mysql import DECIMAL, INTEGER, SMALLINT, TINYINT
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
metadata = Base.metadata


class SmAdmin(Base):
    __tablename__ = 'sm_admin'

    id = Column(INTEGER(11), primary_key=True)
    username = Column(String(25))
    password = Column(String(50))
    passcheck = Column(String(50))
    token = Column(String(25))
    status = Column(TINYINT(3), server_default=text("'0'"))
    addtime = Column(INTEGER(11), server_default=text("'0'"))
    last_login_time = Column(INTEGER(11), server_default=text("'0'"))
    last_login_ip = Column(String(25))


class SmArticle(Base):
    __tablename__ = 'sm_article'

    id = Column(INTEGER(11), primary_key=True)
    title = Column(String(50), nullable=False)
    keyword = Column(String(255))
    thumb = Column(String(150), server_default=text("''"))
    abstract = Column(String(255), nullable=False, server_default=text("''"))
    author = Column(String(25))
    content = Column(Text, nullable=False)
    view_count = Column(INTEGER(11), server_default=text("'0'"))
    status = Column(TINYINT(1), server_default=text("'0'"))
    sort = Column(SMALLINT(6), server_default=text("'0'"))
    addtime = Column(INTEGER(11), nullable=False, server_default=text("'0'"))
    adminname = Column(String(50))


class SmAuthGroup(Base):
    __tablename__ = 'sm_auth_group'

    id = Column(INTEGER(11), primary_key=True)
    title = Column(String(50))
    rules = Column(Text)
    addtime = Column(INTEGER(11), server_default=text("'0'"))
    status = Column(TINYINT(3), server_default=text("'0'"))


class SmAuthGroupAcces(Base):
    __tablename__ = 'sm_auth_group_access'

    id = Column(INTEGER(11), primary_key=True)
    uid = Column(INTEGER(11), server_default=text("'0'"))
    group_id = Column(INTEGER(11), server_default=text("'0'"))


class SmAuthRule(Base):
    __tablename__ = 'sm_auth_rule'

    id = Column(INTEGER(11), primary_key=True)
    classid = Column(INTEGER(11), server_default=text("'0'"))
    name = Column(String(255))
    title = Column(String(50))
    type = Column(TINYINT(1), server_default=text("'1'"))
    status = Column(TINYINT(3), server_default=text("'0'"))
    addtime = Column(INTEGER(11), server_default=text("'0'"))
    condition = Column(String(255))


class SmAuthRuleClas(Base):
    __tablename__ = 'sm_auth_rule_class'

    classid = Column(INTEGER(11), primary_key=True)
    classname = Column(String(25))
    addtime = Column(INTEGER(11), server_default=text("'0'"))


class SmCashprice(Base):
    __tablename__ = 'sm_cashprice'

    id = Column(INTEGER(11), primary_key=True)
    price = Column(String(10))
    float = Column(String(10))
    addtime = Column(INTEGER(11), server_default=text("'0'"))


class SmCoinTran(Base):
    __tablename__ = 'sm_coin_trans'

    id = Column(INTEGER(11), primary_key=True)
    uid = Column(INTEGER(11), server_default=text("'0'"))
    type = Column(String(10))
    referer = Column(String(50))
    amount = Column(DECIMAL(20, 4), server_default=text("'0.0000'"))
    tax = Column(DECIMAL(20, 4), server_default=text("'0.0000'"))
    valamount = Column(DECIMAL(20, 4), server_default=text("'0.0000'"))
    intime = Column(INTEGER(11), server_default=text("'0'"))


class SmConfig(Base):
    __tablename__ = 'sm_config'

    id = Column(INTEGER(11), primary_key=True)
    sitename = Column(String(50))
    sitetitle = Column(String(50))
    levelname = Column(String(255))
    signamount = Column(String(255))
    bankname = Column(String(255))
    companybank = Column(String(255))
    systemswitch = Column(TINYINT(3), server_default=text("'0'"))
    note = Column(String(255))
    minwith = Column(String(8), server_default=text("'0.00'"))
    withwas = Column(String(8), server_default=text("'0.00'"))
    withtax = Column(String(6), server_default=text("'0.00'"))
    withtype = Column(String(50))
    withweek = Column(String(25))
    minrechge = Column(String(8), server_default=text("'0.00'"))
    rechgewas = Column(String(8), server_default=text("'0.00'"))
    rechgetype = Column(String(50))
    exchangetype = Column(String(255))
    shopcash = Column(String(255))
    transcash = Column(String(50))
    mintransfer = Column(String(50))
    smsurl = Column(String(255))
    smsuser = Column(String(255))
    smsapikey = Column(String(255))
    smssignature = Column(String(25))
    smscointrans = Column(TINYINT(1), server_default=text("'0'"))
    smsexchange = Column(TINYINT(1), server_default=text("'0'"))
    minername1 = Column(String(25))
    minername2 = Column(String(25))
    minername3 = Column(String(25))
    minername4 = Column(String(25))
    minername5 = Column(String(25))
    minerprice1 = Column(String(10))
    minerprice2 = Column(String(10))
    minerprice3 = Column(String(10))
    minerprice4 = Column(String(10))
    minerprice5 = Column(String(10))
    minerout1 = Column(String(10))
    minerout2 = Column(String(10))
    minerout3 = Column(String(10))
    minerout4 = Column(String(10))
    minerout5 = Column(String(10))
    minerhour1 = Column(String(10))
    minerhour2 = Column(String(10))
    minerhour3 = Column(String(10))
    minerhour4 = Column(String(10))
    minerhour5 = Column(String(10))
    minerswitch1 = Column(TINYINT(1), server_default=text("'0'"))
    minerswitch2 = Column(TINYINT(1), server_default=text("'0'"))
    minerswitch3 = Column(TINYINT(1), server_default=text("'0'"))
    minerswitch4 = Column(TINYINT(1), server_default=text("'0'"))
    minerswitch5 = Column(TINYINT(1), server_default=text("'0'"))
    minerbuymax = Column(String(10))
    signgive = Column(String(10))
    jdbonus = Column(String(255))


class SmExchange(Base):
    __tablename__ = 'sm_exchange'

    id = Column(INTEGER(11), primary_key=True)
    uid = Column(INTEGER(11), server_default=text("'0'"))
    ztype = Column(String(25))
    amount = Column(DECIMAL(20, 4), server_default=text("'0.0000'"))
    valamount = Column(DECIMAL(20, 4), nullable=False, server_default=text("'0.0000'"))
    addtime = Column(INTEGER(11), server_default=text("'0'"))


class SmHistory(Base):
    __tablename__ = 'sm_history'

    id = Column(INTEGER(11), primary_key=True)
    uid = Column(INTEGER(11), server_default=text("'0'"))
    htype = Column(String(25))
    amount_q = Column(DECIMAL(20, 4), server_default=text("'0.0000'"))
    amount = Column(DECIMAL(20, 4), server_default=text("'0.0000'"))
    amount_h = Column(DECIMAL(20, 4), server_default=text("'0.0000'"))
    note = Column(String(255))
    oid = Column(INTEGER(11), server_default=text("'0'"))
    addtime = Column(INTEGER(11), server_default=text("'0'"))
    actionname = Column(String(25))


class SmMessage(Base):
    __tablename__ = 'sm_message'

    id = Column(INTEGER(11), primary_key=True)
    send_uid = Column(INTEGER(11), server_default=text("'0'"))
    receive_uid = Column(INTEGER(11), server_default=text("'0'"))
    mid = Column(INTEGER(11), server_default=text("'0'"))
    content = Column(String(255))
    status = Column(TINYINT(3), server_default=text("'0'"))
    addtime = Column(INTEGER(11), server_default=text("'0'"))
    updatetime = Column(INTEGER(11), nullable=False, server_default=text("'0'"))


class SmMiner(Base):
    __tablename__ = 'sm_miner'

    id = Column(INTEGER(11), primary_key=True)
    uid = Column(INTEGER(11), server_default=text("'0'"))
    minertype = Column(TINYINT(1), server_default=text("'0'"))
    minerlife = Column(String(10))
    minerout = Column(String(10))
    buytime = Column(INTEGER(11), server_default=text("'0'"))
    status = Column(TINYINT(1), server_default=text("'0'"))
    source = Column(String(10))
    totalout = Column(DECIMAL(10, 2), server_default=text("'0.00'"))


class SmSl(Base):
    __tablename__ = 'sm_sl'

    id = Column(INTEGER(11), primary_key=True)
    uid = Column(INTEGER(11), server_default=text("'0'"))
    type = Column(String(25))
    amount = Column(DECIMAL(20, 4), server_default=text("'0.0000'"))
    suanli = Column(DECIMAL(20, 4), server_default=text("'0.0000'"))
    up = Column(DECIMAL(20, 4), server_default=text("'0.0000'"))
    addtime = Column(INTEGER(11), server_default=text("'0'"))
    day = Column(String(20))


class SmUser(Base):
    __tablename__ = 'sm_user'

    id = Column(INTEGER(11), primary_key=True)
    username = Column(String(25))
    truename = Column(String(25))
    password = Column(String(50))
    passcheck = Column(String(50))
    token = Column(String(25))
    mobile = Column(String(20))
    reid = Column(INTEGER(11), server_default=text("'0'"))
    re_path = Column(Text)
    relevel = Column(INTEGER(11), server_default=text("'0'"))
    fatherid = Column(INTEGER(11), server_default=text("'0'"))
    p_path = Column(Text)
    plevel = Column(INTEGER(11), server_default=text("'0'"))
    l = Column(INTEGER(11), server_default=text("'0'"))
    r = Column(INTEGER(11), server_default=text("'0'"))
    signmoney = Column(DECIMAL(10, 2), server_default=text("'0.00'"))
    level = Column(TINYINT(1), server_default=text("'0'"))
    recount = Column(INTEGER(11), server_default=text("'0'"))
    agentname = Column(String(50), server_default=text("'0'"))
    openid = Column(INTEGER(11), server_default=text("'0'"))
    signtime = Column(INTEGER(11), server_default=text("'0'"))
    opentime = Column(INTEGER(11), server_default=text("'0'"))
    status = Column(TINYINT(1), server_default=text("'0'"))
    is_login = Column(TINYINT(1), server_default=text("'1'"))
    transcash = Column(DECIMAL(20, 4), server_default=text("'0.0000'"))
    wkcash = Column(DECIMAL(20, 4), server_default=text("'0.0000'"))
    usercode = Column(String(25))
    address = Column(String(50))
    bankname = Column(String(25))
    bankcard = Column(String(25))
    bankaccount = Column(String(25))
    bankaddress = Column(String(50))
    alipay = Column(String(25))
    wechat = Column(String(25))
    area = Column(TINYINT(3), server_default=text("'0'"))
    answer = Column(String(50))
    newl = Column(DECIMAL(10, 2), server_default=text("'0.00'"))
    newr = Column(DECIMAL(10, 2), server_default=text("'0.00'"))
    lyj = Column(DECIMAL(20, 2), server_default=text("'0.00'"))
    ryj = Column(DECIMAL(20, 2), server_default=text("'0.00'"))
    scday = Column(String(10))
    is_ft = Column(TINYINT(1), server_default=text("'0'"))
    code1 = Column(String(255))
    code2 = Column(String(255))
    code3 = Column(String(255))


class SmWithcash(Base):
    __tablename__ = 'sm_withcash'

    id = Column(INTEGER(11), primary_key=True)
    uid = Column(INTEGER(11), server_default=text("'0'"))
    hid = Column(INTEGER(11), server_default=text("'0'"))
    wtype = Column(String(25))
    amount = Column(DECIMAL(10, 2), server_default=text("'0.00'"))
    tax = Column(DECIMAL(10, 2), server_default=text("'0.00'"))
    note = Column(String(255))
    status = Column(TINYINT(3), server_default=text("'0'"))
    addtime = Column(INTEGER(11), server_default=text("'0'"))
    updatetime = Column(INTEGER(11), server_default=text("'0'"))
    adminname = Column(String(25))
    qrcode = Column(String(50))


