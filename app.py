from flask import Flask, render_template, redirect, url_for
import requests
import os
import pandas as pd
app = Flask(__name__)

app.config['SECRET_KEY'] = os.urandom(12)

@app.route("/")
@app.route("/home")
def home():
    return redirect(url_for('covid19'))

@app.route("/covid19")
def covid19():
    df=pd.read_csv(r"state_wise.csv")
    Confirmed=df.loc[[0],['Confirmed']]
    Confirmed=Confirmed.to_csv(header=None,index=False)
    Recovered=df.loc[[0],['Recovered']]
    Recovered = Recovered.to_csv(header=None, index=False)
    Deaths=df.loc[[0],['Deaths']]
    Deaths = Deaths.to_csv(header=None, index=False)

    return render_template("index.html", Confirmed=Confirmed, Recovered=Recovered, Deaths=Deaths)

if __name__=="__main__":
    app.run(debug=False)