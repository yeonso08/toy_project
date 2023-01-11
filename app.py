from flask import Flask, render_template, request, jsonify
app = Flask(__name__)

from pymongo import MongoClient
import certifi

ca = certifi.where()

client = MongoClient('mongodb+srv://test:sparta@cluster0.gvsa3p3.mongodb.net/Cluster0?retryWrites=true&w=majority', tlsCAFile=ca)
db = client.dbsparta

@app.route('/')
def home():
    return render_template('index.html')
@app.route('/pets2')
def home2():
    return render_template('index2.html')


@app.route("/pets", methods=["POST"])
def web_pets_post():
    name_receive = request.form['name_give']
    age_receive = request.form['age_give']
    phone_number_receive = request.form['phone_number_give']
    address_receive = request.form['address_give']
    reason_receive = request.form['reason_give']
    doc = {
        'name':name_receive,
        'age':age_receive,
        'phone_number':phone_number_receive,
        'address':address_receive,
        'reason':reason_receive
    }
    db.pets.insert_one(doc)

    return jsonify({'msg': '신청되었습니다'})


@app.route("/pets", methods=["GET"])
def web_pets_get():
    pets_list = list(db.pets.find({},{'_id':False}))
    return jsonify({'pets':pets_list})

if __name__ == '__main__':
    app.run('0.0.0.0', port=4000, debug=True)