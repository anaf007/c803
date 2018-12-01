# -*- coding: utf-8 -*-

from main.database import Column, Model, SurrogatePK, db, reference_col, relationship

import datetime as dt


class Product(SurrogatePK, Model):
    """表名称system_config
    name：产品名称
    price：价格
    earnings：收益
    cycle：周期
    enable：启用
    sum:总购买数量

    """
    __tablename__ = 'products'
    name = Column(db.String(80),nullable=False)
    price = Column(db.String(80),nullable=False)
    earnings = Column(db.String(80),nullable='0')
    cycle = Column(db.Integer(),default=30)
    enable = Column(db.Boolean,default=True)
    product_sum = Column(db.Integer(),default=0)

    



