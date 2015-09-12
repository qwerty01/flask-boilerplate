import sys
sys.path.insert(0, '/home/qw3rty01/public/hackathon.qw3rty01.com/flask-boilerplate')
activate = '/home/qw3rty01/public/hackathon.qw3rty01.com/flask-boilerplate/env/bin/activate_this.py'
execfile(activate, dict(__file__=activate))
from hackathon import app as application
