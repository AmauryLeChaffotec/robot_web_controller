const socket = io.connect();

// Fonction pour envoyer des commandes
function envoyerCommande(commande) {
    socket.emit('commande', { commande: commande });
}

// Je gére les messages de statut reçus du serveur
socket.on('statut', (data) => {
    document.getElementById('statut').innerText = data.statut;
});
