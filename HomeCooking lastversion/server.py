from flask import Flask,render_template, request

app=Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/about")
def about():
    return  render_template("about.html")
@app.route("/LSH")
def LSH():
    return  render_template("LSH.html")
 
@app.route("/contact")
def contact():
    return render_template("contact.html")
@app.route("/order")
def order():
    return render_template("order.html")
@app.route("/admin")
def admin():
    return render_template("admin.html")
@app.route("/login_admin")
def login_admin():
    return render_template("login_admin.html")
if __name__=="__main__":
    app.run(debug=True)