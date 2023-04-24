import os
from flask import Flask, render_template
from flask_socketio import SocketIO, emit
import serial

# Configurer la communication série
ser = serial.Serial('COM3', 9600)  # Change 'COM3' par le port approprié sur ton système

app = Flask(__name__)
app.config['SECRET_KEY'] = os.urandom(24)
socketio = SocketIO(app)

def envoyer_commande_microcontroleur(commande):
    ser.write(commande.encode('utf-8'))

@app.route('/')
def accueil():
    return render_template('index.html')

# Cette fonction gère les commandes reçues depuis la page Web et les envoie au microcontrôleur.
@socketio.on('commande')
def gerer_commande(data):
    commande = data['commande']
    print(f'Commande reçue: {commande}')

    # Selon la commande reçue, envoie la commande correspondante au microcontrôleur
    if commande == 'avancer':
        envoyer_commande_microcontroleur('A')
    elif commande == 'reculer':
        envoyer_commande_microcontroleur('B')
    elif commande == 'gauche':
        envoyer_commande_microcontroleur('L')
    elif commande == 'droite':
        envoyer_commande_microcontroleur('R')
    else:
        print('Commande inconnue')

    # Envoie un message de statut indiquant que la commande a été reçue
    emit('statut', {'statut': 'Commande reçue: ' + commande}, broadcast=True)

if __name__ == '__main__':
    socketio.run(app)
