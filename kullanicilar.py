#Kullanıcıları yönetmek için ir API oluştur. kullanıcıları eklemek, listelemek ve güncellemek için gerekli işlevleri yapmalı

from flask import Flask, jsonify
import requests
app = Flask(__name__)

users = []


#KULLANICI EKLEMEK İÇİN 
@app.route('/api/users',methods=['POST'])
def kullanici_ekle():  
    data = requests.get_json()
    user_id = data.get('id'),
    name = data.get('name'),
    email = data.get('email')

    if user_id in users:
        return jsonify({"error":'Name and email are required'}),400
    
    data['id'] = len(users)+1
    users.append(data)
    return jsonify(data),201        


#KULLANICILARI LİSTELEMEK İÇİN
@app.route('/api/users', methods=['GET'])
def kullanici_listele():
    return jsonify(users), 200
    

#KULLANICILARI GÜNCELLEMEK İÇİN 
@app.route('/api/users/<user_id>',methods = ['PUT'])
def kullanici_guncelle(user_id):
    data = requests.get_json()
    if user_id not in users:
        return jsonify({"error": "User not found"}), 404

    name = data.get('name')
    email = data.get('email')

    if name is not None:
        users[user_id]['name'] = name
    if email is not None:
        users[user_id]['email'] = email

    return jsonify({"message": "User updated successfully"}), 200

if __name__ == '__main__':
    app.run(debug=True)
