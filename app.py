from flask import Flask,jsonify,request
from werkzeug.security import generate_password_hash, check_password_hash
from models import init_db, get_db_connection
import jwt
from datetime import datetime, timedelta
from config import SECRET_KEY
from auth import token_required
app=Flask(__name__)
# Routes
# home route
@app.route("/")
def home():
    return jsonify({"message":"Auth API running"})
# Signup route
@app.route("/signup",methods=["POST"])
def sign_up():
    data=request.get_json()
    if not data or "username" not in data or "email" not in data or "password" not in data:
        return jsonify({"error":"every input field must be filled"}),400
    conn=get_db_connection()
    user=conn.execute("SELECT * FROM users WHERE username=? OR email=?",(data["username"],data["email"],)).fetchone()
    # if user is not None:
    if user:
        conn.close()
        return jsonify({"error":"Username or email already exist"}),409
    hash=generate_password_hash(data["password"])
    conn.execute("INSERT INTO users (username, email, password_hash) VALUES(?,?,?)",(data["username"],data["email"],hash,))
    conn.commit()
    conn.close()
    return jsonify({"message":"User created successfully"}),201
# Login route
@app.route("/login",methods=["POST"])
def login():
    data=request.get_json()
    if not data or "username" not in data or "password" not in data:
        return jsonify({"error":"username and password are required"}),400
    conn=get_db_connection()
    user=conn.execute("SELECT * FROM users WHERE username=?",(data["username"],)).fetchone()
    if user is None:
        conn.close()
        return jsonify({"error":"user not found"}),404
    check_password=check_password_hash(user["password_hash"],data["password"])
    if check_password is False:
        conn.close()
        return jsonify({"message":"invalid credentials"}),401
# payload means user's info
    payload={
        "user_id":user["id"],
        "username":user["username"],
        "exp":datetime.utcnow() + timedelta(hours=1)
        }
# token generation
    token=jwt.encode(payload,SECRET_KEY,algorithm="HS256")
    conn.close()
# return response
    return jsonify({"token":token}),200
# Profile route
@app.route("/profile",methods=["GET"])
@token_required
def profile(payload):
    user_id=payload["user_id"]
    conn=get_db_connection()
    response=conn.execute("SELECT username, email FROM users WHERE id=?",(user_id,)).fetchone()
    if response is None:
        conn.close()
        return jsonify({"error":"User not found"}),404
    conn.close()
    return jsonify({"username":response["username"],"email":response["email"]})
# User route - get all user
@app.route("/users",methods=["GET"])
def get_all_users():
    conn=get_db_connection()
    users=conn.execute("SELECT username, email FROM users").fetchall()
    if not users:
        conn.close()
        return jsonify({"error":"no user found"}),404
    users_list=[{"username":user["username"],"email":user["email"]} for user in users]
    conn.close()
    return jsonify(users_list)
# Entry point
if __name__=="__main__":
    init_db()
    app.run(debug=True)