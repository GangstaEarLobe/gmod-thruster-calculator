#!/usr/bin/python3

# This calculator helps the user in finding the total amount of thrust needed to achieve "passive lift" based on the weight load and the specific thruster(s) being used

# This function gets the user's input and handles any errors as a result of the input values, string version
def str_input(prompt, error_msg = ") Incorrect input, please try again."):

    # Init fail counter sentinel
    fails = 0

    # Check if user has made too many fails
    while fails < 3:
        # Try converting the input into a string
        try:
            return str(input(prompt))

        except ValueError:
            print(error_msg)

            fails += 1

    # If too many fails have been made, send them back and return an empty string
    return ""


# This function gets the user's input and handles any errors as a result of the input values
def load_input(prompt, error_msg = "\n) Incorrect input, please try again." ):
    # Init fail counter sentinel
    fails = 0

    #Try converting the input into a float
    while fails < 3:
        try:
            return float(input(prompt))

        except ValueError:
            print(error_msg)

            fails += 1

    # If too many fails have been made, send them back and return an empty string
    return ""


# Thruster varaints calculation values. Lists are parallel and the same index is used for both so that both values are used for the same thruster
# Base force needed for each unit
thrusters_base_lift = [6.576, 2.599, 19.478]

# Added force needed if affected by gravity
thrusters_added_gravity = [230.134, 90.901, 681.752]

# This function handles the input and calculation for the force
def thruster_calc(thruster_num):

    # Init fail counter sentinel 
    fails = 0

    # Check if user has made too many fails
    while fails < 3:

        # Get decision value
        no_grav = str_input("\n) Enter [Y/N] if thruster(s) have no-gravity or not.\n)> ")

        # Get total weight load
        load = load_input("\n) Enter total weight load (does not include the lift thruster(s) weight).\n)> ")

        # If user made too many fails, return the user to initial selection to prevent an error
        if load == "":

            return

        # If thruster(s) have no-gravity, use appropiate formula
        if str.lower(no_grav) == "y":
            needed_force = thrusters_base_lift[thruster_num-1] * ( load / 10 )

            print("\n) Total thrust needed: {:.3f}".format(needed_force))

            return

        # If thruster(s) have gravity, use appropiate formula
        elif str.lower(no_grav) == "n":
            needed_force = thrusters_added_gravity[thruster_num-1] + ( thrusters_base_lift[thruster_num-1] * ( load / 10 ) )

            print("\n) Total thrust needed: {:.3f}".format(needed_force))

            return

        # If user has failed the input, increment fail counter
        else:
            print("\n) Unknown input, please try again.")

            fails += 1

    # Reaches fail counter "cut-off" to prevent the user from being stuck in a fail-loop and sends them back to the "main menu"
    print("\n) Too many failed inputs, returning to initial selection.")

    return


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


while proceed:
    # Get user input
    usr_in = str_input("\n) Enter thruster number or a command:\n)> ")

    if str.lower(usr_in) == "quit":
        proceed = False

 
    elif str.lower(usr_in) == "help":
        help_info()

    elif str.isnumeric(usr_in):
        # Check if user entered a valid thruster choice 1-3
        if int(usr_in) > 0 and int(usr_in) < 4:
            thruster_calc(int(usr_in))

        else:
            print("\n) Unknown thruster number.")

    else:
        print("\n) Unknown command.")

# Exit Message
print("\n--Program Exited--\n")
