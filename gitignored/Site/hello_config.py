""" Flask configuration file for groja.com

After a bit of research, we are going to use the method presented here:
    http://flask.pocoo.org/docs/0.11/config/
Another resource:
    https://realpython.com/blog/python/flask-by-example-part-1-project-setup/

"""
import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config( object ):
    """ Configuration settings for groja.com """
    TEMPLATES_AUTO_RELOAD = True
    SEND_FILE_MAX_AGE_DEFAULT = 0
    CSRF_ENABLED = True
    #
    #   This is just a formality, to insure the DEBUG setting is off in production.
    #   We turn on debugging by setting FLASK_DEBUG to 1 in the run.sh script
    #
    DEBUG = False
    #
    #   To generate a new key, run these commands:
    #        $ python3
    #       >>> import os
    #       >>> os.urandom(24)
    #   Reference: http://flask.pocoo.org/docs/0.12/quickstart/#sessions
    #
    SECRET_KEY = b'\xf6\xe0[2\xf0\x89:]\xed\xa2\x8a\x97\xcb\x05\x7f\x86>\xc5\xd4g\x00\x01\xb2\xdd'


# ##############################################################################
#
#  THE REST OF THIS FILE IS CRUFT - saved for possible future reference
#  ------------------------------
#
class ProductionConfig( object ):
   TESTING = False

class DevelopmentConfig( object ):
   TESTING = False

class TestingConfig( object ):
   TESTING = True

####  ##
####  # Get additional configuration values based on the hostname
####  #
####  import socket
####  def get_additional_config():
####     hostname = socket.gethostname()
####  
####     if hostname == 'sam':
####        app.config.from_object('config.DevelopmentConfig')
####     else:
####        app.config.from_object('config.ProductionConfig')
####  
####  ##
####  # Load the configuration settings
####  #
####  from config import *
####  app.config.from_object('config.Config')
####  get_additional_config()

