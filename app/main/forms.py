from flask import flash
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, IntegerField, SelectField, DateTimeField
from wtforms.validators import ValidationError, DataRequired, EqualTo
from app.models import Train, Voiture, Gare
from app import db
from datetime import datetime


class RechercheTrajet(FlaskForm):
    gareDepart = SelectField("Gare de départ", coerce=int, validators=[DataRequired()], choices=[])
    gareArrivee = SelectField("Gare d'arrivée", coerce=int, validators=[DataRequired()], choices=[])
    submit = SubmitField("Rechercher")


class AcheterReduction(FlaskForm):
    reduction = SelectField("Reduction", coerce=int, validators=[DataRequired()])
    submit = SubmitField("Acheter")


class RechargerArgent(FlaskForm):
    recharge = IntegerField("€", validators=[DataRequired()])
    submit = SubmitField("Recharger")


class ChoisirPlace(FlaskForm):
    classe = SelectField("Classe", coerce=bool, choices=[(0, '2nde classe'), (1, '1ere classe')])
    voiture = SelectField("Voiture", coerce=int, validators=[DataRequired()], choices=[])
    place = SelectField("Place", coerce=int, validators=[DataRequired()], choices=[])
    submit = SubmitField("Acheter")


