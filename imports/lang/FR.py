#####
#STANDARD LINES
#####
st_welcome = str("Bienvenue dans l’aperçu des points de Space Frontiers.\n")
st_invalid_input = str("Import invalide, veuillez réessayer.\n")
st_press_enter = str("\nAppuyez sur [ENTER] pour continuer.")
st_input = str("Entrée: ")
st_choice = str("Êtes-vous sûr? [y/n]n")


#####
#MENU LINES
#####
menu = str("""
1. Créer une équipe
2. Ajouter des joueurs
3. Afficher l'aperçu des partitions
4. Ajouter des points
5. Supprimer les données actuelles
6. Sauvegarder et quitter
""")

menu_choice = str("Donnez votre choix:")
menu_clear_choice = str("Êtes-vous sûr de vouloir supprimer toutes les données? [y/n]\n")
menu_exit_choice = str("Êtes-vous sûr de vouloir fermer ce programme? [y/n]\n")


#####
#ADD LINES
#####
add_teamname = str("Donnez le nom de l'équipe\n")
add_team_header = str("Equipes actuelles:")
add_team_not_exist = str("%s n'existe pas.")
add_team_choice = str("\nEntrez un nom d’équipe inexistant ou appuyez sur 'X' pour revenir en arrière. n\A nom peut comporter 18 caractères au maximum.")
add_team_exist_choice = str("\nEntrez un nom d’équipe existant ou appuyez sur 'X' pour revenir en arrière.")
add_team_already_exist = str("%s existe déjà.")
add_team_empty_input = str("Vous ne pouvez pas entrer un nom vide.")
add_team_too_long = str("Un nom d'équipe peut comporter jusqu'à 18 caractères.")
add_player_amount = str("Combien de joueurs voulez-vous ajouter à %s?\n")
add_player_name = str("Entrez le nom du joueur %i.")
add_player_already_in_team = str("%s est déjà dans %s.\n")
add_point_menu = str("""Où voulez-vous ajouter des points?
1. Vitesse (s)
2. Efficacité (e)
Entrée: """)
add_point_amount = str("Combien de points voulez-vous ajouter à %s?\n")
add_speed = str("vitesse")
add_effectivity = str("l'efficacité")
add_has_points = str("%s: %s des points")

#####
#SHOW LINES
#####
show_has_points = str("%s a %s points et consiste en")
show_has_points_indivi = str("%s s %s points")
show_table_header_teamname = str("Nom de l'équipe")
show_table_header_total_points = str("Points")
show_table_header_indivi_points = str("Point individuel")
show_table_header_team_members = str("Membres de l'équipe")
show_invidi_points = str("\nAppuyez sur [ENTER] pour afficher des points individuels ou sur 'X' pour revenir en arrière. n\Input: ")

#####
#CSV LINES
#####
csv_clear_succesful = str("Aperçu des points supprimé avec succès")
csv_save = str("Toutes les données ont été sauvegardées")