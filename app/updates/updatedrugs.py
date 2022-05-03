from flask import jsonify, request
from app.models import Drug, Token
from app import db

def updatedrugs():
    '''update drug name'''
    data = request.get_json()
    token = request.headers['TOKEN']
    name=data['name']
    
    

    t=Token.query.filter_by(token=token).first()

    is_expired=t.status
    
    

    if data:
        print(name)
        if name is not None:
            if token and is_expired == 'active':
                old_drugname=data['old_drugname']
                current_drug_record=Drug.query.filter_by(name=old_drugname).first()
                if current_drug_record is not None:
                    drug_name=Drug.query.filter_by(name=name).first()
                    if drug_name is None:
                        
                        current_drug_record.name=name,
                        current_drug_record.barcode=data['barcode'],
                        current_drug_record.qrcode=data['qrcode'],
                        current_drug_record.img=data['img']
                        
                        db.session.add(current_drug_record)
                        db.session.commit()

                        return{
                            'id': current_drug_record.id, 'name': current_drug_record.name, 'barcode': current_drug_record.barcode, 'qrcode': current_drug_record.qrcode, 'img': current_drug_record.img
                        }, 201
                    else:
                        return jsonify('drug already exists'),500
                else:
                    return jsonify('Drug does not exist, create new drug instead'),500
            else:
                return jsonify('no token provided or token has expired'),500
        else:
            return jsonify('no new drug name provided for updating a current drug'),500
    return jsonify('Provide new drug records for update'),500
                

                