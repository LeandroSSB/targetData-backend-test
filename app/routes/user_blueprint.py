from flask import Blueprint

bp = Blueprint("bp_user", __name__, url_prefix='/user')

bp.post("/login")()
