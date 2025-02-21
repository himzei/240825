from scrapper import job_berlin, job_web3
from flask import Flask, render_template, request, redirect, send_file
from file import save_to_file

app = Flask(__name__)

db = {}

@app.route('/')
def home():
    return render_template("home.html")

@app.route('/search')
def search():
    keyword = request.args.get("keyword")
    if keyword == "": 
        return redirect("/")
    if keyword in db: 
        jobs = db[keyword]
    else: 
        data_berlin = job_berlin(keyword)
        data_web3 = job_web3(keyword)
        jobs = data_berlin + data_web3
        db[keyword] = jobs
        
    return render_template("search.html", keyword=keyword, jobs=jobs)


@app.route("/export") 
def export(): 
    keyword = request.args.get("keyword")
    if keyword == "": 
        return redirect("/")
    if keyword not in db: 
        return redirect(f"/search?keyword={keyword}")
    save_to_file(keyword, db[keyword])
    return send_file(f"{keyword}.csv", as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)