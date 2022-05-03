from calendar import month
import uuid
from flask import Response, jsonify, request, session
from app.models import Drug, Description, Manufacturer, Non_clinical_info, Overdose, Pharmaceutical_info, Pharmacodynamic_properties, Pharmacokinetic_properties, Special_population, Clinical_trial_data, Clinical_info,Users,Token,ClientDetails
from app import db
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime, timedelta

def greet():
    return "Hello, World!"


def newuser():
    '''add new users or signup '''
    data = request.get_json()
    p=generate_password_hash(data['password'])
    user=Users(
        firstname=data['firstname'],
        lastname=data['lastname'],
        username=data['username'],
        password=p,
        email=data['email'],
        telephone=data['telephone']
    )
    try:
        #raise Exception('some error') 
        u = Users.query.filter_by(username=user.username).first()
        e=Users.query.filter_by(email=user.email).first()
        t=Users.query.filter_by(telephone=user.telephone).first()
        if u is not None:
            
            raise Exception('use a different username')
        
        elif e is not None:
            raise Exception('use a different email')
            
        
        elif t is not None:
            raise Exception('use a different phone number')
            
        else:
            db.session.add(user)
            db.session.commit()

            return{
                'id':user.id, 'firstname':user.firstname, 'lastname':user.lastname, 'email':user.email, 'telephone':user.telephone
            },201
    except Exception as e:
        print (e)
        
        resp = Response({"username or email or telephone number already in use."}, status=500, mimetype='application/json')
        return resp


def login():
    '''user login'''
    data = request.get_json()
    user = Users.query.filter_by(username=data['username']).first()
    #print(user.password)
    print(data['password'])
    p=data['password']
    #print(check_password_hash(user.password,p))
    if user and check_password_hash(user.password, p):
        session['loggedin'] = True
        session['id'] = user.id
        session['username'] = user.username
        return('login success'),201
    else:
        return jsonify('error'),501

def logout():
    '''logout user'''
    if session['loggedin'] is not False:
        session['loggedin'] = False
        session.pop('id')
        session.pop('username')
        
        return("you're now logged out"),200
    else:
        return("already logged out"),500


def token():
    data = request.get_json()
    tk = str(uuid.uuid4())

    current_date = datetime.now(tz=None)
    expiry = current_date + timedelta(days=90)


    if session['id'] is not None:

        #check if user has an active token and take action accordingly
        is_active=Token.query.filter_by(user_id=session['id'],status='active').first()
       

        if is_active is not None:
            #set status of the last token to expired
            is_active.status='expired'

        token = Token(
            token=tk,
            expiry=expiry,
            user_id=session['id']


        )

        db.session.add(token)
        db.session.commit()
        session['token'] = tk

        return{
            'id': token.id,  'token': token.token, 'user_id': token.user_id
        }, 201
    
    else:
        return('you are currently logged out, please log in'),500


def clientdetails():
    '''client device provides details for tracking purposes'''
    data = request.get_json()
    token=request.headers['TOKEN']
    t=Token.query.filter_by(token=token).first()
    is_expired=t.status

    if data is not None:
        if token and is_expired=='active':
            clientdetails = ClientDetails(
                ip=data['ip'],
                useragent=data['useragent']
            )

            db.session.add(clientdetails)
            db.session.commit()

            return{
                'id': clientdetails.id, 'ip': clientdetails.ip, 'useragent': clientdetails.useragent
            },201
        else:
            return('no token provided or token has expired')
    else:
        return('provide data to insert')


def drug():
    '''enter basic drug details here'''
    data = request.get_json()
    token = request.headers['TOKEN']

    t=Token.query.filter_by(token=token).first()

    is_expired=t.status
    
    if data:
        if 'name' in data:
            if token and is_expired == 'active':
                drug = Drug(
                    name=data['name'],
                    barcode=data['barcode'],
                    qrcode=data['qrcode'],
                    img=data['img']
                )
                db.session.add(drug)
                db.session.commit()

                return{
                    'id': drug.id, 'name': drug.name, 'barcode': drug.barcode, 'qrcode': drug.qrcode, 'img': drug.img
                }, 201
            else:
                return jsonify('no token provided or token has expired'),500
        
        else:
            return jsonify('provide name of drug'),500
    else:
        return jsonify('provide data to insert')




def description():
    '''enter some drug descriptions here'''
    data = request.get_json()
    token=request.headers['TOKEN']
    t=Token.query.filter_by(token=token).first()
    is_expired =t.status

    if data is not None:
        if token and is_expired =='active':

            description = Description(
                color=data['color'],
                gram=data['gram'],
                shape=data['shape'],
                extra_details=data['extra_details'],
                drug_id=data['drug_id']

            )

            db.session.add(description)
            db.session.commit()

            return{
                'id': description.id, 'color': description.color, 'gram': description.gram, 'shape': description.shape, 'extra_details': description.extra_details, 'drug_id': description.drug_id
            }, 201
        else:
            return('no token provided or token expired'),500
    else:
        return('provide data to insert'),500



def manufacturer():
    '''enter manufacturer details here'''
    data = request.get_json()
    token=request.headers['TOKEN']
    t=Token.query.filter_by(token=token).first()
    is_expired=t.status

    if data is not None:
        if token and is_expired =='active':
            
            
            #drug_id = Manufacturer.query.filter_by(drug_id=data.drug_id ).first()
            try:
                manufacturer = Manufacturer(
                    name=data['name'],
                    address=data['address'],
                    drug_id=data['drug_id']

                )

                db.session.add(manufacturer)
                db.session.commit()

                return{
                    'id': manufacturer.id, 'name': manufacturer.name, 'address': manufacturer.address
                }, 201
            except:
                return jsonify('drug manufacturer already exist, try editing instead'),500
            

        else:
            return('no token provided or token expired')
    else:
        return('provide data to insert')


def non_clinical_info():
    '''enter clinical information here'''
    data = request.get_json()
    token=request.headers['TOKEN']
    t=Token.query.filter_by(token=token).first()
    is_expired=t.status

    if data is not None:
        if token and is_expired=='active':


            non_clinical_info = Non_clinical_info(
                description=data['description'],
                carcinogenicity_mutagenicity=data['carcinogenicity_mutagenicity'],
                reproductive_toxicology=data['reproductive_toxicology'],
                feritlity=data['feritlity'],
                drug_id=data['drug_id']

            )

            db.session.add(non_clinical_info)
            db.session.commit()

            return{
                'id': non_clinical_info.id, 'description': non_clinical_info.description, 'carcinogenicity_mutagenicity': non_clinical_info.carcinogenicity_mutagenicity, 'reproductive_toxicology': non_clinical_info.reproductive_toxicology, 'feritlity': non_clinical_info.feritlity, 'drug_id': non_clinical_info.drug_id
            }, 201
        else:
            return('no token provided or token has expired')
    else:
        return('provide data to be inserted')


def overdose():
    '''enter overdose details here'''
    data = request.get_json()
    token = request.headers['TOKEN']
    t=Token.query.filter_by(token=token).first()
    is_expiry=t.status

    if data is not None:
        if token and is_expiry=='active':
            
            
            overdose = Overdose(
                description=data['description'],
                signs_symptoms=data['signs_symptoms'],
                treatment=data['treatment'],
                clinical_info_id=data['clinical_info_id']


            )

            db.session.add(overdose)
            db.session.commit()

            return{
                'id': overdose.id, 'description': overdose.description, 'signs_symptoms': overdose.signs_symptoms, 'treatment': overdose.treatment, 'clinical_info_id': overdose.clinical_info_id
            }, 201
            
        else:
            return('no token provided or token has expired'),500
    else:
        return('provide data to be inserted'),500


def pharmaceutical_info():
    '''enter pharmaceutical informaiton here'''
    data = request.get_json()
    token=request.headers['TOKEN']
    t= Token.query.filter_by(token=token).first()
    is_expiry=t.status

    if data is not None:
        if token and is_expiry=='acitve':
            pharmaceutical_info = Pharmaceutical_info(
                list_of_excipients=data['list_of_excipients'],
                storage_conditions=data['storage_conditions'],
                nature_content_ofContainer=data['treatment'],
                instruction_for_handling=data['instruction_for_handling'],
                instruction_for_disposal=data['instruction_for_disposal'],
                text_revision_date=data['text_revision_date'],
                drug_id=data['drug_id']


            )

            db.session.add(pharmaceutical_info)
            db.session.commit()

            return{
                'id': pharmaceutical_info.id, 'list_of_excipients': pharmaceutical_info.list_of_excipients, 'storage_conditions': pharmaceutical_info.storage_conditions, 'nature_content_ofContainer': pharmaceutical_info.nature_content_ofContainer, 'instruction_for_handling': pharmaceutical_info.instruction_for_handling, 'instruction_for_disposal': pharmaceutical_info.instruction_for_disposal, 'text_revision_date': pharmaceutical_info.text_revision_date, 'drug_id': pharmaceutical_info.drug_id
            }, 201
        else:
            return('no token provided or token has expired'),500
    else:
        return('provide data to be inserted'),500


def pharmacodynamic_props():
    '''enter pharmocodynamic properties here'''
    data = request.get_json()
    token=request.headers['TOKEN']
    t=Token.query.filter_by(token=token).first()
    is_expired=t.status

    if data is not None:
        if token and is_expired=='active':
            if Pharmacodynamic_properties.query.filter_by(drug_id=data['drug_id']).first() is None:


                pharmacodynamic_properties = Pharmacodynamic_properties(
                    description=data['description'],
                    mechanism_of_action=data['mechanism_of_action'],
                    drug_id=data['drug_id']
                )

                db.session.add(pharmacodynamic_properties)
                db.session.commit()

                return{
                    'id': pharmacodynamic_properties.id, 'description': pharmacodynamic_properties.description, 'mechanism_of_action': pharmacodynamic_properties.mechanism_of_action, 'drug_id': pharmacodynamic_properties.drug_id
                }, 201
            else:
                return jsonify('the specified drug already has pharmacodynamic properties')
        else:
            return('token not provided or token has expired'),500
    else:
        return('provide data to be inserted'),500


def pharmacokinetic_props():
    '''enter pharmacokinetic properties here'''
    data = request.get_json()
    token =request.headers['TOKEN']
    t=Token.query.filter_by(token=token).first()
    is_expired=t.status

    if data is not None:
        check_drug_id=Pharmacokinetic_properties.query.filter_by(drug_id=data['drug_id']).first()
        if check_drug_id==None:
            if token and is_expired=='active':
                pharmacokinetic_properties = Pharmacokinetic_properties(
                    description=data['description'],
                    absorption=data['absorption'],
                    distribution=data['distribution'],
                    metabolism=data['metabolism'],
                    elimination=data['elimination'],
                    steady_state_pharmacokinetics=data['steady_state_pharmacokinetics'],
                    drug_id=data['drug_id']


                )

                db.session.add(pharmacokinetic_properties)
                db.session.commit()

                return{
                    'id': pharmacokinetic_properties.id, 'description': pharmacokinetic_properties.description, 'absorption': pharmacokinetic_properties.absorption, 'distribution': pharmacokinetic_properties.distribution, 'metabolism': pharmacokinetic_properties.metabolism, 'elimination': pharmacokinetic_properties.elimination, 'steady_state_pharmacokinetics': pharmacokinetic_properties.steady_state_pharmacokinetics, 'drug_id': pharmacokinetic_properties.drug_id
                }, 201
            else:
                return jsonify('token not provided or token has expired')
        else:
            return('drug already has pharmacokinetic properties set')
    else:
        return('provide data to insert'),500


def special_population():
    '''enter special population details here'''
    data = request.get_json()
    token=request.headers['TOKEN']
    t=Token.query.filter_by(token=token).first()
    is_expired=t.status

    if data is not None:
        if token and is_expired=='active':
            check_clinical_info_id=Special_population.query.filter_by(clinical_info_id=data['clinical_info_id']).first()
            if check_clinical_info_id==None:
                special_population = Special_population(
                    name=data['name'],
                    description=data['description'],
                    clinical_info_id=data['clinical_info_id']


                )

                db.session.add(special_population)
                db.session.commit()

                return{
                    'id': special_population.id, 'name': special_population.name, 'description': special_population.description, 'clinical_info_id': special_population.clinical_info_id
                }, 201
            else:
                return jsonify('the clinical info record specified already has special population record set'),500
        else:
            return('no token provided or token expired')
    else:
        return('provide data to insert'),500


def clinical_trial_data():
    '''enter clinical trial data here'''
    data = request.get_json()
    token=request.headers['TOKEN']
    t=Token.query.filter_by(token=token).first()
    is_expired=t.status

    if data is not None:
        if token and is_expired=='active':
            clinical_trial_data = Clinical_trial_data(
                description=data['description'],
                clinical_info_id=data['clinical_info_id']


            )

            db.session.add(clinical_trial_data)
            db.session.commit()

            return{
                'id': clinical_trial_data.id,  'description': clinical_trial_data.description, 'clinical_info_id': clinical_trial_data.clinical_info_id
            }, 201
        else:
            return('no token provided or token has expired')
    else:
        return('provide data to insert')

def clinical_info():
    '''enter clinical info details here'''
    data = request.get_json()
    token=request.headers['TOKEN']
    t=Token.query.filter_by(token=token).first()
    is_expired=t.status

    if data is not None:
        if token and is_expired=='active':
            clinical_info = Clinical_info(
                cli_id=data['cli_id'],
                indication=data['indication'],
                dosage=data['dosage'],
                administration=data['administration'],
                contrindication=data['contrindication'],
                interaction=data['interaction'],
                fertility=data['fertility'],
                warning_precaution=data['warning_precaution'],
                adverse_reaction=data['adverse_reaction'],
                drug_id=data['drug_id']


            )

            db.session.add(clinical_info)
            db.session.commit()

            return{
                'id': clinical_info.id, 'cli_id': clinical_info.cli_id, 'indication': clinical_info.indication, 'dosage': clinical_info.dosage, 'administration': clinical_info.administration, 'contrindication': clinical_info.contrindication, 'interaction': clinical_info.interaction, 'fertility': clinical_info.fertility, 'warning_precaution': clinical_info.warning_precaution, 'adverse_reaction': clinical_info.adverse_reaction, 'drug_id': clinical_info.drug_id
            }, 201
        else:
            return('no token provided or token has expired'),500
    else:
        return('provide data to insert'),500

