# Importation des modules nécessaires de Flask
from flask import Flask, send_file

# Initialisation de l'application Flask
app = Flask(__name__)

# Route permettant de télécharger le fichier malware.sh
@app.route('/malware')
def download_malware():
    # Envoie le fichier malware.sh au client avec une option de téléchargement
    return send_file('malware.sh', as_attachment=True)

# Route permettant de télécharger le fichier antimalware.sh
@app.route('/antimalware')
def download_antimalware():
    # Envoie le fichier antimalware.sh au client avec une option de téléchargement
    return send_file('antimalware.sh', as_attachment=True)

# Vérification si le script est exécuté directement
if __name__ == '__main__':
    # Lancement du serveur Flask en écoutant sur toutes les interfaces réseau (0.0.0.0) et le port 8000
    app.run(host='0.0.0.0', port=8000)
