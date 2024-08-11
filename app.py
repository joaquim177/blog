from flask import Flask, render_template, request, redirect, url_for,session
from database import db
import archives

app = Flask(__name__)
app.secret_key = archives.key


@app.route("/", methods=['GET', 'POST'])
def home():
    try:
        username = session.get('user')[1]
    except:
        return redirect('/login')
    
 
    
    if(request.method == 'GET'):
        posts = db.get_posts()
       
        return  render_template("home.html", posts=posts, user=username)
    elif(request.method == 'POST'):
        new_posts = []
        posts = db.get_posts()
        search = request.form.get('search')
        
        if(not search):
            return  render_template("home.html", posts=posts, user=username)

        for post in posts:
            if(search and search in post[2]):
                new_posts.append(post)
                
        return render_template("home.html", posts=new_posts, user=username)
        #terminar (fazer funcionar)

@app.route("/post/<int:id>")
def post(id):
    post_db = db.verify_id_post(id)
    username = session.get('user')[1]

    if(not post_db): return

    return render_template("post.html", post=post_db, user=username)



@app.route("/create_post", methods=['GET', 'POST'])
def create_post():
    username = session.get('user')[1]

    if request.method == 'GET':
        return render_template("criar_posts.html", user=username)
    elif request.method == 'POST':
        title = request.form.get("title")
        description = request.form.get("description")

        res = db.create_post((username, title, description))
        return redirect('/')

        #terminar

@app.route("/delete_post/<int:id>")

def delete_post(id):
    username = session.get('user')[1]

    res = db.delete_post(username, id)
    if res:
        return redirect(url_for('home'))
    else:
        return "Error deleting post", 500

#################################################
        # register and login (account)



@app.route("/login",methods=['GET','POST'])
def login():
    if request.method == 'GET':
        return render_template("login.html")
    elif request.method == 'POST':
        name = request.form.get('name')
        password = request.form.get('password')
        verify = db.login((name, password))

        if not verify[0]:
            return render_template("login.html",login_invalid=verify[1] )
        session['user'] = verify[1]
        return redirect("/")

        #terminar
@app.route("/quit")
def quit():
     session.clear()
     return redirect('/login')


@app.route("/register", methods=['GET', 'POST'])
def register():
    if request.method == 'GET':
        return render_template("cadastro.html")
    elif request.method == 'POST':
        name = request.form.get('name')
        password = request.form.get('password')
        email = request.form.get('email')
        verify = db.register_user((name,password, email))
        if(not verify[0]):
            return render_template("cadastro.html", register_invalid=verify[1])
        return redirect("/login")
        #terminara

if __name__ == '__main__':
    app.run(debug=True)


