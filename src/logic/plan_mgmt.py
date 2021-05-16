from data_service.plan_service import create_plan, get_plans_by_user

def new_plan(session, name, description):
    """Creates a new plan to the system using plan_service

    Args:
        session (SessionInfo): current session
        name (string): plan name
        description (string): plan description
    """
    create_plan(session.get_username(),session.get_db_connection(), name, description)

def load_plans(session):
    """Uses plan_service to get a list of plans.

    Args:
        session (SessionInfo): current session

    Returns:
        (list): list of plans
    """
    return get_plans_by_user(session.get_username(), session.get_db_connection())
