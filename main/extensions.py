# -*- coding: utf-8 -*-
"""Extensions module. Each extension is initialized in the app factory located in app.py."""
from flask_bcrypt import Bcrypt
from flask_caching import Cache
from flask_debugtoolbar import DebugToolbarExtension
# from flask_login import LoginManager
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from flask_wtf.csrf import CSRFProtect
from flask_login_multi.login_manager import LoginManager  
from flask_restful import Api


bcrypt = Bcrypt()
csrf_protect = CSRFProtect()
login_manager = LoginManager()
db = SQLAlchemy()
migrate = Migrate()
cache = Cache()
debug_toolbar = DebugToolbarExtension()
login_manager = LoginManager() 



login_manager.blueprint_login_views = { 
    'user':  "http://oa.com/login/index?value=f", 
    'admin': "http://oa.com/login/index?value=f", 
} 

login_manager.login_message = "请登录."

api = Api(decorators=[csrf_protect.exempt])

