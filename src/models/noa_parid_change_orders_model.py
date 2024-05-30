from app import db
from werkzeug.security import generate_password_hash, check_password_hash
from secrets import token_urlsafe
from sqlalchemy import event, Column, Integer
from datetime import datetime
from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()


"""
    val01 : new_land_assessment
    val02 : new_bldg_assessment
    char01 : altid
    char02 :docket number
"""
class NOAParid_Change_Orders(Base):
    __tablename__ = "noa_parid_change_orders"
    parid = db.Column(db.String(30), nullable=True, primary_key=True, unique=True)
    jur = db.Column(db.String(6), nullable=True)
    repaired_flag = db.Column(db.String(1), nullable=True)
    apr_land = db.Column(db.Integer, default=0)
    apr_bldg = db.Column(db.Integer, default=0)
    new_parid = db.Column(db.String(30), nullable=True)
    val01 = db.Column(db.Integer, default=0)
    val02 =  db.Column(db.Integer, default=0)
    char01 = db.Column(db.String(100), nullable=True)
    char02 = db.Column(db.String(100), nullable=True)
    char03 = db.Column(db.String(100), nullable=True)
    char04 = db.Column(db.String(100), nullable=True)
    char05 = db.Column(db.String(100), nullable=True)
    taxyr = db.Column(db.Integer, nullable=True)
    who = db.Column(db.String(20), nullable=True)
 