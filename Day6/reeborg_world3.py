"""
To be able to run this program we need to go to this site and capy-paste the code
https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Hurdle%204&url=worlds%2Ftutorial_en%2Fhurdle4.json
"""


def turn_right():
    turn_left()
    turn_left()
    turn_left()

while not at_goal():
    if wall_on_right() and front_is_clear():
        move()
    elif wall_on_right() and not front_is_clear():
        turn_left()
    elif not wall_on_right():
        turn_right()
        move()