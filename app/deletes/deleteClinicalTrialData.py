from flask import jsonify, request
from app.models import Clinical_trial_data, Token
from app import db

def deleteClinicalTrialData(id):
    '''delete clinical trial data record'''
   
    token = request.headers['TOKEN']
    
    

    t=Token.query.filter_by(token=token).first()

    is_expired=t.status
    
    

    
    if id is not None:
        if token and is_expired == 'active':
            clinicalTrialData=Clinical_trial_data.query.filter_by(id=id).first()
                
            if clinicalTrialData is not None:
                    
                db.session.delete(clinicalTrialData)
                db.session.commit()

                return jsonify('clinical trial data deleted successfully'),201
          
            else:
                return jsonify('Clinical trial data record specified does not exist'),500
        else:
            return jsonify('no token provided or token has expired'),500
    else:
        return jsonify('No clinical trial data id provided'),500
    
                