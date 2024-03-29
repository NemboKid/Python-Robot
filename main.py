import robot
import inventory
import quote

robotino_image = r"""

                   /~@@~\,
 _______ . _\_\___/\ __ /\___|_|_ . _______
/ ____  |=|      \  <_+>  /      |=|  ____ \
~|    |\|=|======\\______//======|=|/|    |~
 |_   |    \      |      |      /    |    |
  \==-|     \     |  2D  |     /     |----|~~)
  |   |      |    |      |    |      |____/~/
  |   |       \____\____/____/      /    / /
  |   |         {----------}       /____/ /
  |___|        /~~~~~~~~~~~~\     |_/~|_|/
   \_/        [/~~~~~||~~~~~\]     /__|\
   | |         |    ||||    |     (/|[[\)
   [_]        |     |  |     |
              |_____|  |_____|
              (_____)  (_____)
              |     |  |     |
              |     |  |     |
              |/~~~\|  |/~~~\|
              /|___|\  /|___|\
             <_______><_______>
"""

"""
It's an eternal loop, until q (exit) is pressed.
"""

while True:
    print(chr(27) + "[2J" + chr(27) + "[;H")
    print(robotino_image)
    print("Hi, my name is Robotino. I know it all. What can I do you for?")

    marvin.menu()
    choice = input("--> ")
    
    make_lower = choice.lower()

    if choice == "q" or choice == "Q":
        print("Bye, bye - and welcome back anytime!")
        break

    elif choice == "2":
        marvin.celcius_convert()

    elif choice == "3":
        marvin.word_multiplicator()

    elif choice == "4":
        marvin.sum_and_mean()

    elif choice == "5":
        marvin.which_is_bigger()

    elif choice == "6":
        marvin.prolong_word()

    elif choice == "7":
        marvin.isogram_checker()

    elif choice == "8":
        marvin.word_shaker()

    elif choice == "9":
        marvin.anagram()

    elif choice == "10":
        marvin.acronym()

    elif choice == "11":
        marvin.censur()

    elif choice == "inv":
        print(inventory.read_inv())

    elif "pick" in choice:
        add_item = choice[9:]
        inventory.write_to_file(add_item, "a")

    elif "drop" in choice:
        if choice[:10:-1] != inventory.read_inv():
            drop_item = choice[9:]
            inventory.replace_content(drop_item)
            print(inventory.read_inv())
            
    elif "citat" in make_lower:
        print(quote.read_citation())

    elif "lunch" in make_lower:
        print(quote.read_lunch())

    elif "hej" in make_lower:
        print(quote.read_hej())

    elif "mat" in make_lower or "käk" in make_lower:
        print(quote.read_mat())

    else:
        print("That is not a valid choice. You can only choose from the menu.")

    input("\nPress enter to continue...")
