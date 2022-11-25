__autor__ = "Daniel Gomes e Silvana Siqueira"
__org__ = "milivro"

__chave_api__ = "AIzaSyCRaDBOAxPHRmqsegnSlm16wnq7hc0eg14"


import requests


'''
#CATEGORIAS

livro = input("Digite o nome do livro: ")
#categoria=input("Categoria:")
#+subject:{categoria}

link = f"https://www.googleapis.com/books/v1/volumes?q={livro}"

resposta = requests.get(link)
conteudo = resposta.json()

re = []
for itm in conteudo["items"]:
    re.append(itm["volumeInfo"]["title"])
    #re = itm["volumeInfo"]["title"]
    
    #l = [str(i) for i in re]
    #li = str("".join(l))
print(re[2])
    
#livros = conteudo["items"][0]

'''


#'''
from flask import Flask, redirect, render_template, url_for, session,request
import mysql.connector

connect = mysql.connector.connect(host="localhost",
                                  database="milivro", user="root",
                                  password="META100Kk#")

cursor = connect.cursor(buffered=True)


app = Flask(__name__)
app.secret_key="milivro-app-c78890"


@app.route("/")
def home():
    return render_template("index.html")

##################################################

@app.route("/inicio/ficcao")
def fic():

    link = "https://www.googleapis.com/books/v1/volumes?q=subject:fiction"

    resposta = requests.get(link)
    conteudo = resposta.json()

    
    re = []
    im =[]
    for itm in conteudo["items"]:
        re.append(itm["volumeInfo"]["title"])
        im.append(itm["volumeInfo"]["imageLinks"]["smallThumbnail"])

    l1 = re[0]
    im1 = im[0]
    l2=re[1]
    im2 = im[1]
    l3=re[2]
    im3 = im[2]
    l4=re[3]
    im4 = im[3]
    l5=re[4]
    im5 = im[4]
    l6=re[5]
    im6 = im[5]
    l7=re[6]
    im7 = im[6]
    l8=re[7]
    im8 = im[7]
    l9=re[8]
    im9 = im[8]
    l10=re[9]
    im10 = im[9]
            
            

    return render_template("fic.html", l1=l1, l2=l2,l3=l3,l4=l4,l5=l5,l6=l6,l7=l7,l8=l8,l9=l9,l10=l10
                            ,im1=im1,im2=im2,im3=im3,im4=im4,im5=im5,im6=im6,im7=im7,im8=im8,im9=im9,im10=im10)


@app.route("/inicio/acao")
def ac():
    link = "https://www.googleapis.com/books/v1/volumes?q=subject:action"

    resposta = requests.get(link)
    conteudo = resposta.json()

    
    re = []
    im =[]
    for itm in conteudo["items"]:
        re.append(itm["volumeInfo"]["title"])
        im.append(itm["volumeInfo"]["imageLinks"]["smallThumbnail"])

    l1 = re[0]
    im1 = im[0]
    l2=re[1]
    im2 = im[1]
    l3=re[2]
    im3 = im[2]
    l4=re[3]
    im4 = im[3]
    l5=re[4]
    im5 = im[4]
    l6=re[5]
    im6 = im[5]
    l7=re[6]
    im7 = im[6]
    l8=re[7]
    im8 = im[7]
    l9=re[8]
    im9 = im[8]
    l10=re[9]
    im10 = im[9]
            
            

    return render_template("ac.html", l1=l1, l2=l2,l3=l3,l4=l4,l5=l5,l6=l6,l7=l7,l8=l8,l9=l9,l10=l10
                            ,im1=im1,im2=im2,im3=im3,im4=im4,im5=im5,im6=im6,im7=im7,im8=im8,im9=im9,im10=im10)

@app.route("/inicio/comedia")
def com():
    link = "https://www.googleapis.com/books/v1/volumes?q=subject:comedy"

    resposta = requests.get(link)
    conteudo = resposta.json()

    
    re = []
    im =[]
    for itm in conteudo["items"]:
        re.append(itm["volumeInfo"]["title"])
        im.append(itm["volumeInfo"]["imageLinks"]["smallThumbnail"])

    l1 = re[0]
    im1 = im[0]
    l2=re[1]
    im2 = im[1]
    l3=re[2]
    im3 = im[2]
    l4=re[3]
    im4 = im[3]
    l5=re[4]
    im5 = im[4]
    l6=re[5]
    im6 = im[5]
    l7=re[6]
    im7 = im[6]
    l8=re[7]
    im8 = im[7]
    l9=re[8]
    im9 = im[8]
    l10=re[9]
    im10 = im[9]
            
            

    return render_template("com.html", l1=l1, l2=l2,l3=l3,l4=l4,l5=l5,l6=l6,l7=l7,l8=l8,l9=l9,l10=l10
                            ,im1=im1,im2=im2,im3=im3,im4=im4,im5=im5,im6=im6,im7=im7,im8=im8,im9=im9,im10=im10)

@app.route("/inicio/aventura")
def adv():
    link = "https://www.googleapis.com/books/v1/volumes?q=subject:adventure"

    resposta = requests.get(link)
    conteudo = resposta.json()

    
    re = []
    im =[]
    for itm in conteudo["items"]:
        re.append(itm["volumeInfo"]["title"])
        im.append(itm["volumeInfo"]["imageLinks"]["smallThumbnail"])

    l1 = re[0]
    im1 = im[0]
    l2=re[1]
    im2 = im[1]
    l3=re[2]
    im3 = im[2]
    l4=re[3]
    im4 = im[3]
    l5=re[4]
    im5 = im[4]
    l6=re[5]
    im6 = im[5]
    l7=re[6]
    im7 = im[6]
    l8=re[7]
    im8 = im[7]
    l9=re[8]
    im9 = im[8]
    l10=re[9]
    im10 = im[9]
            
            

    return render_template("av.html", l1=l1, l2=l2,l3=l3,l4=l4,l5=l5,l6=l6,l7=l7,l8=l8,l9=l9,l10=l10
                            ,im1=im1,im2=im2,im3=im3,im4=im4,im5=im5,im6=im6,im7=im7,im8=im8,im9=im9,im10=im10)

@app.route("/inicio/juvenil")
def juv():
    link = "https://www.googleapis.com/books/v1/volumes?q=subject:juvenil"

    resposta = requests.get(link)
    conteudo = resposta.json()

    
    re = []
    im =[]
    for itm in conteudo["items"]:
        re.append(itm["volumeInfo"]["title"])
        im.append(itm["volumeInfo"]["imageLinks"]["smallThumbnail"])

    l1 = re[0]
    im1 = im[0]
    l2=re[1]
    im2 = im[1]
    l3=re[2]
    im3 = im[2]
    l4=re[3]
    im4 = im[3]
    l5=re[4]
    im5 = im[4]
    l6=re[5]
    im6 = im[5]
    l7=re[6]
    im7 = im[6]
    l8=re[7]
    im8 = im[7]
    l9=re[8]
    im9 = im[8]
    l10=re[9]
    im10 = im[9]
            
            

    return render_template("juv.html", l1=l1, l2=l2,l3=l3,l4=l4,l5=l5,l6=l6,l7=l7,l8=l8,l9=l9,l10=l10
                            ,im1=im1,im2=im2,im3=im3,im4=im4,im5=im5,im6=im6,im7=im7,im8=im8,im9=im9,im10=im10)

####################################################

@app.route("/preview", methods=["GET", "POST"])
def previa():
    if request.method=="POST":
        li = request.form["livr"]
        link = f"https://www.googleapis.com/books/v1/volumes?q={li}"

        resposta = requests.get(link)
        conteudo = resposta.json()

    
        re = []
        im =[]
        for itm in conteudo["items"]:
            re.append(itm["volumeInfo"]["title"])
            im.append(itm["volumeInfo"]["imageLinks"]["smallThumbnail"])

        l1 = re[0]
        im1 = im[0]
        l2=re[1]
        im2 = im[1]
        l3=re[2]
        im3 = im[2]
        l4=re[3]
        im4 = im[3]
        l5=re[4]
        im5 = im[4]
        l6=re[5]
        im6 = im[5]
        l7=re[6]
        im7 = im[6]
        l8=re[7]
        im8 = im[7]
        l9=re[8]
        im9 = im[8]
        l10=re[9]
        im10 = im[9]
            
            

        return render_template("preview.html", l1=l1, l2=l2,l3=l3,l4=l4,l5=l5,l6=l6,l7=l7,l8=l8,l9=l9,l10=l10
                               ,im1=im1,im2=im2,im3=im3,im4=im4,im5=im5,im6=im6,im7=im7,im8=im8,im9=im9,im10=im10)
        

        
    return render_template("preview.html")


@app.route("/inicio", methods=["GET", "POST"])
def inicio():
    if request.method=="POST":
        li = request.form["livr"]
        link = f"https://www.googleapis.com/books/v1/volumes?q={li}"

        resposta = requests.get(link)
        conteudo = resposta.json()

    
        re = []
        im =[]
        for itm in conteudo["items"]:
            re.append(itm["volumeInfo"]["title"])
            im.append(itm["volumeInfo"]["imageLinks"]["smallThumbnail"])

        l1 = re[0]
        im1 = im[0]
        l2=re[1]
        im2 = im[1]
        l3=re[2]
        im3 = im[2]
        l4=re[3]
        im4 = im[3]
        l5=re[4]
        im5 = im[4]
        l6=re[5]
        im6 = im[5]
        l7=re[6]
        im7 = im[6]
        l8=re[7]
        im8 = im[7]
        l9=re[8]
        im9 = im[8]
        l10=re[9]
        im10 = im[9]
            
            

        return render_template("inicio.html", l1=l1, l2=l2,l3=l3,l4=l4,l5=l5,l6=l6,l7=l7,l8=l8,l9=l9,l10=l10
                               ,im1=im1,im2=im2,im3=im3,im4=im4,im5=im5,im6=im6,im7=im7,im8=im8,im9=im9,im10=im10)

        
    return render_template("inicio.html")

@app.route("/login", methods=["GET", "POST"])
def login():
    msg = ""
    if request.method=="POST":
        emails = request.form["email"]
        senhas = request.form["senha"]
        cursor.execute("SELECT * FROM usuario WHERE email=%s AND senha=%s",(emails, senhas))
        resposta = cursor.fetchone()

        ###########################
        
        if resposta:
            session["loggedin"] = True
            session["email"] = resposta[1]
            return redirect(url_for("inicio", email=emails))
        else:
            msg="Email/Senha incorretos"

        ###########################
    return render_template("conta.html",msg=msg)


@app.route("/sign", methods=["GET", "POST"])
def sign():
    if request.method=="POST":
        name = request.form["nome"]
        email = request.form["email_sign"]
        senha = request.form["senha_sign"]
        respostas = cursor.execute("INSERT INTO usuario(id, Nome, Email, Senha) VALUES(null, %s, %s, %s)", (name, email, senha))
        connect.commit()
        connect.close()
        return redirect(url_for("inicio", email=email))
    return render_template("sign.html")



if __name__ == "__main__":
    app.run(debug=True, port="9701")

#'''
