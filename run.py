import os
from flask import Flask, render_template, flash, redirect, url_for, session, logging, request
from flask_sqlalchemy import SQLAlchemy
import cherrypy
from flask_httpauth import HTTPBasicAuth

from routes import app

auth = HTTPBasicAuth()

cherrypy.tree.graft(app.wsgi_app, '/')
cherrypy.config.update({'server.socket_host': '0.0.0.0',
                           'server.socket_port': 7001,
                           'engine.autoreload.on': False,
                           })

if __name__ == "__main__":
    app.config['SECRET_KEY'] = os.getenv('SECRET')
    try:
       cherrypy.engine.start()
    except KeyboardInterrupt:
       cherrypy.engine.stop()