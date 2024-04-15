# Projet-Python
Projet pour une interface graphique de pilotage et acquisition d'un robot turtle bot

3 axes principaux:
    - Démarrage et Connexion avec le robot
    - Acquisition des données
    - Pilotage du robot

Démarrage et Connexion avec le robot:
    Tâches à accomplir:
        - Attendre que l'utilisateur donne la bonne adresse du robot (ROS URI et Hostname)
        - Permettre le démarrage ou l'arrêt de l'acquisition des données ainsi que du pilotage du robot
        - Permettre à l'utilisateur de savoir si l'acquisition est en cours ou non à l'aide d'un voyant

Acquisition des données:
    Tâches à accomplir:
        - Effectuer l'acquisition de données (Position (x,y) - Vitesse linéaire - Vitesse angulaire)
        - Stocker les information dans des fichiers dumps
        - permettre la visualisation des ces données à l'aide de graphiques (maplotlib)

Pilotage du Robot:
    Tâches à accomplir:
        - Permettre le pilotage du robot à l'aide de touche du clavier
        - Permettre la variation de la vitesse angulaire et de la vitesse linéaire à l'aide de sliders sur l'interface