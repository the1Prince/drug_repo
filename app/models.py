
from enum import unique
from app import db
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime


class Clinical_info(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    cli_id = db.Column(db.String(64))
    indication = db.Column(db.Text)
    dosage = db.Column(db.Text)
    administration = db.Column(db.Text)
    contrindication = db.Column(db.Text)
    interaction = db.Column(db.Text)
    fertility = db.Column(db.Text)
    warning_precaution = db.Column(db.Text)
    adverse_reaction = db.Column(db.Text)
    drug_id = db.Column(db.Text)


class Clinical_trial_data(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.Text)
    clinical_info_id = db.Column(db.Integer)


class Description(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    color = db.Column(db.String(64))
    gram = db.Column(db.Float)
    shape = db.Column(db.String(128))
    extra_details = db.Column(db.Text)
    drug_id = db.Column(db.Integer)


class Drug(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), index=True, unique=True)
    barcode = db.Column(db.String(64))
    qrcode = db.Column(db.String(128))
    img = db.Column(db.String(128))


class Manufacturer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64))
    address = db.Column(db.String(128))
    drug_id = db.Column(db.Integer, unique=True)


class Non_clinical_info(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.Text)
    carcinogenicity_mutagenicity = db.Column(db.Text)
    reproductive_toxicology = db.Column(db.Text)
    feritlity = db.Column(db.Text)
    drug_id = db.Column(db.Integer, unique=True)


class Overdose(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.Text)
    signs_symptoms = db.Column(db.Text)
    treatment = db.Column(db.Text)
    clinical_info_id = db.Column(db.Integer)


class Pharmaceutical_info(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    list_of_excipients = db.Column(db.Text)
    storage_conditions = db.Column(db.Text)
    nature_content_ofContainer = db.Column(db.Text)
    instruction_for_handling = db.Column(db.Text)
    instruction_for_disposal = db.Column(db.Text)
    text_revision_date = db.Column(db.Text)
    drug_id = db.Column(db.Integer)


class Pharmacodynamic_properties(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.Text)
    mechanism_of_action = db.Column(db.Text)
    drug_id = db.Column(db.Integer)


class Pharmacokinetic_properties(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.Text)
    absorption = db.Column(db.Text)
    distribution = db.Column(db.Text)
    metabolism = db.Column(db.Text)
    elimination = db.Column(db.Text)
    steady_state_pharmacokinetics = db.Column(db.Text)
    drug_id = db.Column(db.Integer)


class Special_population(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64))
    description = db.Column(db.Text)
    clinical_info_id = db.Column(db.Integer)


class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    firstname = db.Column(db.String(64))
    lastname=db.Column(db.String(64))
    username=db.Column(db.String(64),unique=True)
    password=db.Column(db.String())
    email=db.Column(db.String(64),unique=True)
    telephone=db.Column(db.String(15),unique=True)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

class Token(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    token=db.Column(db.String(128), unique=True)
    expiry=db.Column(db.DateTime)
    status = db.Column(db.String(20), default='active')
    user_id=db.Column(db.Integer)

class ClientDetails(db.Model):
    id=db.Column(db.Integer, primary_key=True)
    ip=db.Column(db.String(64))
    useragent=db.Column(db.String(128))
