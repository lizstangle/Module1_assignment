from flask import Flask

from random import choice

app = Flask(__name__)

@app.route('/')
def homepage():
    """Shows a greeting to the user."""
    return 'Are you there, world? It\'s me, Ducky!'

@app.route('/animal/<users_animal>')
def favorite_animal(users_animal):
    """Display a message to the user that changes based on their favorite animal."""
    return f'Wow, {users_animal} is my favorite animal, too!'

@app.route('/dessert/<users_dessert>')
def favorite_dessert(users_dessert):
    """Display a message to the user that changes based on their favorite dessert."""
    return f'How did you know I liked {users_dessert}?'

@app.route('/madlibs/<adjective>/<noun>')        
def favorite_mad_lib(adjective, noun):
    """Display a message to the user that changes based on their favorite madlib."""
    return f'Flip-flops are a staple of any {adjective} {noun}.'

@app.route('/multiply/<number1>/<number2>')        
def multiply(number1, number2):
    if number1.isdigit() and number2.isdigit() == True:
        answer = int(number1) * int(number2)
        """Display a message to the user that changes based on the numbers selected."""
        return f'{number1} times {number2} is {answer}.'
    return f'Invalid inputs. Please try again by entering 2 numbers!'

#     @app.route('/multiply/<num_1>/<num_2>')
# def multiply(num_1, num_2):
#     if num_1.isdigit() and num_2.isdigit() == True: 
#         result: int = int(num_1) * int(num_2)
#         return f"The result is {result}"
#     else: 
#         return 'Invalid inputs. Please try again by entering 2 numbers!'

@app.route('/sayntimes/<word>/<n>')
def sayntimes(word, n):
    n = int(n)
    repeatedWord = ''
    for i in range(n):   
        repeatedWord += word
    return repeatedWord

@app.route('/dicegame/')
def roll_dice():
    sides = [1, 2, 3, 4, 5, 6]
    result = choice(sides)
    if result == 6:
        return "You Rolled A 6, You Won!" 
    else: 
        return f"You Rolled a {result}, You Lose!"


# TODO: Follow the assignment instructions to complete the required routes!
# (And make sure to delete this TODO message when you're done!)

if __name__ == '__main__':
    app.run(debug=True)
