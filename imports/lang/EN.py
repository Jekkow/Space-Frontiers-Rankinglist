#####
#STANDARD LINES
#####
st_welcome = str("Welcome to the rankinglist of Space Frontiers.\n")
st_invalid_input = str("Input invalid, try again.\n")
st_press_enter = str("\nPress [ENTER] to continue.")
st_input = str("Input: ")
st_choice = str("Are you sure? [y/n]\n")


#####
#MENU LINES
#####
menu = str("""
1. Add team
2. Add player
3. Show rankinglist
4. Assing points
5. Clear rankinglist
6. Save and exit
""")

menu_choice = str("Give choice: ")
menu_clear_choice = str("Are you sure to delete all data? [y/n]\n")
menu_exit_choice = str("Are you sure to exit? [y/n]\n")


#####
#ADD LINES
#####
add_teamname = str("Give team name\n")
add_team_header = str("Current teams:")
add_team_not_exist = str("%s does not exist.")
add_team_choice = str("Give team name or press 'X' to cancel: ")
add_team_exist_choice = str("\nGive an existing tean name or press 'X' to cancel: ")
add_team_already_exist = str("This team already exist.")
add_team_empty_input = str("You can't give an empty teamname")
add_team_too_long = str("Teamname can only be 18characters long.")
add_player_amount = str("How many players do you want to add on %s?\n")
add_player_name = str("Give player name of %i\n")
add_player_already_in_team = str("%s Is already in %s.\n")
add_point_menu = str("""
Wich points do you want to assign?
1. Speed (s)
2. Efficiency(e)
Input: """)
add_point_amount = str("How many points do you want to add to %s?\n")
add_speed = str("speed")
add_effectivity = str("efficiency")
add_has_points = str("%s: %s points")


#####
#SHOW LINES
#####
show_has_points = str("%s has %s points")
show_has_points_indivi = str("%s has %s points")
show_table_header_teamname = str("Team name")
show_table_header_total_points = str("Points")
show_table_header_indivi_points = str("Individual points")
show_table_header_team_members = str("Team members")
show_invidi_points = str("\nPress [ENTER] to see individual points, or press 'X' to cancel.\nInput: ")


#####
#CSV LINES
#####
csv_clear_succesful = str("Rankinglist is succesfully cleared")
csv_save = str("All data is succesfully saved")
