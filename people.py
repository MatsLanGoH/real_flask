from datetime import datetime

from flask import (
    abort,
    make_response,
)


def get_timestamp():
    return datetime.now().strftime(("%Y-%m-%d %H:%M:%S"))


# Data to serve with our API
PEOPLE = {
    "Farrell": {
        "firstname": "Doug",
        "lastname": "Farrell",
        "timestamp": get_timestamp(),
    },
    "Brockman": {
        "firstname": "Kent",
        "lastname": "Brockman",
        "timestamp": get_timestamp(),
    },
    "Easter": {
        "firstname": "Bunny",
        "lastname": "Easter",
        "timestamp": get_timestamp(),
    },
}


# Create a handler for our read (GET) people
def read_all():
    """This function responds to a request for /api/people
    with the complete lists of people

    :return:
        sorted list of people
    """
    # Create the list of people from our data
    return [PEOPLE[key] for key in sorted(PEOPLE.keys())]


def read_one(last_name):
    """This function responds to a request for /api/people/{lastName}
    with one matching person from people
    
    :param last_name:
        last name of person to find
    
    :return:
        person matching last name
    """
    if last_name in PEOPLE:
        person = PEOPLE.get(last_name)
    else:
        abort(404, f"Person with last name {last_name} not found.")

    return person


def create():
    return


def update():
    return


def delete():
    return
