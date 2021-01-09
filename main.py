import time  # Import time for sleep


def menu():
    print(
        """ ---Automated Investing---
    Choose one of the following option:
    s) Start
    q) Quit"""
    )
    choice = input("    Choice: ")
    if choice.lower() in ["s", "q"]:
        return choice.lower()
    else:
        print(choice + "? " + "That is an invalid option")


# executable for stand-alone program
if __name__ == "__main__":

    choice = menu()

    if choice == "s":
        print("loop")
        time.sleep(2.5)
    elif choice == "q":
        print("interrupted!")

    # try:
    #     while True:
    #         print("loop")
    #         time.sleep(2.5)
    # except KeyboardInterrupt:
    #     print('interrupted!')
