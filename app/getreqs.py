from time import timezone
from flask import Response, jsonify, request, session
from app import app
from app.models import Drug, Description, Manufacturer, Non_clinical_info, Overdose, Pharmaceutical_info, Pharmacodynamic_properties, Pharmacokinetic_properties, Special_population, Clinical_trial_data, Clinical_info,Users,Token,ClientDetails



def drugs():
    '''view all drug details'''
    token=request.headers['TOKEN']
    t=Token.query.filter_by(token=token).first()
    is_expiry=t.status

    if token and is_expiry=='active':
        drug = Drug.query.all()
        data_all = []

        for count in drug:
            # prepare visual data
            data_all.append([count.id, count.name, count.barcode, count.qrcode, count.img])

        return jsonify(data_all)
    else:
        resp = Response({"no token provided or token has expired."}, status=500, mimetype='application/json')
        return resp



def drug_item(item):
    '''view a single drug item details'''
    token=request.headers['TOKEN']
    t=Token.query.filter_by(token=token).first()
    is_expiry=t.status

    if token and is_expiry=='active':
        drug_id_or_name=item
        
        if drug_id_or_name.isdigit():
            id=int(drug_id_or_name)
            drug=Drug.query.filter_by(id=id).first()

            return{
                    'id': drug.id, 'name': drug.name, 'barcode': drug.barcode, 'qrcode': drug.qrcode, 'img': drug.img, 'ua':request.headers.get('User-Agent'), 'ip':request.remote_addr
                }, 201
        else:
            name=drug_id_or_name
            drug = Drug.query.filter_by(name=name).first()

            return{
                    'id': drug.id, 'name': drug.name, 'barcode': drug.barcode, 'qrcode': drug.qrcode, 'img': drug.img, 'ua':request.headers.get('User-Agent'), 'ip':request.remote_addr
                }, 201
    else:
        
        return jsonify('no token provided or token has expired'),500

def token():
    '''view user token'''
    id=session['id']
    
    
    if id:
        token=Token.query.filter_by(user_id=id).first()
        print(token)
        is_expired=token.status

        if is_expired=='active':
            return jsonify(token.token)
        else:
            return jsonify('token has expired'),500
    else:
        return jsonify("you're logged out, login to continue"),500



def users():
    '''view user details'''
    print(session['username'])
    id =session['id']
    if id:
        user=Users.query.filter_by(id=id).first()
        if user:
            return jsonify({
                    'id':user.id, 'firstname':user.firstname, 'lastname':user.lastname, 'email':user.email, 'telephone':user.telephone
                }),201
        else:
            return jsonify('user does not exist'),500
    else:
        return jsonify('you\'re logged out. login to proceed.')



def descriptions():
    '''view all drugs description'''
    token=request.headers['TOKEN']
    t=Token.query.filter_by(token=token).first()
    is_expiry=t.status

    if token and is_expiry=='active':
        description = Description.query.all()
        data_all = []

        for count in description:
            # prepare visual data
            data_all.append([count.id, count.color, count.gram, count.shape, count.extra_details,count.drug_id])

        return jsonify(data_all)
    else:
        resp = Response({"no token provided or token has expired."}, status=500, mimetype='application/json')
        return resp


def description(dr_id):
    '''view a single drugs description item'''
    token=request.headers['TOKEN']
    t=Token.query.filter_by(token=token).first()
    is_expiry=t.status


    if token and is_expiry=='active':
        description_item = Description.query.filter_by(drug_id=int(dr_id)).first()
        
        if description_item is not None:
            return{
                    'id': description_item.id, 'color': description_item.color, 'gram': description_item.gram, 'extra_details': description_item.extra_details, 'drug_id': description_item.drug_id
                }, 201
        else:
            return jsonify('invalid drug id'),500    
    else:
        resp = jsonify("no token provided or token has expired."),500
        return resp



def manufacturers():
    '''view all drug manufacturer details'''
    token=request.headers['TOKEN']
    t=Token.query.filter_by(token=token).first()
    is_expiry=t.status
    if token and is_expiry=='active':
        try:
            manufacturers=Manufacturer.query.all()
            data_all=[]
            for count in manufacturers:
                data_all.append([count.id, count.name, count.address, count.drug_id])
            return jsonify(data_all)
        except TypeError:
            return jsonify('no items in manufacturers'),500
    else :
        return jsonify('no token provided or token has expired.'),500

def manufacturer(drug_id):
    '''view a single instance of a manufacturer'''
    token=request.headers['TOKEN']
    t=Token.query.filter_by(token=token).first()
    is_expiry=t.status
    if token and is_expiry=='active':
        manufacturer=Manufacturer.query.filter_by(drug_id=drug_id).first()
        if manufacturer:
            return{
                    'id': manufacturer.id, 'name': manufacturer.name, 'address': manufacturer.address, 'drug_id': manufacturer.drug_id
                }, 201
        else:
            return jsonify('invalid drug id'),500
    else:
        resp = jsonify("no token provided or token has expired."),500
        return resp

def non_clinical_infos():
    '''view all the non clinical info details of the various drugs'''
    token=request.headers['TOKEN']
    t=Token.query.filter_by(token=token).first()
    is_expiry=t.status
    if token and is_expiry=='active':
        non_clinical_infos=Non_clinical_info.query.all()
        data_all=[]
        for count in non_clinical_infos:
            data_all.append([count.id, count.description, count.carcinogenicity_mutagenicity, count.reproductive_toxicology, count.feritlity, count.drug_id])
        return jsonify(data_all),201
    else :
        return jsonify('no token provided or token has expired.'),500

def non_clinical_info(drug_id):
    '''view a single non clinical info about a particular drug'''
    token=request.headers['TOKEN']
    t=Token.query.filter_by(token=token).first()
    is_expiry=t.status
    if token and is_expiry=='active':
        non_clinical_info=Non_clinical_info.query.filter_by(drug_id=drug_id).first()
        if non_clinical_info:
            return{
                    'id': non_clinical_info.id, 'description': non_clinical_info.description, 'carcinogenicity_mutagenicity':non_clinical_info.carcinogenicity_mutagenicity,'reproductive_toxicology':non_clinical_info.reproductive_toxicology,'feritlity':non_clinical_info.feritlity, 'drug_id': non_clinical_info.drug_id
                }, 201
        else:
            return jsonify('invalid drug id'),500
    else:
        resp = jsonify("no token provided or token has expired."),500
        return resp

def overdose():
    '''view all the overdose details of the various drugs'''
    token=request.headers['TOKEN']
    t=Token.query.filter_by(token=token).first()
    is_expiry=t.status
    if token and is_expiry=='active':
        overdose=Overdose.query.all()
        data_all=[]
        if overdose:
            for count in overdose:
                data_all.append([count.id,count.description,count.signs_symptoms,count.treatment,count.clinical_info_id])
            return jsonify(data_all)
        else:
            return jsonify('invalid drug clinical_info_id'),500
    else:
        resp = jsonify("no token provided or token has expired."),500
        return resp


def overdose_item(clinical_info_id):
    '''view a single drug overdose item'''
    token=request.headers['TOKEN']
    t=Token.query.filter_by(token=token).first()
    is_expiry=t.status
    if token and is_expiry=='active':
        overdose = Overdose.query.filter_by(clinical_info_id=clinical_info_id).first()
        if overdose is not None:
            return{
                    'id': overdose.id, 'description': overdose.description, 'signs_symptoms':overdose.signs_symptoms,'treatment':overdose.treatment,'clinical_info_id':overdose.clinical_info_id
                }, 201
        else:
            return jsonify('invalid  clinical_info_id'),500
    else:
        resp = jsonify("no token provided or token has expired."),500
        return resp
        


def clinical_infos():
    '''view all clinical info records for the various drugs'''
    token=request.headers['TOKEN']
    t=Token.query.filter_by(token=token).first()
    is_expiry=t.status
    if token and is_expiry=='active':
        clinical_info=Clinical_info.query.all()
        data_all=[]
        if clinical_info:
            for count in clinical_info:
                data_all.append([count.cli_id, count.indication, count.dosage, count.administration, count.contrindication, count.interaction, count.fertility, count.warning_precaution, count.adverse_reaction, count.drug_id])
            return jsonify(data_all)
        else:
            return jsonify('invalid drug clinical_info_id'),500
    else:
        resp = jsonify("no token provided or token has expired."),500
        return resp


def clinical_info(drug_id):
    '''view a single clinical info about a particular drug'''
    token=request.headers['TOKEN']
    t=Token.query.filter_by(token=token).first()
    is_expiry=t.status
    if token and is_expiry=='active':
        clinical_info=Clinical_info.query.filter_by(drug_id=drug_id).first()
        if clinical_info:
            return{
                    'cli_id': clinical_info.cli_id, 'indication': clinical_info.indication, 'dosage':clinical_info.dosage,'administration':clinical_info.administration,'contrindication':clinical_info.contrindication,'interaction':clinical_info.interaction, 'fertility':clinical_info.fertility, 'warning_precaution':clinical_info.warning_precaution, 'adverse_reaction':clinical_info.adverse_reaction, 'drug_id': clinical_info.drug_id
                }, 201
        else:
            return jsonify('invalid  drug_id'),500
    else:
        resp = jsonify("no token provided or token has expired."),500
        return resp


def clinical_trial_data():
    '''view all clinical trial data about a particular drug'''
    token=request.headers['TOKEN']
    t=Token.query.filter_by(token=token).first()
    is_expiry=t.status
    if token and is_expiry=='active':
        clinical_trial_data=Clinical_trial_data.query.all()
        data_all=[]
        if clinical_trial_data:
            for count in clinical_trial_data:
                data_all.append([count.id, count.description, count.clinical_info_id])
            return jsonify(data_all)
        else:
            return jsonify('invalid drug_id'),500
    else:
        resp = jsonify("no token provided or token has expired."),500
        return resp


def clinical_trial_data_item(clinical_info_id):
    '''view all clinical trial data about a particular drug'''
    token=request.headers['TOKEN']
    t=Token.query.filter_by(token=token).first()
    is_expiry=t.status
    if token and is_expiry=='active':
        clinical_trial_data=Clinical_trial_data.query.filter_by(clinical_info_id=clinical_info_id).first()
        if clinical_trial_data:
            return{
                    'id': clinical_trial_data.id, 'description': clinical_trial_data.description
                }, 201
        else:
            return jsonify('invalid  clinical_info_id'),500
    else:
        resp = jsonify("no token provided or token has expired."),500
        return resp



def special_population():
    '''view all special population data about the various drugs'''
    token=request.headers['TOKEN']
    t=Token.query.filter_by(token=token).first()
    is_expiry=t.status
    if token and is_expiry=='active':
        special_population=Special_population.query.all()
        data_all=[]
        if special_population:
            for count in special_population:
                data_all.append([count.id, count.name, count.description, count.clinical_info_id])
            return jsonify(data_all)
        else:
            return jsonify('invalid clinical_info_id'),500
    else:
        resp = jsonify("no token provided or token has expired."),500
        return resp


def special_population_item(clinical_info_id):
    '''view a single special population data about a particular drugs'''
    token=request.headers['TOKEN']
    t=Token.query.filter_by(token=token).first()
    is_expiry=t.status
    if token and is_expiry=='active':
        special_population=Special_population.query.filter_by(clinical_info_id=clinical_info_id).first()
        if special_population:
            return{
                    'id': special_population.id, 'name': special_population.name, 'description':special_population.description, 'clinical_info_id':special_population.clinical_info_id
                }, 201
        else:
            return jsonify('invalid  clinical_info_id'),500
    else:
        resp = jsonify("no token provided or token has expired."),500
        return resp



def pharmaceutical_info():
    '''view all pharmaceutical info about the various drugs'''
    token=request.headers['TOKEN']
    t=Token.query.filter_by(token=token).first()
    is_expiry=t.status
    if token and is_expiry=='active':
        pharmaceutical_info=Pharmaceutical_info.query.all()
        data_all=[]
        if pharmaceutical_info:
            for count in pharmaceutical_info:
                data_all.append([count.id, count.list_of_excipients, count.storage_conditions, count.nature_content_ofContainer, count.instruction_for_handling, count.instruction_for_disposal, count.text_revision_date, count.drug_id])
            return jsonify(data_all)
        else:
            return jsonify('invalid drug_id'),500
    else:
        resp = jsonify("no token provided or token has expired."),500
        return resp




def pharmaceutical_info_item(drug_id):
    '''view a single pharmaceutical info about a particular drug'''
    token=request.headers['TOKEN']
    t=Token.query.filter_by(token=token).first()
    is_expiry=t.status
    if token and is_expiry=='active':
        pharmaceutical_info=Pharmaceutical_info.query.filter_by(drug_id=drug_id).first()
        if special_population:
            return{
                    'id': pharmaceutical_info.id, 'list_of_excipients': pharmaceutical_info.list_of_excipients, 'storage_conditions':pharmaceutical_info.storage_conditions, 'nature_content_ofContainer':pharmaceutical_info.nature_content_ofContainer,'instruction_for_handling':pharmaceutical_info.instruction_for_handling,'instruction_for_disposal':pharmaceutical_info.instruction_for_disposal,'text_revision_date':pharmaceutical_info.text_revision_date,'drug_id':pharmaceutical_info.drug_id
                }, 201
        else:
            return jsonify('invalid  drug_id'),500
    else:
        resp = jsonify("no token provided or token has expired."),500
        return resp
    


def pharmacodynamic_props():
    '''view all pharmacodynamic properties info about the various drugs'''
    token=request.headers['TOKEN']
    t=Token.query.filter_by(token=token).first()
    is_expiry=t.status
    if token and is_expiry=='active':
        pharmacodynamic_props=Pharmacodynamic_properties.query.all()
        data_all=[]
        if pharmacodynamic_props:
            for count in pharmacodynamic_props:
                data_all.append([count.id, count.description, count.mechanism_of_action, count.drug_id])
            return jsonify(data_all)
        else:
            return jsonify('invalid drug_id'),500
    else:
        resp = jsonify("no token provided or token has expired."),500
        return resp



def pharmacodynamic_prpos_item(drug_id):
    '''view a single pharmacodynamic properties info about a particular drug'''
    token=request.headers['TOKEN']
    t=Token.query.filter_by(token=token).first()
    is_expiry=t.status
    if token and is_expiry=='active':
        pharmacodynamic_props=Pharmacodynamic_properties.query.filter_by(drug_id=drug_id).first()
        if pharmacodynamic_props:
            return{
                    'id': pharmacodynamic_props.id, 'description': pharmacodynamic_props.description, 'mechanism_of_action':pharmacodynamic_props.mechanism_of_action, 'drug_id':pharmacodynamic_props.drug_id
                }, 201
        else:
            return jsonify('invalid  drug_id'),500
    else:
        resp = jsonify("no token provided or token has expired."),500
        return resp



def pharmacokinetic_props():
    '''view all pharmacokinetic properties info about the various drugs'''
    token=request.headers['TOKEN']
    t=Token.query.filter_by(token=token).first()
    is_expiry=t.status
    if token and is_expiry=='active':
        pharmacokinetic_props=Pharmacokinetic_properties.query.all()
        data_all=[]
        if pharmacokinetic_props:
            for count in pharmacokinetic_props:
                data_all.append([count.id, count.description, count.absorption, count.distribution, count.metabolism, count.elimination, count.steady_state_pharmacokinetics, count.drug_id])
            return jsonify(data_all)
        else:
            return jsonify('invalid drug_id'),500
    else:
        resp = jsonify("no token provided or token has expired."),500
        return resp



def pharmacokinetic_props_item(drug_id):
    '''view a single pharmacokinetic properties info about a particular drug'''
    token=request.headers['TOKEN']
    t=Token.query.filter_by(token=token).first()
    is_expiry=t.status
    if token and is_expiry=='active':
        pharmacokinetic_props=Pharmacokinetic_properties.query.filter_by(drug_id=drug_id).first()
        if pharmacokinetic_props:
            return{
                    'id': pharmacokinetic_props.id, 'description': pharmacokinetic_props.description, 'absorption':pharmacokinetic_props.absorption, 'distribution':pharmacokinetic_props.distribution, 'metabolism':pharmacokinetic_props.metabolism, 'elimination':pharmacokinetic_props.elimination, 'steady_state_pharmacokinetics':pharmacokinetic_props.steady_state_pharmacokinetics, 'drug_id':pharmacokinetic_props.drug_id
                }, 201
        else:
            return jsonify('invalid  drug_id'),500
    else:
        resp = jsonify("no token provided or token has expired."),500
        return resp



