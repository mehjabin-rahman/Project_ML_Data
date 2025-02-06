from flask import Flask,render_template,request
import os
import numpy as np
import pandas as pd
from mlProject.pipeline.prediction import PredictionPopeline

app=Flask(__name__)#initialize the flask app

@app.route('/',methods=['GET'])#route to display the home page
def homePage():
    return render_template("index.html")

if __name__=="__main__":
    app.run(host="0.0.0.0",port=8080.debug)