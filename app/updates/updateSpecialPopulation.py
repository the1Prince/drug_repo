from flask import jsonify, request
from app.models import Special_population, Token
from app import db

def updateSpecialPopulation():
    '''update special population record'''
    data = request.get_json()
    token = request.headers['TOKEN']
    id=int(data['id'])
    

    t=Token.query.filter_by(token=token).first()

    is_expired=t.status
    
    

    if data:
        if id is not None:
            if token and is_expired == 'active':
                specialPopulation=Special_population.query.filter_by(id=id).first()
                
                if specialPopulation is not None:
                    
                    specialPopulation.name=data['name'],
                    specialPopulation.description=data['description'],
                        
                            
                    db.session.add(specialPopulation)
                    db.session.commit()
                    return{
                    'id': specialPopulation.id, 'name': specialPopulation.name, 'description': specialPopulation.description, 'clinical_info_id': specialPopulation.clinical_info_id
                }, 201
          
                else:
                    return jsonify('Drug special population record specified does not exist'),500
            else:
                return jsonify('no token provided or token has expired'),500
        else:
            return jsonify('No special population id provided'),500
    return jsonify('Provide new special population records for update'),500
                