from flask import Blueprint

main = Blueprint('main', __name__)

# Modules are imported at the end to avoid circular dependencies, as views.py and errors.py need to import the main blueprint
from . import views, errors