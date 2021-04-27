def get_plans_by_user(username,db_connection):
    query = "SELECT name FROM Plan WHERE username = :username"
    return db_connection.execute(query,{"username":username}).fetchall()

def create_plan(username,db_connection,name,description):
    query = "INSERT INTO Plan (username,name,description) VALUES (:username,:name,:description)"
    db_connection.execute(query,{"username":username,"name":name,"description":description})
    db_connection.commit()
