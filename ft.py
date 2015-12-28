# -*- coding: utf-8 -*-
import os 
from flask import Flask
from flask import request
from flask import render_template
from flask import request, redirect, url_for
from Util import poster,numb,name
from flask import send_from_directory
import re
from Sim import getsimilaritems

app = Flask(__name__)
def dalv(movie):
    prearr = []
    posterurl = str(poster(movie)[0])
    movtitle = str(name(movie)[0])
    if len(movtitle)>34:
        movtitle = str(movtitle[0:35] + " . . . ")
    movyear = str(re.findall("(.+)(\([0-9]*?\))",str(name(movie)))[0][1])
    href = str("/" + str(name(movie)[0]).replace(" ","+"))
    prearr = [posterurl,movtitle,movyear,href]
    return prearr

@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'),
                               'favicon.ico', mimetype='image/vnd.microsoft.icon')

@app.route('/')
def home():
    return render_template('palatelanding.html')

@app.template_filter('smooth')
def smooth(s):
    return str(s)[2:-2]

@app.route('/<title>')
def title(title):
    err = ''
    
    text1 = title.replace("+"," ")
    import re
    arr = []
    datak = int(numb(text1)[0])
    thefocus = dalv(datak)
    try:
        v = getsimilaritems(datak,8)
        
        
        for movie in v:
            if v != [99957, 99917, 99912, 999, 99813, 998] and v != [99957, 99917, 99912, 999, 99813, 998, 99741, 99728]:
                print v
                arr.append(dalv(movie))
    
    except:
        err = "Oops! not enough data"    
    
    
    
    
    return render_template(
        'nav.html',
        focus = thefocus, # the focus is the entered url title
        recs = arr[1:], # all but focus
        oops = err
        )
        



@app.route('/mypalate')
def my_form():
    return render_template("my-form.html")


@app.route('/mypalate', methods=['POST'])
def recommendgo():
    import re
    humanity = request.form['five']
    sensitivity = request.form['sensitivity']
    text1 = request.form['text1']
    text2 = request.form['text2']
    text3 = request.form['text3']
    text4 = request.form['text4']
    text5 = request.form['text5']
    text6 = request.form['text6']
    text7 = request.form['text7']
    text8 = request.form['text8']
    text9 = request.form['text9']
    text10 = request.form['text10']
    text11 = request.form['text11']
    text12 = request.form['text12']
    text13 = request.form['text13']
    text14 = request.form['text14']
    text15 = request.form['text15']
    text16 = request.form['text16']
    text17 = request.form['text17']
    text18 = request.form['text18']
    text19 = request.form['text19']
    text20 = request.form['text20']
    text21 = request.form['text21']
    text22 = request.form['text22']
    text23 = request.form['text23']
    text24 = request.form['text24']
    text25 = request.form['text25']
    text26 = request.form['text26']
    text27 = request.form['text27']
    text28 = request.form['text28']
    text29 = request.form['text29']
    text30 = request.form['text30']
    
    arrkl = (int(humanity))
    
    a1='-empty-'
    a2='-empty-'
    a3='-empty-'
    a4='-empty-'
    a5='-empty-'
    a6='-empty-'
    a7='-empty-'
    a8='-empty-'
    a9='-empty-'
    a10='-empty-'
    a11='-empty-'
    a12='-empty-'
    a13='-empty-'
    a14='-empty-'
    a15='-empty-'
    
    
    if (arrkl>=2):
        a1 = str(str(numb(str(text1))[0])+":"+str(text16)+", ")
        
    if (arrkl>=2):
        a2 = str(str(numb(str(text2))[0])+":"+str(text17)+", ")

    if (arrkl>=2):
        a3 = str(str(numb(str(text3))[0])+":"+str(text18)+", ")

    if (arrkl>=2):
        a4 = str(str(numb(str(text4))[0])+":"+str(text19)+", ")

    if (arrkl>=2):
        a5 = str(str(numb(str(text5))[0])+":"+str(text20)+", ")

    if (arrkl>=2):
        a6 = str(str(numb(str(text6))[0])+":"+str(text21)+", ")

    if (arrkl>=2):
        a7 = str(str(numb(str(text7))[0])+":"+str(text22)+", ")

    if (arrkl>=2):
        a8 = str(str(numb(str(text8))[0])+":"+str(text23)+", ")

    if (arrkl>=2):
        a9 = str(str(numb(str(text9))[0])+":"+str(text24)+", ")

    if (arrkl>=2):
        a10 = str(str(numb(str(text10))[0])+":"+str(text25)+", ")

    if (arrkl>=2):
        a11 = str(str(numb(str(text11))[0])+":"+str(text26)+", ")

    if (arrkl>=2):
        a12 = str(str(numb(str(text12))[0])+":"+str(text27)+", ")

    if (arrkl>=2):
        a13 = str(str(numb(str(text13))[0])+":"+str(text28)+", ")

    if (arrkl>=2):
        a14 = str(str(numb(str(text14))[0])+":"+str(text29)+", ")

    if (arrkl>=2):
        a15 = str(str(numb(str(text15))[0])+":"+str(text30)+", ")
        
    rawent = re.sub(", +}","}",str("{"+a1+a2+a3+a4+a5+a6+a7+a8+a9+a10+a11+a12+a13+a14+a15+"}").replace("~~~:,",""))
    if rawent == "{-empty--empty--empty--empty--empty--empty--empty--empty--empty--empty--empty--empty--empty--empty--empty-}":
        return render_template("my-form.html")
    rawgood = dict((k, v) for k, v in eval(rawent).items() if v >= 3)
    good = list(rawgood.keys())
    
    
    
    
    
    
    import re
    
    try:
        arr = []
        posterarr = []
        ko = good
        focusl = []
        for each in ko:
            v = getsimilaritems(each, 6)
            for movie in v:
                dm = dalv(movie)
                if v != [99957, 99917, 99912, 999, 99813, 998]:
                    if movie not in ko:
                        if dm not in arr:
                            arr.append(dm)
            focusind = dalv(each)                
            if focusind not in focusl:
                focusl.append(focusind)   # This would display overlaping recs
    except:
        arr = ['---Oops! Insufficient Data---']



    return render_template(
        'mypalatenav.html',
        focused = focusl, # the focus is the entered url title
        recs = arr, # all but focus
        )








#app.run(host=os.getenv('IP', '0.0.0.0'),port=int(os.getenv('PORT', 8080)))

if __name__ == '__main__':
    app.debug = True
    app.run()