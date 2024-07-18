from flask import Blueprint, render_template
import os
from dotenv import load_dotenv

load_dotenv()

about = Blueprint('about', __name__, template_folder='templates')

@about.route("/about.html")
def index():
    return render_template("about.html", version=os.getenv('VERSION'), username=os.getenv('NC_USER'))