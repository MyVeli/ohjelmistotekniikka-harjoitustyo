def get_plans_by_user(username,db_connection):
    query = "SELECT name FROM Plan WHERE username = :username"
    return db_connection.execute(query,{"username":username}).fetchall()

def create_plan(username,db_connection,name,description):
    query = "INSERT INTO Plan (username,name,description) VALUES (:username,:name,:description)"
    db_connection.execute(query,{"username":username,"name":name,"description":description})
    db_connection.commit()

def get_costs(username,db_connection,name):
    query = "SELECT description, amount, year FROM Cost WHERE "+\
        "plan_id=(SELECT Plan.plan_id FROM Plan WHERE name=:name AND username=:username)"+\
        "ORDER BY year ASC, description DESC"
    return db_connection.execute(query,{"name":name,"username":username}).fetchall()

def get_cost_types(username,db_connection,name):
    query = "SELECT description FROM Cost WHERE "+\
        "plan_id=(SELECT Plan.plan_id FROM Plan WHERE name=:name AND username=:username)"
    return db_connection.execute(query,{"name":name,"username":username}).fetchall()

def get_revenue(username,db_connection,name):
    query = "SELECT description, amount, year FROM Revenue WHERE "+\
        "plan_id=(SELECT Plan.plan_id FROM Plan WHERE name=:name AND username=:username) "+\
        "ORDER BY year ASC, description DESC"
    return db_connection.execute(query,{"name":name,"username":username}).fetchall()

def get_revenue_types(username,db_connection,name):
    query = "SELECT description FROM Revenue WHERE "+\
        "plan_id=(SELECT Plan.plan_id FROM Plan WHERE name=:name AND username=:username)"
    return db_connection.execute(query,{"name":name,"username":username}).fetchall()

def add_cost(username,db_connection,name,description,amount,year):
    query = "INSERT INTO Cost (plan_id,description,amount,year) VALUES ((SELECT plan_id "+\
        "FROM Plan WHERE name=:name AND username=:username),:description,:amount,:year)"
    db_connection.execute(query,{"name":name,"username":username,\
        "description":description,"amount":amount,"year":year})
    db_connection.commit()

def add_revenue(username,db_connection,name,description,amount,year):
    query = "INSERT INTO Revenue (plan_id,description,amount,year) VALUES ((SELECT plan_id "+\
        "FROM Plan WHERE name=:name AND username=:username),:description,:amount,:year)"
    db_connection.execute(query,{"name":name,"username":username,\
        "description":description,"amount":amount,"year":year})
    db_connection.commit()
