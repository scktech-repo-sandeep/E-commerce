from flask import Flask

app=Flask(__name__)

@app.route('/')
def get():
    return "welcome to E-commerce Project"

app.run(port="3000")