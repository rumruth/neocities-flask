from flask import Blueprint, render_template
import os
from dotenv import load_dotenv

load_dotenv()

home = Blueprint('home', __name__, template_folder='templates')

@home.route("/")
def index():
    return render_template("home.html", version=os.getenv('VERSION'), username=os.getenv('NC_USER'))