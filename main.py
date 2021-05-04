from flask import Flask, render_template
import pandas as pd


app = Flask("flaskdemo")


@app.route("/")
def homepage():
    return "Hello, world"


@app.route("/greet/<name>")
def sayhello(name):
    return f"Hello, {name}"


@app.route("/people")
def people():
    df = pd.read_csv("database.csv")
    print(df)
    # return df.to_html(index=False)
    return render_template("people.html", people_df=df)


if __name__ == "__main__":
    # app.run(host="0.0.0.0", port="5001", debug=True)
    app.run(host="0.0.0.0", port="5001")
