from flask import jsonify, request
from app.models import Pharmaceutical_info, Token
from app import db

def updatePharmaceuticalInfo():
    '''update pharmaceutical info record'''
    data = request.get_json()
    token = request.headers['TOKEN']
    id=int(data['id'])
    

    t=Token.query.filter_by(token=token).first()

    is_expired=t.status
    
    

    if data:
        if id in data and id is not None:
            if token and is_expired == 'active':
                
                if Pharmaceutical_info.query.filter_by(id=id).first() is not None:
                    pharmaceutical_info = Pharmaceutical_info(
                        list_of_excipients=data['list_of_excipients'],
                        storage_conditions=data['storage_conditions'],
                        nature_content_ofContainer=data['treatment'],
                        instruction_for_handling=data['instruction_for_handling'],
                        instruction_for_disposal=data['instruction_for_disposal'],
                        text_revision_date=data['text_revision_date'],
                        drug_id=data['drug_id']
                            )
                    db.session.add(pharmaceutical_info)
                    db.session.commit()
          
                else:
                    return jsonify('Drug pharmaceutical info record specified does not exist'),500
            else:
                return jsonify('no token provided or token has expired'),500
        else:
            return jsonify('No pharmaceutical info id provided'),500
    return jsonify('Provide new pharmaceutical info records for update'),500
                