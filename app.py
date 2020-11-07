import dbcreds
import mariadb 

def MakePost(username):
    
    blog_post =("Make a blog post: ")
    conn = mariadb.connect(user=dbcreds.user, password=dbcreds.password, host=dbcreds.host, port=dbcreds.port, database=dbcreds.database)
    cursor = conn.cursor()
    cursor.execute("INSERT INTO blog_post (username, content, id) VALUES(?, ?, NULL)", [username, blog_post])
    conn.commit()
    cursor.close()
    conn.close()
    
def ViewPosts():

    conn = mariadb.connect(user=dbcreds.user, password=dbcreds.password, host=dbcreds.host, port=dbcreds.port, database=dbcreds.database)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM blog_post")
    rows = cursor.fetchall()
    print(rows)
    cursor.close()
    conn.close()
    
username = input("Enter username: ")
print("pick an option: ")
print("1. make a blog post")
print("2. view posts")


user_option = input("select an option: ")
 
while 1:
    if user_option == "1":
       MakePost(username)
    
    elif user_option == "2":
       ViewPosts()
    else:
        break
    user_option = input("select an option: ")
    
       
        



    





