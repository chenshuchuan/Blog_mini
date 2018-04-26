# -*- coding: utf-8 -*-
from werkzeug.contrib.fixers import ProxyFix
from flask_babel import Babel, gettext as _
from app import create_app

app.create_app()
saasapp = app.app_

babel = Babel(app.app_)

saasapp.wsgi_app = ProxyFix(saasapp.wsgi_app)

if __name__ == '__main__':
    saasapp.run()
