#####
#STANDARD LINES
#####
st_welcome = str("Welkom bij het puntenoverzicht van Space Frontiers.\n")
st_invalid_input = str("Invoer ongeldig, probeer het nog een keer.\n")
st_press_enter = str("\nDruk op [ENTER] om verder te gaan.")
st_input = str("Invoer: ")
st_choice = str("Weet je het zeker? [y/n]]n")


#####
#MENU LINES
#####
menu = str("""
1. Team aanmaken
2. Spelers toevoegen
3. Toon scoreoverzicht
4. Voeg punten toe
5. Verwijder huidige gegevens
6. Opslaan en afsluiten
""")

menu_choice = str("Geef uw keuze: ")
menu_clear_choice = str("Weet je zeker om alle gegevens te verwijderen? [y/n]\n")
menu_exit_choice = str("Weet je zeker om dit programma te sluiten? [y/n]\n")


#####
#ADD LINES
#####
add_teamname = str("Geef team naam\n")
add_team_header = str("Huidige teams:")
add_team_not_exist = str("%s bestaat niet.")
add_team_choice = str("\nVul een niet-bestaand team naam in of druk op 'X' om terug te gaan.\nEen naam mag maximaal 18 karakters lang zijn.")
add_team_exist_choice = str("\nVul een bestaand team naam in of druk op 'X' om terug te gaan.")
add_team_already_exist = str("%s bestaat al.")
add_team_empty_input = str("Je kunt geen lege naam invullen.")
add_team_too_long = str("Een teamnaam mag maximaal 18 karakters lang zijn.")
add_player_amount = str("Hoeveel spelers wil je toevoegen aan %s?\n")
add_player_name = str("Vul de naam van speler %i in.")
add_player_already_in_team = str("%s zit al in %s.\n")
add_point_menu = str("""Waar wil je punten aan toevoegen?
1. Snelheid (s)
2. Effectiviteit (e)
Invoer: """)
add_point_amount = str("Hoeveel punten wil je toevoegen aan %s?\n")
add_speed = str("snelheid")
add_effectivity = str("effectiviteit")
add_has_points = str("%s: %s punten")

#####
#SHOW LINES
#####
show_has_points = str("%s heeft %s punten en bestaat uit")
show_has_points_indivi = str("%s heeft %s punten")
show_table_header_teamname = str("Team naam")
show_table_header_total_points = str("Punten")
show_table_header_indivi_points = str("Individueel punt")
show_table_header_team_members = str("Teamleden")
show_invidi_points = str("\nDruk op [ENTER] om individuele punten in te zien, of op 'X' om terug te gaan.\nInvoer: ")

#####
#CSV LINES
#####
csv_clear_succesful = str("Puntenoverzicht succesvol verwijderd")
csv_save = str("Alle gegevens zijn opgeslagen")