from flask import Flask, redirect, url_for, render_template

app = Flask(__name__)

isAdmin = True

@app.route("/")
def home():
	return render_template("index.html")

@app.route("/admin")
def admin():
	if isAdmin:
		return "admin page"

	else:
		return redirect(url_for("home"))

if __name__ == "__main__":
	app.run(debug = True)