from flask import jsonify, request
from app.models import Special_population, Token
from app import db

def deleteSpecailPopulation(id):
    '''delete special properties record'''
    
    token = request.headers['TOKEN']
    
    

    t=Token.query.filter_by(token=token).first()

    is_expired=t.status
    
    

    
    if id is not None:
        if token and is_expired == 'active':
            specialProps=Special_population.query.filter_by(id=id).first()
                
            if specialProps is not None:
                    
                db.session.delete(specialProps)
                db.session.commit()

                return jsonify('special population record deleted successfully'),201
          
            else:
                return jsonify('Special properties record specified does not exist'),500
        else:
            return jsonify('no token provided or token has expired'),500
    else:
        return jsonify('No special properties id provided'),500
    
                