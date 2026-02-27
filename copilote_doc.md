# Documentation d'Arrera Copilote

## Fonctions spécifiques à Copilote

Tout comme Ryley, Arrera Copilote possède 4 modes de fenêtre : 

- *Mode normal* : Mode de fenêtre par défaut dans Arrera Copilote. 
- *Mode petite fenêtre* : Le mode petite fenêtre peut être lancé de deux façons : depuis le bouton à droite de la zone de texte ou en disant "fenêtre réduite".
- *Mode CodeHelp* : Le mode CodeHelp est un mode qui ajoute des boutons pour lancer simplement les outils intégrés à CodeHelp. Il se lance depuis le bouton à gauche de la zone de texte ou en disant "mode CodeHelp" à l'assistant.
- *Mode petite fenêtre CodeHelp* : Fait la même chose que le mode CodeHelp sauf que, dû à la petite fenêtre, les boutons des outils CodeHelp ne sont pas affichés.

## Explication des boutons de la zone de recherche 

L'explication des boutons va de gauche à droite

### Mode normal 

![mode_normal_copilote.png](img_doc/mode_normal_copilote.png)

- *Bouton paramètres* : Ouvre les paramètres de Copilote.
- *Bouton CodeHelp* : Passe l'assistant en mode CodeHelp.
- *Bouton petite fenêtre* : Passe l'assistant en mode petite fenêtre (En mode non CodeHelp).
- *Bouton paramètres rapides* : Ouvre les paramètres rapides de Copilote.

### Mode petite fenêtre

![mode_normal_little_copilote.png](img_doc/mode_normal_little_copilote.png)

- *Bouton paramètres* : Ouvre les paramètres de Copilote.
- *Bouton CodeHelp* : Passe l'assistant en mode CodeHelp petite fenêtre.
- *Bouton fenêtre normale* : Passe l'assistant en mode fenêtre normale.
- *Bouton paramètres rapides* : Ouvre les paramètres rapides de Copilote.

### Mode CodeHelp 

![mode_normal_codehelp_copilote.png](img_doc/mode_normal_codehelp_copilote.png)

- *Bouton paramètres* : Ouvre les paramètres de Copilote.
- *Bouton Copilote* : Désactive le mode CodeHelp.
- *Bouton petite fenêtre* : Passe l'assistant en mode petite fenêtre CodeHelp.
- *Bouton paramètres rapides* : Ouvre les paramètres rapides de Copilote.

### Mode petite fenêtre CodeHelp

![mode_little_codehelp_copilote.png](img_doc/mode_little_codehelp_copilote.png)

- *Bouton paramètres* : Ouvre les paramètres de Copilote.
- *Bouton Copilote* : Passe en mode normal en petite fenêtre.
- *Bouton fenêtre normale* : Passe l'assistant en mode fenêtre normale CodeHelp.
- *Bouton paramètres rapides* : Ouvre les paramètres rapides de Copilote.

## Explication des paramètres rapides (Quick settings)

### Mode fenêtre normale

![quick_setting_normal.png](img_doc/quick_setting_normal.png)

- Bouton Micro (Bouton avec le logo de micro) : Active ou désactive le système de trigger word de l'assistant.
- Bouton sons (Bouton avec un logo de haut-parleur) : Active ou désactive la lecture à voix haute de la réponse de l'assistant.
- Bouton Paramètres : Lance les paramètres d'Arrera Copilote.
- Bouton Fermer : Ferme les paramètres rapides.


### Mode petite fenêtre

![quick_setting_little.png](img_doc/quick_setting_little.png)

- Bouton Micro (Bouton avec le logo de micro) : Active ou désactive le système de trigger word de l'assistant.
- Bouton sons (Bouton avec un logo de haut-parleur) : Active ou désactive la lecture à voix haute de la réponse de l'assistant.
- Bouton Fermer : Ferme les paramètres rapides.

## Explication des paramètres

![setting_copilote.png](img_doc/setting_copilote.png)

- *Paramètres généraux* : Paramètre qui permet d'ajouter ou supprimer les dossiers d'Arrera Work et Arrera Download
- *Paramètres utilisateur* : Paramètre pour modifier le nom, le prénom et le genre avec lesquels vous souhaitez que votre assistant vous appelle
- *Paramètres météo* : Permet de gérer les villes enregistrées dans le système de météo de l'assistant
- *Intelligence Artificielle* : Permet d'activer ou désactiver l'utilisation de modèles d'intelligence artificielle et de télécharger de nouveaux modèles 
- *Paramètres de recherche* : Paramètre pour changer le moteur de recherche utilisé par l'assistant
- *Logiciels externes* : Permet d'ajouter ou supprimer les logiciels enregistrés dans l'assistant pour qu'il puisse vous les ouvrir 
- *Raccourcis internet* : Permet d'ajouter ou supprimer les raccourcis internet enregistrés dans l'assistant pour qu'il puisse vous les ouvrir 
- *Adresse GPS* : Permet de modifier les adresses de votre lieu de travail et de domicile enregistrées dans l'assistant pour qu'il puisse vous calculer les meilleurs itinéraires
- *Intégration Github* : Permet d'ajouter le token github pour les fonctions de codehelp
- *Paramètres du micro* : Permet d'ajouter les mots de déclenchement de l'assistant et d'activer ou non le son au déclenchement du micro
- *Retour* : Retourne à l'assistant

## Météo

Obtenez les prévisions météorologiques pour votre localisation ou vos lieux enregistrés.

*   **Météo actuelle** : "meteo", "temps qu'il fait"
*   **Température** : "temperature", "degre", "degres"
*   **Prévisions** :
    *   Demain matin : "demain matin" (avec un mot-clé météo)
    *   Demain après-midi : "demain apres midi" (avec un mot-clé météo)
*   **Lieux spécifiques** :
    *   Domicile : "domicile", "maison", "chez moi", "residence", "appartement"
    *   Travail : "bureau", "travail", "entreprise", "ecole", "universite"

## Résumé (Breef)

Obtenez une synthèse rapide de vos informations.

*   **Résumé général** : "resume", "breef", "recapitulatif", "synthèse"
*   **Actualités** : "actualites", "infos", "news", "titres"
*   **Tâches** : "taches", "a faire", "devoirs", "missions"

## GPS et Itinéraire

Gérez vos déplacements et votre localisation.

*   **Coordonnées GPS** : "gps", "position", "coordonnees", "localisation"
*   **Itinéraire** :
    *   Lancer : "lance l'itineraire", "demarre l'itineraire"
    *   Point de départ : "je pars de", "je compte partir de", "je veux aller a"
    *   Point d'arrivée : "je veux arriver a", "ma destination est", "je desire arriver a"
    *   Aide : "aide", "help"

## Actualités

*   **Consulter** : "actualites", "nouvelles", "infos", "news"

## Traducteur

*   **Ouvrir** : "traducteur", "traduction", "traduire", "translate"

## Documentation Développement

Recherchez de la documentation technique spécifique.

*   **DevDoc** : "cherche [sujet] sur devdoc"
*   **Microsoft Learn** : "cherche [sujet] sur learn microsoft"
*   **Python** : "cherche [sujet] sur python"
*   **GitHub** : "cherche [sujet] sur github"

## Outils de Développement

*   **Organisateur de variables** : "ouvre l'organisateur de variable", "lance orga var"
*   **Sélecteur de couleurs** : "ouvre le sélecteur de couleur"
*   **GitHub** :
    *   Site Web : "ouvre github"
    *   Gestionnaire de projet : "ouvre le gestionnaire github"
*   **Librairie de projets** : "ouvre la librairie"

## Applications et Sites Web

*   **Ouvrir un logiciel/site** : "ouvre [nom]", "lance [nom]", "affiche [nom]"
*   **YouTube** : "ouvre youtube"
*   **YouTube Music** : "ouvre youtube music"
*   **Arrera Download** : "ouvre youtube downloader", "lance arrera download"
*   **Calculatrice** :
    *   Standard : "ouvre calculatrice"
    *   Complexe : "ouvre calculatrice mode complexe"
    *   Pythagore : "ouvre calculatrice mode pythagore"

## Radio

*   **Lancer une station** : "lance la radio [nom]"
    *   *Stations supportées* : Europe 1, Europe 2, France Info, France Inter, France Musique, France Culture, France Bleu, Fun Radio, NRJ, RFM, Nostalgie, Skyrock, RTL.
*   **Arrêter** : "arrete la radio", "stoppe la radio"

## Ressources Disponibles

*   **Lister les logiciels** : "dis moi les logiciels"
*   **Lister les sites** : "dis moi les sites"
*   **Lister les radios** : "dis moi les radios"

## Interface

*   **Activer un mode** : "lance le mode [1-6]"
*   **Désactiver** : "ferme le mode"

## Recherche Internet

*   **Recherche simple** : "recherche [sujet]", "search [sujet]"
*   **Grande recherche** : "bigsearch [sujet]", "grand recherche [sujet]"

## Services Divers

*   **Lecture de texte** : "lis le texte", "lecture du passage"
*   **Calcul rapide** : "calcule [expression]" (+, -, *, /)
*   **Aide Assistant** : "ouvre la documentation", "lance l'aide"
*   **Correction orthographique** : "corrige [texte]"

## Temps et Agenda

*   **Heure** : "quelle heure est-il", "heure"
*   **Date** : "quelle est la date", "date"
*   **Outils** : "lance le chronometre", "ouvre l'horloge", "met un minuteur"
*   **Agenda** :
    *   Voir : "ouvre l'agenda"
    *   Ajouter : "ajoute a l'agenda"
    *   Supprimer : "supprime de l'agenda"

## Gestion des Tâches (To-Do List)

*   **Voir** : "ouvre les taches", "montre ma to do list"
*   **Ajouter** : Dire "ajoute une tache", puis préciser le nom.
*   **Supprimer** : "supprime une tache"
*   **Terminer** : Dire "tache finie", puis préciser le nom.
*   **Statistiques** : "combien de tache [aujourd'hui/demain]"

## Arrera Work (Gestion de Projets)

*   **Aide** : "aide work"
*   **Projets** :
    *   Créer : "cree un projet nommer [nom]"
    *   Ouvrir : "ouvre le projet [nom]"
    *   Lister : "liste les projets"
    *   Fermer : "ferme le projet"
*   **Contenu du Projet** :
    *   Tâches : "montre les taches du projet", "ajoute une tache au projet", "supprime une tache du projet"
    *   Fichiers : "cree un fichier dans le projet" (suivre les étapes), "liste les fichiers du projet"
*   **Bureautique** :
    *   Tableur : "ouvre tableur", "ajoute valeur/somme/moyenne..."
    *   Traitement de texte : "ouvre word", "lis le document", "ecrit dans le document"
*   **Interface** : "ouvre interface work"