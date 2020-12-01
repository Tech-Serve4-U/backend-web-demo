from flask import Flask,jsonify,request
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello world'


@app.route('/summation',methods = ['POST'])
def summation():
    num = request.get_json().get("num")
    sum = 0
    for i in num:
        sum += int(i)

    return jsonify({"sum":sum})

if __name__ == "__main__":
     app.run(host='0.0.0.0')
        
