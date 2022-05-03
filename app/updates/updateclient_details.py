import uuid
from flask import Response, jsonify, request, session
from app.models import Drug, Description, Manufacturer, Non_clinical_info, Overdose, Pharmaceutical_info, Pharmacodynamic_properties, Pharmacokinetic_properties, Special_population, Clinical_trial_data, Clinical_info,Users,Token,ClientDetails
from app import db

