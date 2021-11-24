import os

ENVIRONMENT = os.environ.get('ENVIRONMENT', False)

if ENVIRONMENT:
    try:
        API_ID = int(os.environ.get('316144', 0))
    except ValueError:
        raise Exception("Your API_ID is not a valid integer.")
    API_HASH = os.environ.get('61b01fe1d7686f2c6f64ce61aeefea9f', None)
    BOT_TOKEN = os.environ.get('2108186289:AAFKlF0JJXB1LjEeEZziVqs4IMu89X1rAXo', None)
    DATABASE_URL = os.environ.get('postgres://arvkivrjdndtyi:5a66f7f6188fedb72833f90a3777bdea5b29fdb0be70c015ffca9f7bfe377eb2@ec2-174-129-16-183.compute-1.amazonaws.com:5432/d9nfe5sbe4g6e1', None)
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
    DATABASE_URL = "postgres://arvkivrjdndtyi:5a66f7f6188fedb72833f90a3777bdea5b29fdb0be70c015ffca9f7bfe377eb2@ec2-174-129-16-183.compute-1.amazonaws.com:5432/d9nfe5sbe4g6e1"
    DATABASE_URL = DATABASE_URL.replace("postgres", "postgresql")
    MUST_JOIN = ""
    if MUST_JOIN.startswith("@"):
        MUST_JOIN = MUST_JOIN[1:]
