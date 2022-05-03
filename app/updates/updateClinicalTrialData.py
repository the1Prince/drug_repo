from flask import jsonify, request
from app.models import Clinical_trial_data, Token
from app import db

def updateClinicalTrialData():
    '''update clinical trial data record'''
    data = request.get_json()
    token = request.headers['TOKEN']
    id=int(data['id'])
    

    t=Token.query.filter_by(token=token).first()

    is_expired=t.status
    
    

    if data:
        if id is not None:
            if token and is_expired == 'active':
                old_data=Clinical_trial_data.query.filter_by(id=id).first()
                
                if old_data is not None:
                    
                    old_data.description=data['description'],
                    
                            
                    db.session.add(old_data)
                    db.session.commit()

                    return{
                'id': old_data.id,  'description': old_data.description, 'clinical_info_id': old_data.clinical_info_id
            }, 201
          
                else:
                    return jsonify('Drug clinical trial data record specified does not exist'),500
            else:
                return jsonify('no token provided or token has expired'),500
        else:
            return jsonify('No clinical trial data id provided'),500
    return jsonify('Provide new clinical trial data records for update'),500
                