# Projet de détection d'objects #

### Ce projet a pour but de créer un modèle de détection d'objets en utilisant YOLOv8 (You Only Look Once version 8). Il s'agit d'un réseau de neurones convolutifs pour la détection d'objets en temps réel. Le projet se concentre sur la détection de voitures dans des vidéos, en utilisant un modèle personnalisé entraîné sur un jeu de données spécifique. ###

### Structure du Projet ###
#### Entraînement du Modèle : ####

Le modèle YOLOv8 est construit à partir de zéro en utilisant un fichier de configuration (yolov8n.yaml).
Le modèle est ensuite entraîné sur un jeu de données spécifié dans un fichier de configuration (config.yaml) pendant un certain nombre d'époques.

#### Traitement de la Vidéo : ####

- Une vidéo d'entrée contenant des voitures (Cars.mp4) est lue et traitée cadre par cadre.
- Un modèle YOLOv8 pré-entraîné est utilisé pour détecter les voitures dans chaque cadre de la vidéo.
- Pour chaque détection, une boîte englobante est dessinée autour des voitures détectées, et le nom de la classe (car) est affiché.
- La vidéo avec les détections est ensuite sauvegardée sous un nouveau nom de fichier.

#### Fichiers et Répertoires ####
- yolov8n.yaml : Fichier de configuration pour construire le modèle YOLOv8.
- config.yaml : Fichier de configuration pour l'entraînement du modèle, spécifiant les chemins des données d'entraînement et de validation.
- Videos/ : Répertoire contenant la vidéo d'entrée Cars.mp4.
- runs/detect/train/weights/last.pt : Chemin vers le modèle YOLOv8 entraîné.
- Dataset/ : Répertoire racine du jeu de données avec les sous-répertoires train/images et valid/images contenant les images d'entraînement et de validation respectivement.
