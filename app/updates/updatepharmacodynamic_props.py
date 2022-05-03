from flask import jsonify, request
from app.models import Pharmacodynamic_properties, Token
from app import db

def updatePharmacodynamic():
    '''update pharmacodynamic properties record'''
    data = request.get_json()
    token = request.headers['TOKEN']
    id=int(data['id'])
    

    t=Token.query.filter_by(token=token).first()

    is_expired=t.status
    
    

    if data:
        if id is not None:
            if token and is_expired == 'active':
                old_data=Pharmacodynamic_properties.query.filter_by(id=id).first()
                
                if old_data is not None:
                    
                    old_data.description=data['description'],
                    old_data.mechanism_of_action=data['mechanism_of_action'],
                   
                            
                    db.session.add(old_data)
                    db.session.commit()

                    return{
                        'id': old_data.id, 'description': old_data.description, 'mechanism_of_action': old_data.mechanism_of_action, 'drug_id': old_data.drug_id
                }, 201
          
                else:
                    return jsonify('Drug pharmacodynamic properties record specified does not exist'),500
            else:
                return jsonify('no token provided or token has expired'),500
        else:
            return jsonify('No pharcodynamic properties id provided'),500
    return jsonify('Provide new pharmacodynamic properties records for update'),500
                