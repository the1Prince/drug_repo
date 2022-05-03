from flask import jsonify, request
from app.models import Description, Token
from app import db

def updateDescription():
    '''update pharmacodynamic properties record'''
    data = request.get_json()
    token = request.headers['TOKEN']
    id=int(data['id'])
    

    t=Token.query.filter_by(token=token).first()

    is_expired=t.status
    
    

    if data:
        if id is not None:
            if token and is_expired == 'active':
                old_data=Description.query.filter_by(id=id).first()
                
                if old_data is not None:
                    
                    old_data.color=data['color'],
                    old_data.gram=data['gram'],
                    old_data.shape=data['shape'],
                    old_data.extra_details=data['extra_details'],
                    
                            
                    db.session.add(old_data)
                    db.session.commit()
                    return{
                        'id': old_data.id, 'color': old_data.color, 'gram': old_data.gram, 'shape': old_data.shape, 'extra_details': old_data.extra_details, 'drug_id': old_data.drug_id
                    }, 201
          
                else:
                    return jsonify('Drug description record specified does not exist'),500
            else:
                return jsonify('no token provided or token has expired'),500
        else:
            return jsonify('No description id provided'),500
    return jsonify('Provide new description records for update'),500
                