import sys
sys.path.insert(0, 'imports/functions')
from functions import *

csv_f = csv_functions
add_f = add_functions
start_f = start_functions
save_f = save_functions
menu_f = menu_functions


os.system('color 3f')
start_f()
menu_f.homescreen()
