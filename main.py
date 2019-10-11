"""
Marvin with a simple menu to start up with.
Marvin doesnt do anything, just presents a menu with some choices.
You should add functinoality to Marvin.
"""
import marvin
import inventory

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
Its an eternal loop, until q is pressed.
It should check the choice done by the user and call a appropriate
function.
"""

while True:
    print(chr(27) + "[2J" + chr(27) + "[;H")
    print(robotino_image)
    print("Hi, my name is Robotino. I know it all. What can I do you for?")


    marvin.menu()
    choice = input("--> ")


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



    else:
        print("That is not a valid choice. You can only choose from the menu.")

    input("\nPress enter to continue...")
