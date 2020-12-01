from flask import Flask,jsonify,request
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello world'


@app.route('/reverser',methods = ['POST'])
def reverser():
    num = request.get_json().get("num")
    num = int(num[len(num)::-1])
    return jsonify({"num":num})



if __name__ == "__main__":
     app.run()