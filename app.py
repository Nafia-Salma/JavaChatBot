from flask import Flask, render_template, request, jsonify
import tensorflow as tf


from chatbot import chat

app=Flask(__name__)


@app.get("/")
def idex_get():
    return render_template("index.html")

@app.post("/predict")
def predict():
    text=request.get_json().get("message")
    #TODO:check if text is valid
    response=chat(text)
    message={"answer":response}
    return jsonify(message)


if __name__==  "__main__":
        app.run(debug=True)
