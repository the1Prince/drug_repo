from flask import jsonify, request
from app.models import Manufacturer, Token
from app import db

def updateManufacturer():
    '''update manufacturer record'''
    data = request.get_json()
    token = request.headers['TOKEN']
    id=int(data['id'])
    

    t=Token.query.filter_by(token=token).first()

    is_expired=t.status
    
    

    if data:
        if id is not None:
            if token and is_expired == 'active':
                old_data=Manufacturer.query.filter_by(id=id).first()
                
                if old_data is not None:
                    
                    old_data.name=data['name'],
                    old_data.address=data['address']
                    
                            
                    db.session.add(old_data)
                    db.session.commit()
                    return{
                    'id': old_data.id, 'name': old_data.name, 'address': old_data.address
                }, 201
          
                else:
                    return jsonify('Drug manufacturer record specified does not exist'),500
            else:
                return jsonify('no token provided or token has expired'),500
        else:
            return jsonify('No manufacturer id provided'),500
    return jsonify('Provide new manufacturer records for update'),500
                