from flask import Flask
import datetime

app = Flask(  # Create a flask app
    __name__,
    template_folder='templates',  # Name of html file folder
    static_folder='static'  # Name of directory for static files
)


@app.route('/')
def mainPage():
  date = datetime.datetime.now()
  return f"Datum: {date}"
