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
        "first_name": "Doug",
        "last_name": "Farrell",
        "timestamp": get_timestamp(),
    },
    "Brockman": {
        "first_name": "Kent",
        "last_name": "Brockman",
        "timestamp": get_timestamp(),
    },
    "Easter": {
        "first_name": "Bunny",
        "last_name": "Easter",
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


def create(person):
    """This function creates a new person in the people structure
    based on the passed in person data.

    :param person:
        Person to create in people structure
    :return:
        201 on success, 406 on person exists
    """
    last_name = person.get("last_name", None)
    first_name = person.get("first_name", None)

    if last_name not in PEOPLE and last_name is not None:
        PEOPLE[last_name] = {
            "last_name": last_name,
            "first_name": first_name,
            "timestamp": get_timestamp(),
        }
        return make_response(f"{last_name} successfully created")
    else:
        abort(406, f"Person with last name {last_name} already exists.")


def update(last_name, person):
    """
    This function updates an existing person in the people structure.

    :param last_name:
        Last name of person to update in the people structure
    :param body:
        Request body with person data.
    :return:
        Updated person structure
    """
    if last_name in PEOPLE:
        PEOPLE[last_name]["first_name"] = person.get("first_name")
        PEOPLE[last_name]["timestamp"] = get_timestamp()
        return PEOPLE[last_name]
    else:
        abort(404, f"Person with last name {last_name} not found")


def delete(last_name):
    """
    This function deletes a person from the people structure

    :param last_name:
        Last name of person to delete
    
    :return:
        200 on successful delete,
        404 if not found
    """
    if last_name in PEOPLE:
        del PEOPLE[last_name]
        return make_response(f"{last_name} successfully deleted")
    else:
        abort(404, f"Person with last name {last_name} not found")
