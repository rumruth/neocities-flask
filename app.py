from flask import Flask
import sass

from pages.home import home
from pages.not_found import not_found
from pages.about import about

app = Flask(__name__)
app.register_blueprint(home)
app.register_blueprint(not_found)
app.register_blueprint(about)

sass.compile(dirname=('styles', 'static/styles'))
