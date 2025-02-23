import primer1_modul
import primer1_modul.showcase as showcase
from pathlib import Path
import primer1_modul.deletion as deletion
import primer1_modul.addition as addition

try:
    cars_path = Path(__file__).parent / "primer1_cars.json"
    primer1_modul.Configuration.set_initial_path(cars_path)
except FileNotFoundError as ex:
    print(ex)
    import sys
    sys.exit(1)


while True:
    print(""" --- Cars App--- 
[1] Show available cars
[2] Add a new car
[3] Delete a car
[4] Azurirajte postojeci automobil
[Q] Exit application""")
    choice = input("Your choice: ")
    if choice == "1":
        showcase.show_cars()
    elif choice == "2":
        addition.add_new_car()
    elif choice == "3":
        deletion.delete_a_car()
    elif choice == "4":
        pass
    elif choice.upper() == "Q":
        import sys
        sys.exit()