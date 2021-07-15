from flask import Flask , render_template, request , redirect , url_for

app = Flask(__name__)

@app.route("/",methods=['GET','POST'])
def calculategpa():
    if request.method=='POST':
        rd={
            "eng":[request.form['eng'],3],
            "ac":[request.form['ac'],4],
            "uph":[request.form['uph'],3],
            "ucy":[request.form['ucy'],3],
            "pyt":[request.form['pyt'],3],
            "eg":[request.form['eg'],3],
            "ppl":[request.form['ppl'],1.5],
            "pcl":[request.form['pcl'],1.5]
        }
        # rf={"o":10,"a+":9,"a":8,"b+":7,"b":6}
        for i in rd:
            if rd[i][0] == "0":
                return render_template("index.html",alertext="Select the Options correctly!")
            if rd[i][0] in ["ra","sa","w","ab","au"]:
                return render_template('results.html',grade="Sorry bro you have failed! Dont worry do well next time!")
        
        grade=0
        for i in rd:
            grade+=(int(rd[i][0])*rd[i][1])
            print(grade)

        grade=round(float(grade/22),1)
        return render_template('results.html',grade=grade)
    else:
        return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=False)
