from flask import Flask, request
from flask_restx import Api, Resource, fields
from datetime import datetime, timedelta
from jose import jwt, JWTError


SECRET_KEY = "MYSECRETKEY_1234"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MIN = 10

app = Flask(__name__)

authorizations = {
    "Bearer Auth": {
        "type": "apiKey",
        "in": "header",
        "name": "Authorization",
        "description": "Enter JWT token like: Bearer <JWT>"
    }
}

api = Api(
    app,
    version="1.0",
    title="Flask JWT API",
    description="JWT Authentication API with Swagger",
    doc="/docs",
    authorizations=authorizations,
    security=None  
)

def create_token(username):
    expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MIN)
    payload = {"sub": username, "exp": expire}
    return jwt.encode(payload, SECRET_KEY, algorithm=ALGORITHM)

def verify_token(token):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        return payload["sub"]
    except JWTError:
        return None


login_model = api.model("Login", {
    "username": fields.String(required=True),
    "password": fields.String(required=True)
})

@api.route("/login")
class Login(Resource):
    @api.expect(login_model)
    def post(self):
        data = request.json
        username = data.get("username")
        password = data.get("password")

        if username == "admin" and password == "1234":
            token = create_token(username)
            return {"access_token": token}

        return {"error": "Invalid credentials"}, 401


@api.route("/secure_data")
class SecureData(Resource):
    @api.doc(security="Bearer Auth")
    def get(self):
        auth_header = request.headers.get("Authorization")
        if not auth_header or not auth_header.lower().startswith("bearer "):
            return {"error": "Token missing"}, 400

        token = auth_header.split(" ")[1]

        username = verify_token(token)
        if not username:
            return {"error": "Invalid or expired token"}, 401

        return {"message": f"Hello {username}, this is secure data"}


@app.route("/")
def home():
    return "Flask JWT App Running. Visit /docs for Swagger UI."

if __name__ == "__main__":
    app.run(debug=True)
