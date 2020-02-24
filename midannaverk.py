from flask import Flask, render_template
import urllib.request, json
app = Flask(__name__)

with urllib.request.urlopen("http://apis.is/petrol") as url:
    data = json.loads(url.read().decode())

minnstiBens = 3000
minnstiBensCo = ""
minnstiBensLo = ""
minnstiDis = 3000
minnstiDisCo = ""
minnstiDisLo = ""

for i in data["results"]:
    if i["bensin95"] < minnstiBens:
        minnstiBens = i["bensin95"]
        minnstiBensCo = i["company"]
        minnstiBensLo = i["name"]

for i in data["results"]:
    if i["diesel"] < minnstiDis:
        minnstiDis = i["diesel"]
        minnstiDisCo = i["company"]
        minnstiDisLo = i["name"]

timestampPriceChanges = data["timestampPriceChanges"].split('T')
a,b = timestampPriceChanges

@app.route('/')
def index():
    companyOnce = []
    
    for i in data["results"]:
        if i["company"] not in companyOnce:
            companyOnce.append(i["company"])
    
    return render_template("index.html", co = companyOnce,minnstiBens=minnstiBens,minnstiDis=minnstiDis,minnstiBensCo=minnstiBensCo,minnstiDisCo=minnstiDisCo,minnstiBensLo=minnstiBensLo,minnstiDisLo=minnstiDisLo,date=a,timm=b)

@app.route('/company/<company>')
def company(company):
    return render_template("company.html" ,co=company, data=data)

@app.route('/moreInfo/<key>')
def moreInfo(key):
    print(key)
    return render_template("moreInfo.html" ,co=company, data=data,key=key)


if __name__ == "__main__":
	app.run(debug=True)