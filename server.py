"""Greeting Flask app."""

from random import choice

from flask import Flask, request

# "__name__" is a special Python variable for the name of the current module
# Flask wants to know this to know what any imported things are relative to.
app = Flask(__name__)

AWESOMENESS = [
    'awesome', 'terrific', 'fantastic', 'neato', 'fantabulous', 'wowza',
    'oh-so-not-meh', 'brilliant', 'ducky', 'coolio', 'incredible',
    'wonderful', 'smashing', 'lovely']


@app.route('/')
def start_here():
    """Home page."""

    return """
    <!doctype html>
    <html>
      Hi! This is the home page.
      <a href="/hello">Hello!</a>
      <a href="/hellodiss">Loser!</a>
    </html>
    """


@app.route('/hello')
def say_hello():
    """Say hello and prompt for user's name."""

    return """
    <!doctype html>
    <html>
      <head>
        <title>Hi There!</title>
      </head>
      <body>
        <h1>Hi There!</h1>
        <form action="/greet">
          What's your name? <input type="text" name="person">

          Choose your compliment:
          
          <input type="radio" name="compliment" value="amazing">
          <label>you are amazing!</label>

          <input type="radio" name="compliment" value="rad">
          <label>you are rad!</label>

          <input type="radio" name="compliment" value="radiant">
          <label>you radiate light</label>

          <input type="submit" value="Submit">
        </form>
      </body>
    </html>
    """
@app.route('/hellodiss')
def diss():
    """Say diss and prompt for user's name."""

    return """
    <!doctype html>
    <html>
      <head>
        <title>Hi Loser</title>
      </head>
      <body>
        <h1>Hi Loser</h1>
        <form action="/diss">
          What's your name? <input type="text" name="person">

          How are you felling today?
          
          <input type="radio" name="diss" value="stupid">
          <label>stupid</label>

          <input type="radio" name="diss" value="inept">
          <label>inept</label>

          <input type="radio" name="diss" value="angry">
          <label>angry</label>

          <input type="submit" value="Submit">
        </form>
      </body>
    </html>
    """



@app.route('/greet')
def greet_person():
    """Get user by name."""

    player = request.args.get("person")
    compliment = request.args.get("compliment")
  
    # compliment = choice(AWESOMENESS)

    return """
    <!doctype html>
    <html>
      <head>
        <title>A Compliment</title>
      </head>
      <body>
        Hi, {}! I think you're {}!
      </body>
    </html>
    """.format(player, compliment)


@app.route('/diss')
def diss_person():
    """Get user by name."""

    player = request.args.get("person")
    diss = request.args.get("diss")

    return """
    <!doctype html>
    <html>
      <head>
        <title>A Diss</title>
      </head>
      <body>
        Hi, {}! I think you're {}!
      </body>
    </html>
    """.format(player, diss)
    


if __name__ == '__main__':
    # debug=True gives us error messages in the browser and also "reloads"
    # our web app if we change the code.
    app.run(debug=True, host="0.0.0.0")
