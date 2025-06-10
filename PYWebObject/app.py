from flask import Flask, render_template,request,jsonify

app = Flask(__name__)

#模拟用户数据
VALID_USERNAME = "admin"
VALID_PASSWORD = "123"

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/login",methods = ["GET","POST"])
def login():
    data = request.get_json()
    username = data.get("username")
    password = data.get("password")
    if username == VALID_USERNAME and password == VALID_PASSWORD:
        return jsonify({"success":True, "message":"登录成功"})
    else:
        return jsonify({"success":False,"message":"用户名或密码错误"})

if __name__ == "__main__":
    app.run(debug=True)








