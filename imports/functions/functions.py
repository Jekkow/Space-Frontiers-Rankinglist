import os
import csv
import sys

os.system('color 3f')
sys.path.insert(0, 'imports/lang')
lang = input("""Typ 'NL' voor Nederlands.
Type 'EN' for English.
Geben Sie 'DE' für Deutsch.
Tapez "FR" pour le français.
Invoer: """).lower()
if lang in ["en"]:
    from EN import *
elif lang in ["de"]:
    from DE import *
elif lang in ["fr"]:
    from FR import *
else:
    from NL import *

class start_functions:
    if(os.path.exists("data/Teams.csv") and
           os.path.exists("data/Score.csv") and
           os.path.exists("data/Score_Individual.csv")):
            pass
    else:
        try:
            os.mkdir('data')
        except FileExistsError:
            pass
        with open("data/Teams.csv", "a+", newline='') as file:
            pass
        with open("data/Score.csv", "a+", newline='') as file:
            pass
        with open("data/Score_Individual.csv", "a+", newline='') as file:
            pass
    
    team_reader = csv.reader(open("data/Teams.csv"))
    teamDic = {}
    for row in team_reader:
        teamDic[row[0]] = row[1:]
    
    score_reader = csv.reader(open("data/Score.csv"))
    scoreDic = {}
    for row in score_reader:
        scoreDic[row[0]] = row[1:]
    
    score_indivi_reader = csv.reader(open("data/Score_Individual.csv"))
    score_indivi_Dic = {}
    for row in score_indivi_reader:
        score_indivi_Dic[row[0]] = row[1:]

class csv_functions:
    def add_to_score_indivi_csv():
        with open('data/Score_Individual.csv', 'w', newline='') as file:
            writer = csv.writer(file)
            for key, values in start_f.score_indivi_Dic.items():
                new_row = [key]
                new_row.extend(values)
                writer.writerow(new_row)


    def add_to_score_csv():
        with open('data/Score.csv', 'w', newline='') as file:
            writer = csv.writer(file)
            for key, values in start_f.scoreDic.items():
                new_row = [key]
                new_row.extend(values)
                writer.writerow(new_row)
    
    
    def add_to_teams_csv():
        with open('data/Teams.csv', 'w', newline='') as file:
            writer = csv.writer(file)
            for key, values in start_f.teamDic.items():
                new_row = [key]
                new_row.extend(values)
                writer.writerow(new_row)

    def clear_csv():
        clr = open('data/Score_Individual.csv', 'w+')
        clr.close()
        clr = open('data/Score.csv', 'w+')
        clr.close()
        clr = open('data/Teams.csv', 'w+')
        clr.close()
        start_f.teamDic = {}
        start_f.scoreDic = {}
        start_f.score_indivi_Dic = {}
        
        os.system('cls')
        print(csv_clear_succesful)
        input(st_press_enter)
        menu_f.homescreen()
        
class add_functions:
    def add_team():
        os.system('cls')
        print(add_team_header)
        for key, values in start_f.teamDic.items():
            print(key)
        print(add_team_choice)
        team_name = input(st_input)
        if(team_name.isspace() or not team_name):  # if team_name is empty or doesn't exist
            os.system('cls')
            print(add_team_empty_input)
            input(st_press_enter)
            add_f.add_team()
        elif(len(team_name) > 18):  # if team_name length is longer than 18
            os.system('cls')
            print(add_team_too_long)
            input(st_press_enter)
            add_f.add_team()
        elif(team_name and  # if team_name exists and
           team_name not in start_f.teamDic and  # team_name is not in teamDic dictionary and
           team_name.lower() != "x" and  # team_name is not X or x and
           len(team_name) <= 18):  # team_name length is shorter than or equal to 18
            start_f.teamDic[team_name] = []
            start_f.scoreDic[team_name] = [0, 0, 0]
            save_f.data("teams")
            save_f.data("score")
            menu_f.homescreen()
        elif(team_name.lower() == "x"):  # if team_name input was X or x
            menu_f.homescreen()
        else:  # if team_name already exists
            os.system('cls')
            print(add_team_already_exist % (team_name))
            input(st_press_enter)
            add_f.add_team()

    def add_players():
        os.system('cls')
        print(add_team_header)
        for key, values in start_f.teamDic.items():
            print(key)
        print(add_team_exist_choice)
        team_name = input(st_input)
        if(team_name.isspace() or not team_name):
            os.system('cls')
            print(add_team_empty_input)
            input(st_press_enter)
            add_f.add_players()
        elif(len(team_name) > 18):
            os.system('cls')
            print(add_team_too_long)
            input(st_press_enter)
            add_f.add_players()
        elif(team_name and
             team_name in start_f.teamDic and
             team_name.lower() != "x" and
             len(team_name) <= 18):
            cancel_ask = False
            os.system('cls')
            while not cancel_ask:
                try:
                    player_amount = int(input(add_player_amount % (team_name)))
                    cancel_ask = True
                except ValueError:
                    os.system('cls')
                    print(st_invalid_input)
            count = 1
            while count <= player_amount:
                cancel_ask = False
                os.system('cls')
                while not cancel_ask:
                    print(add_player_name % (count))
                    player = input(st_input)
                    if(player not in start_f.teamDic[team_name]):
                        start_f.teamDic[team_name].append(player)
                        start_f.score_indivi_Dic.update({player:[0]})
                        count += 1
                        cancel_ask = True
                    else:
                        os.system('cls')
                        print(add_player_already_in_team % (player, team_name))
            save_f.data("teams")
            save_f.data("score_indivi")
            input(st_press_enter)
            menu_f.homescreen()
        elif(team_name.lower() == "x"):
            menu_f.homescreen()
        else:
            os.system('cls')
            print(add_team_not_exist % (team_name))
            input(st_press_enter)
            add_f.add_players()


    def add_points():
        os.system('cls')
        print(add_team_header)
        for key, values in start_f.teamDic.items():
            print(add_has_points % (key, start_f.scoreDic[key][2]))
        print(add_team_exist_choice)
        team_name = input(st_input)
        if(team_name.isspace() or not team_name):
            os.system('cls')
            print(add_team_empty_input)
            input(st_press_enter)
            add_f.add_points()
        elif(len(team_name) > 18):
            os.system('cls')
            print(add_team_too_long)
            input(st_press_enter)
            add_f.add_players()
        elif(team_name and
             team_name in start_f.scoreDic and
             team_name.lower() != "x" and
             len(team_name) <= 18):
            cancel_ask = False
            os.system('cls')
            while not cancel_ask:
                try:
                    point_check = input(add_point_menu).lower()
                    if(point_check.isspace() or not point_check):
                        os.system('cls')
                        print(st_invalid_input)
                    elif(point_check in "s"):
                        get_value = 0
                        point_check_string = add_speed
                        cancel_ask = True
                    elif(point_check in "e"):
                        get_value = 1
                        point_check_string = add_effectivity
                        cancel_ask = True
                    else:
                        os.system('cls')
                        print(st_invalid_input)
                except ValueError:
                    os.system('cls')
                    print(st_invalid_input)
            os.system('cls')
            cancel_ask = False
            while not cancel_ask:
                try:
                    score = int(input(add_point_amount % (point_check_string)))
                    cancel_ask = True
                except ValueError:
                    os.system('cls')
                    print(st_invalid_input)
            start_f.scoreDic[team_name][get_value] = int(start_f.scoreDic[team_name][get_value]) + score
            start_f.scoreDic[team_name][2] = int(start_f.scoreDic[team_name][0]) + int(start_f.scoreDic[team_name][1])
            save_f.data("score")
            add_f.add_indivi_points()
            save_f.data("score_indivi")
            menu_f.homescreen()
        elif(team_name.lower() == "x"):
            menu_f.homescreen()
        else:
            os.system('cls')
            print(add_team_not_exist % (team_name))
            input(st_press_enter)
            add_f.add_points()

    def add_indivi_points():
        player_list = []
        for key, value in start_f.teamDic.items():
            for field in value:
                while field not in player_list:
                    player_list.append(field)
        count = 0
        while count < len(player_list):
            start_f.score_indivi_Dic[player_list[count]][0] = int(0)
            count += 1

        count = 0
        while count < len(player_list):
            for key, value in start_f.teamDic.items():
                if player_list[count] in value:
                    score = int(start_f.scoreDic[key][2])
                    start_f.score_indivi_Dic[player_list[count]][0] = int(start_f.score_indivi_Dic[player_list[count]][0]) + int(score)
                else:
                    pass
            count += 1

class save_functions:
    def data(type):
        if(type == "teams"):
            csv_f.add_to_teams_csv()
        elif(type == "score"):
            csv_f.add_to_score_csv()
        elif(type == "score_indivi"):
            csv_f.add_to_score_indivi_csv()
        elif(type == "all"):
            csv_f.add_to_teams_csv()
            csv_f.add_to_score_csv()
            csv_f.add_to_score_indivi_csv()
        else:
            print("fout")

class menu_functions:
    def homescreen():
        os.system('cls')
        print(st_welcome, menu)
        homescreen_choice = input(menu_choice)
        menu_f.choice_check(homescreen_choice)
        return

    def choice_check(homescreen_choice):
        choiceMade = False
        while not choiceMade:
            if homescreen_choice in ["1", "2", "3", "4", "5", "6"]:
                if homescreen_choice in "1":
                    add_f.add_team()
                elif homescreen_choice in "2":
                    add_f.add_players()
                elif homescreen_choice in "3":
                    menu_f.show_leaderboard()
                elif homescreen_choice in "4":
                    add_f.add_points()
                elif homescreen_choice in "5":
                    clear_choice = input(menu_clear_choice).lower()
                    while clear_choice not in ["y", "n"]:
                        print(st_invalid_input)
                        clear_choice = input(menu_clear_choice).lower()
                    if clear_choice in "y":
                        csv_f.clear_csv()
                        menu_f.homescreen()
                    elif clear_choice in "n":
                        menu_f.homescreen()
                elif homescreen_choice in "6":
                    exit_choice = input(menu_exit_choice).lower()
                    while exit_choice not in ["y", "n"]:
                        print(st_invalid_input)
                        exit_choice = input(menu_exit_choice).lower()
                    if exit_choice in "y":
                        os.system('cls')
                        save_f.data("all")
                        print(csv_save)
                        sys.exit(0)
                    elif exit_choice in "n":
                        menu_f.homescreen()
            else:
                print(st_invalid_input)
                homescreen_choice = input(menu_choice)

    def show_leaderboard():
        os.system('cls')

        # table
        print(show_table_header_teamname, " "*18, end="")
        print(show_table_header_total_points, " "*10, end="")
        print(show_table_header_team_members)

        for key, values in start_f.teamDic.items():
            multiple_members = False
            print(key, " "*(26-len(key)), start_f.scoreDic[key][2], end = " ")
            points_string = str(start_f.scoreDic[key][2])
            for i in range(len(start_f.teamDic[key])):
                if(not multiple_members and i < len(start_f.teamDic[key])-1):
                    print(" "*(15-len(points_string)), start_f.teamDic[key][i])
                    multiple_members = True
                else:
                    if(multiple_members):
                        addition = 0
                        if(len(points_string) == 1):
                            addition = 2
                        elif(len(points_string) == 2):
                            addition = 1
                        elif(len(points_string) == 3):
                            addition = 0
                        elif(len(points_string) == 4):
                            addition = -1
                        elif(len(points_string) == 5):
                            addition = -2
                        elif(len(points_string) == 6):
                            addition = -3
                        elif(len(points_string) == 7):
                            addition = -4
                        elif(len(points_string) == 8):
                            addition = -5
                        elif(len(points_string) == 9):
                            addition = -6
                        elif(len(points_string) == 10):
                            addition = -7
                        print(" "*(41+len(points_string)+addition), start_f.teamDic[key][i])
                    else:
                        print(" "*(15-len(points_string)), start_f.teamDic[key][i])

        table_choice = input(show_invidi_points)
        if(table_choice and table_choice.lower() in "x"):
            menu_f.homescreen()
        else:
            os.system('cls')
            print(show_table_header_teamname, " "*18, end="")
            print(show_table_header_indivi_points, " "*10, end="")
            print(show_table_header_team_members)

            for key, values in start_f.teamDic.items():
                multiple_members = False
                print(key, " "*(26-len(key)), end = " ")
                points_string = str(start_f.score_indivi_Dic[start_f.teamDic[key][0]])
                points_string = points_string.strip("[']")
                for i in range(len(start_f.teamDic[key])):
                    if(not multiple_members and i < len(start_f.teamDic[key])-1):
                        points_string_print = str(start_f.score_indivi_Dic[start_f.teamDic[key][i]])
                        points_string_print = points_string_print.strip("[']")
                        print(points_string_print, " "*(25-len(points_string)), start_f.teamDic[key][i])
                        multiple_members = True
                    else:
                        if(multiple_members):
                            points_string_print = str(start_f.score_indivi_Dic[start_f.teamDic[key][i]])
                            points_string_print = points_string_print.strip("[']")
                            addition = 0
                            if(len(points_string_print) == 1):
                                addition = 2
                            elif(len(points_string_print) == 2):
                                addition = 1
                            elif(len(points_string_print) == 3):
                                addition = -3
                            elif(len(points_string_print) == 4):
                                addition = -4
                            elif(len(points_string_print) == 5):
                                addition = 0
                            elif(len(points_string_print) == 6):
                                addition = 0
                            elif(len(points_string_print) == 7):
                                addition = 0
                            elif(len(points_string_print) == 8):
                                addition = 0
                            elif(len(points_string_print) == 9):
                                addition = 0
                            elif(len(points_string_print) == 10):
                                addition = 0
                            points_string_print = str(start_f.score_indivi_Dic[start_f.teamDic[key][i]])
                            points_string_print = points_string_print.strip("[']")
                            print(" "*27, points_string_print, " "*(21+len(points_string)+addition), start_f.teamDic[key][i])
                        else:
                            points_string_print = str(start_f.score_indivi_Dic[start_f.teamDic[key][i]])
                            points_string_print = points_string_print.strip("[']")
                            print(points_string_print, " "*(25-len(points_string)), start_f.teamDic[key][i])
            
            #for key, values in start_f.score_indivi_Dic.items():
            #    print(show_has_points_indivi % (key, start_f.score_indivi_Dic[key][0]))

        input(st_press_enter)
        menu_f.homescreen()

csv_f = csv_functions
add_f = add_functions
start_f = start_functions
save_f = save_functions
menu_f = menu_functions
