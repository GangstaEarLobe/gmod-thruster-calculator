#!/usr/bin/python3

# This calculator helps the user in finding the total amount of thrust needed to achieve "passive lift" based on the weight load and the specific thruster(s) being used

import Thrusters as th

# This function gets the user's input and handles any errors as a result of the input values, string version
def str_input(prompt, error_msg = ") Incorrect input, please try again."):
    while True:
        # Try converting the input into a string
        try:
            return str(input(prompt))

        except ValueError:
            print(error_msg)


# This function displays the "help" information
def help_info():
    print("""
) Thruster options: enter the respective thruster number to select a thruster
- Thruster: projector            -> 1
- Thruster: Afterburner1large    -> 2
- Thruster: dav0r/thruster.mdl   -> 3
    
) Commands:
- quit: Exits the program.
- help: Displays this message again.""")

# Display intro msg
print("""
--------------------------------------------------------------------------
---------------ShyAdvocate's Passive Lift Calculator v0.0.1---------------
--------------------------------------------------------------------------""")

# Display help information
help_info()

# Init sentinel value
proceed = True

# Begin selection loop if proceed is True
while proceed:
    usr_in = str_input("\n) Enter thruster number or a command:\n)> ")

    if str.lower(usr_in) == "quit":
        proceed = False

    elif str.lower(usr_in) == "help":
        help_info()

    elif str.isnumeric(usr_in):
        if int(usr_in) == 1:
            th.thruster_1()

        elif int(usr_in) == 2:
            th.thruster_2()

        elif int(usr_in) == 3:
            th.thruster_3()

        else:
            print("\n) Unknown thruster number.")

    else:
        print("\n) Unknown command.")

print("\n--Program Exited--\n")
