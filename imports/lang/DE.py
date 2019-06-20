#####
#STANDARD LINES
#####
st_welcome = str("Willkommen auf der Punkteübersicht von Space Frontiers.\n")
st_invalid_input = str("Eingabe ungültig, bitte erneut versuchen.\n")
st_press_enter = str("\nDrücken Sie [ENTER], um fortzufahren.")
st_input = str("Eingabe: ")
st_choice = str("Bist du sicher? [y/n]]n")


#####
#MENU LINES
#####
menu = str("""
1. Team erstellen
2. Spieler hinzufügen
3. Ergebnisübersicht anzeigen
4. Punkte hinzufügen
5. Aktuelle Daten löschen
6. Speichern Sie und beenden Sie
""")

menu_choice = str("Gib deine wahl: ")
menu_clear_choice = str("Möchten Sie wirklich alle Daten löschen? [y/n]\n")
menu_exit_choice = str("Möchten Sie dieses Programm wirklich schließen? [y/n]\n")


#####
#ADD LINES
#####
add_teamname = str("Gib den Namen des Teams an\n")
add_team_header = str("Aktuelle Teams:")
add_team_not_exist = str("%s existiert nicht")
add_team_choice = str("\nGeben Sie einen nicht existierenden Teamnamen ein oder drücken Sie 'X', um zurückzugehen.n\ NA kann bis zu 18 Zeichen lang sein.")
add_team_exist_choice = str("\nGeben Sie einen vorhandenen Teamnamen ein oder drücken Sie 'X', um zurückzugehen.")
add_team_already_exist = str("%s existiert bereits")
add_team_empty_input = str("Sie können keinen leeren Namen eingeben.")
add_team_too_long = str("Ein Teamname kann bis zu 18 Zeichen lang sein.")
add_player_amount = str("Wie viele Spieler möchten Sie hinzufügen? %s?\n")
add_player_name = str("Geben Sie den Namen des Spielers %i ein.")
add_player_already_in_team = str("%s ist schon in %s.\n")
add_point_menu = str("""Wo möchten Sie Punkte hinzufügen?
1. Geschwindigkeit (s)
2. Wirksamkeit (e)
Eingabe: """)
add_point_amount = str("Wie viele Punkte möchten Sie hinzufügen? %s?\n")
add_speed = str("Geschwindigkeit")
add_effectivity = str("Wirksamkeit")
add_has_points = str("%s: %s punkte")

#####
#SHOW LINES
#####
show_has_points = str("%s hat %s Punkte und besteht aus")
show_has_points_indivi = str("%s hat %s punkte")
show_table_header_teamname = str("Teamname")
show_table_header_total_points = str("Punkten")
show_table_header_indivi_points = str("Einzelpunkt")
show_table_header_team_members = str("Teammitglieder")
show_invidi_points = str("\Drücken Sie [ENTER], um einzelne Punkte anzuzeigen, oder 'X', um zurückzugehen. n\Eingabe: ")

#####
#CSV LINES
#####
csv_clear_succesful = str("Punkteübersicht erfolgreich entfernt")
csv_save = str("Alle Daten wurden gespeichert")