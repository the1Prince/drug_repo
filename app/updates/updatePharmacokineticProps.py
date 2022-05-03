from flask import jsonify, request
from app.models import Manufacturer, Pharmacokinetic_properties, Token
from app import db

def updatePharmacokinetic():
    '''update pharmacokinetic properties record'''
    data = request.get_json()
    token = request.headers['TOKEN']
    id=int(data['id'])
    

    t=Token.query.filter_by(token=token).first()

    is_expired=t.status
    
    

    if data:
        if id is not None:
            if token and is_expired == 'active':
                old_data=Pharmacokinetic_properties.query.filter_by(id=id).first()
                
                if old_data is not None:
                    
                    old_data.description=data['description'],
                    old_data.absorption=data['absorption'],
                    old_data.distribution=data['distribution'],
                    old_data.metabolism=data['metabolism'],
                    old_data.elimination=data['elimination'],
                    old_data.steady_state_pharmacokinetics=data['steady_state_pharmacokinetics'],
                    
                            
                    db.session.add(old_data)
                    db.session.commit()

                    return{
                    'id': old_data.id, 'description': old_data.description, 'absorption': old_data.absorption, 'distribution': old_data.distribution, 'metabolism': old_data.metabolism, 'elimination': old_data.elimination, 'steady_state_pharmacokinetics': old_data.steady_state_pharmacokinetics, 'drug_id': old_data.drug_id
                }, 201
          
                else:
                    return jsonify('Drug pharmacokinetic properties record specified does not exist'),500
            else:
                return jsonify('no token provided or token has expired'),500
        else:
            return jsonify('No pharmacokinetic properties id provided'),500
    return jsonify('Provide new pharmacokinetic properties records for update'),500
                