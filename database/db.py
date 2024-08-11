import sqlite3
import archives
#USER
def consult_user_db(type, data):
    conn = sqlite3.connect(archives.database, check_same_thread=False)
    cursor = conn.cursor()

    if(type == 'name'):
        try:
            cursor.execute('SELECT * FROM users WHERE nome = ?', (data,))
            res = cursor.fetchone()

            if(not res):
                return print("usuario nao existe")
            
            return res
        except:
            print("erro")
        finally:
            conn.close()

    elif(type == 'id'):
        try:
            cursor.execute('SELECT * FROM users WHERE id = ?', (data,))
            res = cursor.fetchone()

            if(not res):
                return print("usuario nao existe")
            
            return res
        except:
            print("erro")
        finally:
            conn.close()

    elif(type == 'email'):
        try:
            cursor.execute('SELECT * FROM users WHERE email = ?', (data,))
            res = cursor.fetchone()

            if(not res):
                return print("usuario nao existe")
            
            return res
        except:
            print("erro")
        finally:
            conn.close()
    else:
        print("type invalid")


#register_user(('joaquim', '123', 'joaquim@gmail.com'))
def register_user(user):
    for u in user:
        if(len(u) <= 0):
            return [False, 'Preencha todos campos'] # campo vazio

    conn = sqlite3.connect(archives.database, check_same_thread=False)
    cursor = conn.cursor()

    verify_user_name = consult_user_db('name', user[0])
    verify_user_email = consult_user_db('email', user[2])

    if(verify_user_name or verify_user_email):
        return [False, 'Name ou Email ja utilizado']  # usuario ou email ja cadastrado

    try:
        cursor.execute("INSERT INTO users (nome, password, email) VALUES (?,?,?)", user)
        conn.commit()
        return [True]
    except:
        return [False, 'Erro ao tentar fazer login']
    finally:
        conn.close()

#login(('neymar', '123'))
def login(user):
    for u in user:
        if(len(u) <= 0):
            return [False, 'Preencha todos os campos'] #campo vazio
    conn = sqlite3.connect(archives.database, check_same_thread=False)
    cursor = conn.cursor()
    
    try:
        cursor.execute("SELECT * FROM users WHERE (nome, password) = (?,?)", user)
        res = cursor.fetchone()
        if(not res):
            return [False, 'Usuario nao existe']  # usuario nao existe
        print(res)
        return [True, res]
    except:
        return [False, 'Erro ao tentar fazer login']
    finally:
        conn.close()







#POSTS
def get_posts():
    conn = sqlite3.connect(archives.database,check_same_thread=False)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM posts")
    res = cursor.fetchall()
    conn.close()
    return res


def verify_id_post(id):
    conn = sqlite3.connect(archives.database,check_same_thread=False)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM posts WHERE id = ?", (id,))
    post = cursor.fetchone()
    conn.close()
    return post


def create_post(post):
    for u in post:
        if(len(u) <= 0):
            return [False, 'Preencha todos os campos']  # veio campo vazio
        
    verify_user_name = consult_user_db('name', post[0])  

    if not verify_user_name:
        return [False] #usuario nao existe

    conn = sqlite3.connect(archives.database)
    cursor = conn.cursor()
    try:
        cursor.execute("INSERT INTO posts (username, title, description) VALUES (?,?,?)", (post))    
        conn.commit()
    except:
        print("erro")    
    finally:
        conn.close()

def delete_post(username, postId):
    conn = sqlite3.connect(archives.database)
    cursor = conn.cursor()

    verify = cursor.execute('SELECT * FROM posts WHERE id = ?', (postId,))
    post = verify.fetchone()
    if(username != post[1]):
        return print("remoçao invalida")
    print(post)

    try:
        cursor.execute("DELETE FROM posts WHERE id = ?", (postId,))
        conn.commit()
        return True
    except:
        print("error")
    finally:
        conn.close()

