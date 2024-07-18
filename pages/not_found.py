from flask import Blueprint, render_template
import os
from dotenv import load_dotenv

load_dotenv()

not_found = Blueprint('not_found', __name__, template_folder='templates')

@not_found.route("/not_found.html")
def index():
    return render_template("not_found.html", version=os.getenv('VERSION'))