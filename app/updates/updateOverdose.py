from flask import jsonify, request
from app.models import Overdose, Token
from app import db

def updateOverdose():
    '''update overdose record'''
    data = request.get_json()
    token = request.headers['TOKEN']
    id=int(data['id'])
    

    t=Token.query.filter_by(token=token).first()

    is_expired=t.status
    
    

    if data:
        if id is not None:
            if token and is_expired == 'active':
                old_data=Overdose.query.filter_by(id=id).first()
                
                if old_data is not None:
                    
                    old_data.description=data['description'],
                    old_data.signs_symptoms=data['signs_symptoms'],
                    old_data.treatment=data['treatment']
                        
                            
                    db.session.add(old_data)
                    db.session.commit()


                    return{
                        'id': old_data.id, 'description': old_data.description, 'signs_symptoms': old_data.signs_symptoms, 'treatment': old_data.treatment, 'clinical_info_id':old_data.clinical_info_id
                }, 201
          
                else:
                    return jsonify('Drug overdose record specified does not exist'),500
            else:
                return jsonify('no token provided or token has expired'),500
        else:
            return jsonify('No overdose id provided'),500
    return jsonify('Provide new overdose records for update'),500
                