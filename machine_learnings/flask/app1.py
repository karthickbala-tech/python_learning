from flask import Flask,request,render_template

app= Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html",number=15000,language="python",List=["data science","mechine learning","data analyties","artificial intelligence"])

@app.route("/about")
def about():
    print(request.args)
    print(request.args['name'])
    print(request.args['age'])
    return render_template("about.html")

@app.template_filter("double")
def double(n):
    return n*2

@app.route("/contect/<name>")
def user(name):
    return render_template("contect.html")

if __name__== "__main__":
    app.run(debug=True,port= 5010)






 


    
