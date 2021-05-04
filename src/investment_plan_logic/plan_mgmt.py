def get_plans_by_user(username,db_connection):
    """Returns a list of plans for a username

    Args:
        username (string): logged in username
        db_connection (string): sqlite 3 connection

    Returns:
        list of plan names (strings)
    """
    query = "SELECT name FROM Plan WHERE username = :username"
    return db_connection.execute(query,{"username":username}).fetchall()

def create_plan(username,db_connection,name,description):
    """Creates a new plan to DB with given name & description

    Args:
        username (string): logged in username
        db_connection (string): sqlite 3 connection
        name (string): name of plan
        description (string): description of the plan

    Raises:
        InputError: if name is missing
    """
    if len(name) == 0:
        raise InputError("Name missing")
    query = "INSERT INTO Plan (username,name,description) VALUES (:username,:name,:description)"
    db_connection.execute(query,{"username":username,"name":name,"description":description})
    db_connection.commit()

def get_costs(username,db_connection,name):
    """used to get all cost items for a plan

    Args:
        username (string): logged in username
        db_connection (string): sqlite 3 connection
        name (string): name of plan

    Raises:
        InputError: raises error if input parameter is empty

    Returns:
        list of cost items for the plan, including description, amount & year
    """
    if len(name) == 0:
        raise InputError("Name missing")
    query = "SELECT description, amount, year FROM Cost WHERE "+\
        "plan_id=(SELECT Plan.plan_id FROM Plan WHERE name=:name AND username=:username)"+\
        "ORDER BY year ASC, description DESC"
    return db_connection.execute(query,{"name":name,"username":username}).fetchall()

def get_cost_types(username,db_connection,name):
    """used to get all cost types for a plan

    Args:
        username (string): logged in username
        db_connection (string): sqlite 3 connection
        name (string): name of plan

    Returns:
        list of cost names for a plan
    """
    query = "SELECT description FROM Cost WHERE "+\
        "plan_id=(SELECT Plan.plan_id FROM Plan WHERE name=:name AND username=:username)"
    return db_connection.execute(query,{"name":name,"username":username}).fetchall()

def get_revenue(username,db_connection,name):
    """used to get all revenue items for a certain plan

    Args:
        username (string): logged in username
        db_connection (string): sqlite 3 connection
        name (string): name of plan

    Raises:
        InputError: if parameter is empty

    Returns:
        list of revenue items for the plan, including description, amount & year
    """
    if len(name) == 0:
        raise InputError("Name missing")
    query = "SELECT description, amount, year FROM Revenue WHERE "+\
        "plan_id=(SELECT Plan.plan_id FROM Plan WHERE name=:name AND username=:username) "+\
        "ORDER BY year ASC, description DESC"
    return db_connection.execute(query,{"name":name,"username":username}).fetchall()

def get_revenue_types(username,db_connection,name):
    """returns revenue types found for a plan

    Args:
        username (string): logged in username
        db_connection (string): sqlite 3 connection
        name (string): name of plan

    Returns:
        list of cost names
    """
    query = "SELECT description FROM Revenue WHERE "+\
        "plan_id=(SELECT Plan.plan_id FROM Plan WHERE name=:name AND username=:username)"
    return db_connection.execute(query,{"name":name,"username":username}).fetchall()

def add_cost(username,db_connection,name,description,amount,year):
    """Adds a single cost item to the db.

    Args:
        username (string): logged in username
        db_connection (string): sqlite 3 connection
        name (string): name of plan
        description (string): description of cost item
        amount (can be string or integer): amount of cost
        year (can be string or integer): year for cost

    Raises:
        InputError: if input is missing
    """
    if len(name) == 0 or len(description) == 0 or len(amount) == 0 or len(year) == 0:
        raise InputError("missing parameter")
    query = "INSERT INTO Cost (plan_id,description,amount,year) VALUES ((SELECT plan_id "+\
        "FROM Plan WHERE name=:name AND username=:username),:description,:amount,:year)"
    db_connection.execute(query,{"name":name,"username":username,\
        "description":description,"amount":amount,"year":year})
    db_connection.commit()

def add_revenue(username,db_connection,name,description,amount,year):
    """Adds a single revenue item to the db.

    Args:
        username (string): logged in username
        db_connection (string): sqlite 3 connection
        name (string): name of plan
        description (string): description of revenue item
        amount (can be string or integer): amount of revenue
        year (can be string or integer): year for revenue

    Raises:
        InputError: if input is missing
    """
    if len(name) == 0 or len(description) == 0 or len(amount) == 0 or len(year) == 0:
        raise InputError("missing parameter")
    query = "INSERT INTO Revenue (plan_id,description,amount,year) VALUES ((SELECT plan_id "+\
        "FROM Plan WHERE name=:name AND username=:username),:description,:amount,:year)"
    db_connection.execute(query,{"name":name,"username":username,\
        "description":description,"amount":amount,"year":year})
    db_connection.commit()

class InputError(Exception):
    pass
