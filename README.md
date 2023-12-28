# Application Planning Poker

## Aperçu
Le Planning Poker est une technique d'estimation et de planification agile basée sur le consensus. Notre application, "Pocker App", est conçue pour rendre ce processus fluide et interactif pour les équipes agiles. Elle permet aux équipes d'estimer leur travail de manière amusante, facile et rapide.

## Fonctionnalités
- **Création de jeu :** Les utilisateurs peuvent démarrer une nouvelle partie, choisir un nom de jeu et sélectionner le mode (Strict, Moyenne, Médiane, Majorité Absolue, Majorité Relative).
- **Gestion des joueurs :** Ajout ou suppression de joueurs de manière dynamique pour chaque partie.
- **Gestion des tâches :** Permet d'ajouter des tâches et facilite le vote sur chaque tâche.
- **Système de vote :** Les joueurs peuvent voter sur les tâches en utilisant une variété d'options de cartes.
- **Mises à jour en temps réel :** L'application se met à jour en temps réel au fur et à mesure que les joueurs rejoignent, votent et que les tâches sont ajoutées.
- **Intégration Firebase :** Mises à jour et stockage de la base de données en temps réel avec Firebase.

## Pile technologique
- Dash de Plotly
- Firebase Realtime Database
- Python

## Configuration et installation
1. **Cloner le dépôt :**

2. **Installer les dépendances :**
Assurez-vous d'avoir Python installé sur votre système. Ensuite, installez les paquets requis :

3. **Configuration Firebase :**
- Remplacez `'chemin/vers/votre/credentials.json'` par le chemin vers votre fichier JSON de clé de compte de service Firebase.
- Mettez à jour l'URL `databaseURL` dans la méthode `firebase_admin.initialize_app` avec l'URL de votre base de données Firebase.

4. **Lancement de l'application :**
Pour démarrer le serveur, exécutez :

## Utilisation
- Accédez à la page principale pour démarrer une nouvelle partie ou rejoindre une partie existante.
- Créez une nouvelle partie en saisissant un nom de jeu et en sélectionnant un mode.
- Ajoutez des joueurs et des tâches, puis commencez à voter sur les tâches.
- Chaque joueur sélectionne une carte pour voter sur une tâche. Une fois que tous les joueurs ont voté, les votes sont révélés.

## Contribuer
Les contributions à ce projet sont les bienvenues. Veuillez forker le dépôt et soumettre une demande de tirage avec vos modifications.

## Licence
Ce projet est sous licence [MIT License](LICENSE.md).

