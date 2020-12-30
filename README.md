# Gmod Thruster Calculator


### Short Description:

This Python 3 script is designed to ease the calculation and utilization of a formula that I devised. This formula can be used to calculate the near exact amount of force needed, from certain thrusters, to counter the gravitational pull on an object. In other words, it allows you to calculate the amount of force needed to create near perfect "passive lift."

Sadly, due to the fact that every thruster in the game seems to react differently to the same amount of set force, the script cannot calculate the needed force for every thruster variant (yet). Therefore, when using the script, you must choose the thruster variant you desire to work with in order for the correct formula variant to be used. The base structure of the formula is the same for each thruster variant, but certain values must change to accomodate the different behaviors. 


### How to use:

The script works in a sort of "command line" manner in the hopes of making it easier to use, and also becuase it seems like a reasonable system to use to allow for many selections in a manner that is easy to handle and expand upon in the future. 

When opened/ran, you are greeted with a welcome message and another message that lists all the commands and choices for each supported thruster:

>) Thruster options: enter the respective thruster number to select a thruster<br>
>\- Thruster: projector            -> 1<br>
>\- Thruster: Afterburner1large    -> 2<br>
>\- Thruster: dav0r/thruster.mdl   -> 3<br>
>
>) Commands:<br>
>\- quit: Exits the program.<br>
>\- help: Displays this message again.<br>
>
>) Enter thruster number or a command:<br>
>)>

You can then enter in the respective number to choose a specific thruster variant or a command. Entering the 'quit' command exits and stops the program. Entering the 'help' command displays the message again. If you choose a thruster, you then move to another selection: 

>) Enter [1] if thruster(s) have no-gravity, or [0] if not.<br>
>)>

You must enter '1' if the thruster(s) you are going to be using to create this desired effect have "no gravity" or are not affected by gravity. Or, you must enter '0' if the thrusters are affected by gravity. Once you make your choice, the next section is displayed:

>) Enter total weight load (does not include the lift thruster(s) weight).<br>
>)> 

Here you must enter the total weight of the object that you are trying to "lift." This total weight must **NOT** include the weight of the thruster(s) and any objects that are not affected by gravity, as to not interfere with the design of the formula and the choices made thus far. Once this is done, the final section is displayed:

>) Total thrust needed: 

This displays the resulting amount of force needed to achieve the desired effect. Once this is done, it simply loops back around to the initial selection and you can repeat this process as many times as you desire until you exit and close the program by entering the 'quit' command. 


### Extra Info and Notes

If you would like to read more about the program and more about the actual formula itself, along with how certain things work related to that, the information will be in another file you can read named "extra_info."
