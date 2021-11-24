import os

ENVIRONMENT = os.environ.get('ENVIRONMENT', False)

if ENVIRONMENT:
    try:
        API_ID = int(os.environ.get('316144', 0))
    except ValueError:
        raise Exception("Your API_ID is not a valid integer.")
    API_HASH = os.environ.get('61b01fe1d7686f2c6f64ce61aeefea9f', None)
    BOT_TOKEN = os.environ.get('2108186289:AAFKlF0JJXB1LjEeEZziVqs4IMu89X1rAXo', None)
    DATABASE_URL = os.environ.get('postgres://atohjwyznaizqb:c47beb9e949e5c1cb2aa2521769862d2a877acfa67b76a929ca1599dfcacb7e9@ec2-3-230-82-215.compute-1.amazonaws.com:5432/d9loi55upq8gss', None)
    DATABASE_URL = DATABASE_URL.replace("postgres", "postgresql")  # Sqlalchemy dropped support for "postgres" name.
    # https://stackoverflow.com/questions/62688256/sqlalchemy-exc-nosuchmoduleerror-cant-load-plugin-sqlalchemy-dialectspostgre
    MUST_JOIN = os.environ.get('MUST_JOIN', None)
    if MUST_JOIN.startswith("@"):
        MUST_JOIN = MUST_JOIN.replace("@", "")
else:
    # Fill the Values
    API_ID = 316144
    API_HASH = "61b01fe1d7686f2c6f64ce61aeefea9f"
    BOT_TOKEN = "2108186289:AAFKlF0JJXB1LjEeEZziVqs4IMu89X1rAXo"
    DATABASE_URL = "postgres://atohjwyznaizqb:c47beb9e949e5c1cb2aa2521769862d2a877acfa67b76a929ca1599dfcacb7e9@ec2-3-230-82-215.compute-1.amazonaws.com:5432/d9loi55upq8gss"
    DATABASE_URL = DATABASE_URL.replace("postgres", "postgresql")
    MUST_JOIN = ""
    if MUST_JOIN.startswith("@"):
        MUST_JOIN = MUST_JOIN[1:]
