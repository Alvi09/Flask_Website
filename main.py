# pip install flask-login for logging our users in
# pip install flask-sqlalchemy is wrapper for SQL to make it easier for our database
from website import create_app

app = create_app()

if __name__ == "__main__":  # Only if we run this function, not imports, then it'll execute the following lines
    app.run(debug = True)   # debug = True, everytime we make a change to website, it'll automatically rerun the server
