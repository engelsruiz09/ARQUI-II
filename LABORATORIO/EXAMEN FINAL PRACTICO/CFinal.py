from flask import *
import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BOARD)
#GPIO.setup(12, GPIO.OUT)

Texto = ""
POSx = 0
POSy = 0
POSr = 0
NUM1 = 0
NUM2 = 0
NUM3 = 0
NUM4 = 0
NUM5 = 0
NUM6 = 0
NUM7 = 0
NUM8 = 0
NUM9 = 0
NUM10 = 0
NUM11 = 0
NUM12 = 0
NUM13 = 0
NUM14 = 0
NUM15 = 0
NUM16 = 0
rows, cols = (4, 4)
arr = [[0 for i in range(cols)] for j in range(rows)]

app = Flask(__name__)

@app.route('/', methods = ['GET', 'POST'])
def main():
    return render_template('templates.html')

@app.route('/Dos', methods = ['GET', 'POST'])
def camina():
    num = 0
    Texto1 = ''
    Texto2 = ''
    Texto3 = ''
    Texto4 = ''
    Texto5 = ''
    Texto6 = ''
    Texto7 = ''
    Texto8 = ''
    Texto9 = ''
    Texto10 = ''
    Texto11 = ''
    Texto12 = ''
    Texto13 = ''
    Texto14 = ''
    Texto15 = ''
    Texto16 = ''
    global POSr
    global POSx
    global POSy
    global arr

    POSr = POSx * POSy

    if POSr == 0:
        Texto1 = 'X'
    
    return render_template('templates.html', Texto1 = Texto1, Texto2 = Texto2, Texto3 = Texto3, Texto4 = Texto4, Texto5 = Texto5, Texto6 = Texto6, Texto7 = Texto7, Texto8 = Texto8, Texto9 = Texto9, Texto10 = Texto10, Texto11 = Texto11, Texto12 = Texto12, Texto13 = Texto13, Texto14 = Texto14, Texto15 = Texto15, Texto16 = Texto16)

if __name__ == '__main__':
    app.run(debug = True, host = '0.0.0.0')