# -*- coding: utf-8 -*-
"""User models."""
import datetime as dt

from flask_login import UserMixin

from main.database import Column, Model, SurrogatePK, db, reference_col, relationship
from main.extensions import bcrypt


class Role(SurrogatePK, Model):
    """A role for a user."""

    __tablename__ = 'roles'
    name = Column(db.String(80), unique=True, nullable=False)
    user_id = reference_col('users')
    user = relationship('User', backref='roles')

    def __init__(self, name, **kwargs):
        """Create instance."""
        db.Model.__init__(self, name=name, **kwargs)

    def __repr__(self):
        """Represent instance as a unique string."""
        return '<Role({name})>'.format(name=self.name)


class User(UserMixin, SurrogatePK, Model):
    """用户表名称users
     - username：
     - email:
     - password
     - created_at
     - phone
     - first_name
     - last_name
     - active
     - is_admin

     - passcheck:二级密码
     - reid：推荐人id
     - repath：推荐路径
     - regmoney：注册金额
     - recount：推荐人数
     - openid：开通人
     - opentime：开通时间
     - bankname：开户银行名称
     - bankcard：开户银行卡号
     - bankaccount 开户行地址

    """

    __tablename__ = 'users'
    username = Column(db.String(80), unique=True, nullable=False)
    email = Column(db.String(80), unique=True)
    #: The hashed password
    password = Column(db.Binary(128))
    created_at = Column(db.DateTime, nullable=False, default=dt.datetime.utcnow)
    phone = Column(db.String(30))
    first_name = Column(db.String(30))
    last_name = Column(db.String(30))
    active = Column(db.Boolean(), default=False)
    is_admin = Column(db.Boolean(), default=False)

    passcheck = Column(db.Binary(128))
    reid = Column(db.Integer())
    repath =Column(db.UnicodeText())
    regmoney = Column(db.String(30))
    recount = Column(db.Integer(),default=0)
    openid = Column(db.Integer())
    opentime = Column(db.DateTime)
    bankname = Column(db.String(30))
    bankcard = Column(db.String(30))
    bankaccount = Column(db.String(30))
    bankaddress = Column(db.String(30))


    def __init__(self, username, password=None,passcheck=None, **kwargs):
        """Create instance."""
        db.Model.__init__(self, username=username, **kwargs)
        if password:
            self.set_password(password)
        else:
            self.password = None
        if passcheck:
            self.set_passcheck(passcheck)
        else:
            self.passcheck = None


    def set_password(self, password):
        """Set password."""
        self.password = bcrypt.generate_password_hash(password)

    def check_password(self, value):
        """Check password."""
        return bcrypt.check_password_hash(self.password, value)

    def set_passcheck(self, passcheck):
        """Set passcheck."""
        self.passcheck = bcrypt.generate_password_hash(passcheck)

    def check_passcheck(self, value):
        """Check passcheck."""
        return bcrypt.check_password_hash(self.passcheck, value)

    @property
    def full_name(self):
        """Full user name."""
        return '{0} {1}'.format(self.first_name, self.last_name)

    def __repr__(self):
        """Represent instance as a unique string."""
        return '<User({username!r})>'.format(username=self.username)

    # def createuser(self):
    #     self.create(username='admin', password='111111', active=True)  
    #     self.commit()


class Admin(UserMixin, SurrogatePK, Model):
    """A user of the app."""

    __tablename__ = 'admins'
    username = Column(db.String(80), unique=True, nullable=False)
    password = Column(db.Binary(128))
    created_at = Column(db.DateTime, nullable=False, default=dt.datetime.utcnow)
    last_at = Column(db.DateTime)
    phone = Column(db.String(30))

    def __init__(self, username, password=None, **kwargs):
        """Create instance."""
        db.Model.__init__(self, username=username, **kwargs)
        if password:
            self.set_password(password)
        else:
            self.password = None

    def set_password(self, password):
        """Set password."""
        self.password = bcrypt.generate_password_hash(password)

    def check_password(self, value):
        """Check password."""
        return bcrypt.check_password_hash(self.password, value)




