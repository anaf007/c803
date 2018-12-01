# -*- coding: utf-8 -*-

from main.database import Column, Model, SurrogatePK, db, reference_col, relationship

import datetime as dt



class SystenConfig(SurrogatePK, Model):
    """表名称system_config
    name：系统名称
    title：系统标题
    enable：前台是否可用
    enable_msg：前台关闭提示
    blank_name：注册银行列表，| 分割
    minwith：提现最低金额
    withwas：提现金额倍数
    withtax：提现手续费系数
    mintransfer:最低转账
    max_buy_product:最大产品购买量
    default_send_product:默认注册送的产品

    """
    __tablename__ = 'system_config'
    name = Column(db.String(80),nullable=False)
    title = Column(db.String(80),nullable=False)
    enable = Column(db.Boolean,default=True)
    enable_msg = Column(db.String(200),nullable=False)
    blank_name = Column(db.String(200),nullable=False)
    minwith = Column(db.Integer(),default=0)
    withwas = Column(db.Integer(),default=0)
    withtax = Column(db.Float(),default=0.01)
    mintransfer = Column(db.Integer(),default=0)
    max_buy_product = Column(db.Integer(),default=5)
    default_send_product = Column(db.Integer(),default=1)

    



