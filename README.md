# Contrôleur de robot via une interface web

Ce projet permet de contrôler un robot à l'aide d'une interface web. Le projet utilise Flask pour créer un serveur web et communique avec le robot via un microcontrôleur.

## Prérequis

- Python 3.6 ou supérieur
- pip (outil de gestion des paquets Python)

## Installation et configuration

tu suis les étapes ci-dessous pour configurer et exécuter le projet :

### 1. Cloner le dépôt

Tu clone mon dépôt sur ta machine locale en utilisant la commande suivante :

```bash
git clone https://github.com/AmauryLeChaffotec/robot_web_controller.git
```
### 2. Créer un environnement virtuel
tu accèdes au répertoire du projet et créez un environnement virtuel Python pour isoler les dépendances :

```bash

cd robot-web-controller
python3 -m venv env


```

### 3. Activer l'environnement virtuel
tu actives ton environnement virtuel en exécutant la commande pour ton système d'exploitation :

Sur Windows :
```bash 
env\Scripts\activate

```

sur linux :
```bash 
source env/bin/activate
```

### 4. Installer les dépendances
tu installes les bibliothèques requises en utilisant le fichier requirements.txt 

```bash
pip install -r requirements.txt


```

### 5. Lancer le serveur Flask
tu executes le serveur Flask en utilisant la commande suivante :

```bash

python serveur.py


```

Le serveur doit maintenant être en cours d'exécution et accessible à l'adresse http://127.0.0.1:5000 dans ton navigateur web.

### Utilisation
tu ouvres un navigateur web et tu accéde à l'adresse http://127.0.0.1:5000. tu arrivera sur l'interface de contrôle du robot avec des boutons pour avancer, reculer, tourner à gauche et tourner à droite. Tu cliques sur les boutons pour envoyer les commandes au robot.


