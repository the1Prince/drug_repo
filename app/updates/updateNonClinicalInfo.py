from flask import jsonify, request
from app.models import Non_clinical_info, Token
from app import db

def updateNonClinicalInfo():
    '''update non clinical info record'''
    data = request.get_json()
    token = request.headers['TOKEN']
    id=int(data['id'])
    

    t=Token.query.filter_by(token=token).first()

    is_expired=t.status
    
    

    if data:
        if id is not None:
            if token and is_expired == 'active':
                old_data=Non_clinical_info.query.filter_by(id=id).first()
                
                if old_data is not None:
                    
                    old_data.description=data['description'],
                    old_data.carcinogenicity_mutagenicity=data['carcinogenicity_mutagenicity'],
                    old_data.reproductive_toxicology=data['reproductive_toxicology'],
                    old_data.feritlity=data['feritlity']
                    
                            
                    db.session.add(old_data)
                    db.session.commit()

                    return{
                    'id': old_data.id, 'description': old_data.description, 'carcinogenicity_mutagenicity': old_data.carcinogenicity_mutagenicity, 'reproductive_toxicology': old_data.reproductive_toxicology, 'feritlity': old_data.feritlity, 'drug_id': old_data.drug_id
                }, 201
          
                else:
                    return jsonify('Drug non clinical info record specified does not exist'),500
            else:
                return jsonify('no token provided or token has expired'),500
        else:
            return jsonify('non clinical info id is not provided'),500
    return jsonify('Provide new non clinical info records for update'),500
                