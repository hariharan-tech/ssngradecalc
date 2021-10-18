from flask import Flask , render_template, request , redirect , url_for

app = Flask(__name__)

@app.route("/",methods=['GET','POST'])
def calculategpa():
    if request.method=='POST':
        rd={
            "te":[request.form['te'],3],
            "cflt":[request.form['cflt'],4],
            "pee":[request.form['pee'],3],
            "eie":[request.form['eie'],3],
            "ed":[request.form['ed'],3],
            "ca":[request.form['ca'],4],
            "dp":[request.form['dp'],1.5],
            "cdl":[request.form['cdl'],1.5]
        }
        # rf={"o":10,"a+":9,"a":8,"b+":7,"b":6}
        for i in rd:
            if rd[i][0] == "0":
                return render_template("index.html",alertext="Select the Options correctly!")
            if rd[i][0] in ["ra","sa","w","ab","au"]:
                return render_template('results.html',grade="Dont worry, do well next time!")
        
        grade=0
        for i in rd:
            grade+=(int(rd[i][0])*rd[i][1])
#             print(grade)

        grade=round(float(grade/23),1)
        return render_template('results.html',grade=grade)
    else:
        return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=False)
