
# Custom module contianing all available thruster passive_lift calculations.

# This function gets the user's input and handles any errors as a result of the input values
def num_input(prompt, type, error_msg = "\n) Incorrect input, please try again." ):

    # If specified -type- is "int" then convert the iput into an integer
    if type == "int":
        while True:
            try:
                return int(input(prompt))

            except ValueError:
                print(error_msg)

    # If specified -type- is "float" then convert the input into a float
    elif type == "float":
        while True:
            try:
                return float(input(prompt))

            except ValueError:
                print(error_msg)

    # If specified -type- is not "int" or "float" then notify user that wrong specfied -type- has been written
    else:
        print("- Unkown type specified.")


# This function calculates the needed thrust for "thruster# 1" or the "thruster_projector"
def thruster_1():

    # Init sentinel value for counting failed inputs so that the user is not stuck in the loop if making incorrect inputs
    fails = 0

    # Checks whether or not the user has made too many failed inputs
    while fails <= 2:

        # Get no-grav option value
        no_grav = num_input("\n) Enter [1] if thruster(s) have no-gravity, or [0] if not.\n)> ", "int")

        # Get total weight load
        load = num_input("\n) Enter total weight load (does not include the lift thruster(s) weight).\n)> ", "float")

        # Calculates needed thrust for thruster(s) with no gravity, note: all thrusters must be at a weight of 350
        if no_grav == 1:
            thrust = 6.576 * ( load / 10 )

            print("\n) Total thrust needed:", thrust)

            return

        # Calculates needed thrust for thruster(s) with gravity, note: all thrusters must be at a weight of 350
        elif no_grav == 0:
            thrust = 230.134 + ( 6.576 * ( load / 10 ) )

            print("\n) Total thrust needed:", thrust)

            return

        # Notify the user if they have entered the wrong no-grav option value, return to beginning of loop, and increment fail count
        else:
            print("\n) Unknown no-gravity option, please try again.")

            fails += 1

    print("\n) Returning to first selection, failed input too many times.")

    return


# This function calculates the needed thrust for "thruster# 1" or the "thruster_Afterburner1large"
def thruster_2():

    # Init sentinel value for counting failed inputs so that the user is not stuck in the loop if making incorrect inputs
    fails = 0

    # Checks whether or not the user has made too many failed inputs
    while fails <= 2:

        # Get no-grav option value
        no_grav = num_input("\n) Enter [1] if thruster(s) have no-gravity, or [0] if not.\n)> ", "int")

        # Get total weight load
        load = num_input("\n) Enter total weight load (does not include the lift thruster(s) weight).\n)> ", "float")

        # Calculates needed thrust for thruster(s) with no gravity, note: all thrusters must be at a weight of 350
        if no_grav == 1:
            thrust = 2.599 * ( load / 10 )

            print("\n) Total thrust needed:", thrust)

            return

        # Calculates needed thrust for thruster(s) with gravity, note: all thrusters must be at a weight of 350
        elif no_grav == 0:
            thrust = 90.901 + ( 2.599 * ( load / 10 ) )

            print("\n) Total thrust needed:", thrust)

            return

        # Notify the user if they have entered the wrong no-grav option value, return to beginning of loop, and increment fail count
        else:
            print(") Unknown no-gravity option, please try again.")

            fails += 1

    print("\n) Returning to first selection, failed input too many times.")

    return


# This function calculates the needed thrust for "thruster# 1" or the "thruster_dav0r/thruster.mdl"
def thruster_3():

    # Init sentinel value for counting failed inputs so that the user is not stuck in the loop if making incorrect inputs
    fails = 0

    # Checks whether or not the user has made too many failed inputs
    while fails <= 2:

        # Get no-grav option value
        no_grav = num_input("\n) Enter [1] if thruster(s) have no-gravity, or [0] if not.\n)> ", "int")

        # Get total weight load
        load = num_input("\n) Enter total weight load (does not include the lift thruster(s) weight).\n)> ", "float")

        # Calculates needed thrust for thruster(s) with no gravity, note: all thrusters must be at a weight of 350
        if no_grav == 1:
            thrust = 19.478 * ( load / 10 )

            print(") Total thrust needed:", thrust)

            return

        # Calculates needed thrust for thruster(s) with gravity, note: all thrusters must be at a weight of 350
        elif no_grav == 0:
            thrust = 681.752 + ( 19.478 * ( load / 10 ) )

            print("\n) Total thrust needed:", thrust)

            return

        # Notify the user if they have entered the wrong no-grav option value, return to beginning of loop, and increment fail count
        else:
            print("\n) Unknown no-gravity option, please try again.")

            fails += 1

    print("\n) Returning to first selection, failed input too many times.")

    return
