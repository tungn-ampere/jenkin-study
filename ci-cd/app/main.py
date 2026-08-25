from flask import Flask

app = Flask(__name__)

@app.get("/")
def home():
    return {"message": "Hello CI/CD"}

@app.get("/health")
def health():
    return {"status": "okla"}

@app.get("/version")
def version():
    return {"version": "1.0.1"}

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)