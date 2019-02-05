import turtle
import random
import time


def main():
    # Tests the final score function with sample score lists and results.
    finalscoretest()

    # Sets up the screen, turtle, and graphics from the turtle module.
    z, screen = screen_turtle_scoreboard_setup()

    # Initializes the bowling variables and pinlist to store pins hit.
    pinlist = []
    endgame = False
    frame, pinindex, throw = 0, 0, 0
    pins_remaining = 10

    while not endgame:
        # Resets the pin display at the end of each frame.
        # Returns pinlocation list to alter to keep track of pins "hit."
        pinlocation = pin_display(z)

        endframe = False
        while not endframe:
            # Marks and writes the current frame number to the scoreboard.
            mark_frame_number(z, frame, throw)

            # Prompts user for a # of pins hit.
            pins_hit = pins_hit_(pins_remaining, frame, screen)
            pinlist.append(pins_hit)

            # Knocks down pins by altering pinlist locations and updates list.
            pinlocation = pinknockdown(z, pins_hit, pinlocation)

            # Determines if strike or spare, calculates pins_remaining.
            strike, spare, pins_remaining = \
                spare_strike_pins_remain(pinlist, pins_hit, frame,
                                         throw, pins_remaining, pinindex)

            # Graphically displays throw and/or frame results to scoreboard.
            displayscore(z, pinlist,
                         strike, spare, frame, throw, pinindex)

            if frame != 9:
                # Checks if the frame is over and/or setup for the next throw.
                if throw == 1 or strike:
                    endframe = True
                    frame += 1
                    throw = 0
                    pinindex += 1
                else:
                    throw += 1
                    pinindex += 1
                time.sleep(2)
            else:
                # Checks if end of the last frame.
                # Checks if 1st and 2nd throw not spare/strike or 3rd throw.
                if (throw == 1 and not(spare or strike)
                        and pinlist[pinindex - 1] != 10) or throw == 2:
                    endframe = True
                    endgame = True
                else:
                    # Game not over if strike in 1st/2nd or spare in 2nd throw.
                    if strike or spare\
                            or (pinlist[pinindex - 1] + pinlist[pinindex] == 10)\
                            and throw != 0:
                        time.sleep(2)
                        pinlocation = pin_display(z)
                    throw += 1
                    pinindex += 1
    # Ends game with message and prompt to click screen to exit game.
    z.goto(450, 210)
    z.write("Game Over. Thanks for Playing! Click Screen to Exit.")
    screen.exitonclick()


def screen_turtle_scoreboard_setup():
    # Instantiates screen & turtle objects
    # Sets up screen dimensions and quicker animation.
    z = turtle.Turtle()
    screen = z.getscreen()
    screen.setworldcoordinates(0, 0, 1000, 1000)
    screen.tracer(2, 0)

    # Sets turtle shape and size, then hides it.
    z.shape("circle")
    z.turtlesize(3, 3, None)
    z.hideturtle()

    # Moves the turtle where the scoreboard will be drawn.
    z.penup()
    z.goto(0, 200)

    # Calls the scoreboard function to draw it to the screen.
    scoreboard(z)

    return z, screen


def scoreboard(z):
    # Draws the column headers on the scoreboard.
    for header in range(10):
        scoreboard_headers(z)

    # Left aligns the turtle back to the first column, below headers.
    z.goto(0, 175)

    # Draws bigsquares on the scoreboard.
    sidelength = 90
    for bigsquares in range(10):
        scoreboardsquares(z, sidelength)

    # Draws littlesquares on the scoreboard for frames 0-8.
    sidelength = 30
    z.goto(60, 175)
    for littlesquares in range(9):
        scoreboardsquares(z, sidelength)

    # Draws littlesquares on the scoreboard for frame 10.
    z.goto(810, 175)
    for threelittlesquares in range(3):
        scoreboardsquares(z, sidelength, 3)


def scoreboard_headers(z):
    # Gets the current turtle position coordinates to reference.
    start_x_pos = z.xcor()
    start_y_pos = z.ycor()

    # Draws a column header.
    drawrectangle(z, 90, 25)

    # Adjusts turtle position for a new column header to be drawn.
    z.penup()
    z.goto(start_x_pos + 90, start_y_pos)


def drawrectangle(z, xlength, ylength):
    z.pendown()
    z.goto(z.xcor(), z.ycor() - ylength)
    z.goto(z.xcor() + xlength, z.ycor())
    z.goto(z.xcor(), z.ycor() + ylength)
    z.goto(z.xcor() - xlength, z.ycor())


def scoreboardsquares(z, sidelength, offset=1):
    drawrectangle(z, sidelength, sidelength)
    z.penup()
    z.goto(z.xcor() + 90//offset, z.ycor())


def pin_display(z):
    # Goes to starting point where the pins will be displayed.
    z.penup()
    z.goto(450, 300)

    # Initializes new pinlocation list to keep track of pins up or knocked down.
    pinlocation = []

    # Stamps pins to the screen and puts pin location in list.
    for pin in range(10):
        if pin in range(0, 4):
            z.goto(z.xcor() + 50, z.ycor() + 90)
            z.stamp()
        if pin in range(4, 5):
            z.goto(z.xcor() - 100, z.ycor())
            z.stamp()
        if pin in range(5, 7):
            z.goto(z.xcor() - 50, z.ycor() - 90)
            z.stamp()
        if pin in range(7, 8):
            z.goto(z.xcor(), z.ycor() + 180)
            z.stamp()
        if pin in range(8, 9):
            z.goto(z.xcor() - 50, z.ycor() - 90)
            z.stamp()
        if pin in range(9, 10):
            z.goto(z.xcor() - 50, z.ycor() + 90)
            z.stamp()
        pinlocation.append(z.pos())

    return pinlocation


def mark_frame_number(z, frame, throw):
    z.goto(30, 190)

    # Marks dot on the screen and overwrites it if not the current frame.
    for frames in range(10):
        if frames == frame:
            z.pendown()
            z.dot(5, "black")
            z.penup()
        else:
            z.pendown()
            z.dot(5, "white")
            z.penup()
        z.goto(z.xcor() + 90, z.ycor())

    # Writes the frame on screen, only executes on first throw of that frame.
    z.goto(45, 180)
    for frames in range(10):
        if frames == frame and throw == 0:
            z.write("{}" .format(frame + 1), False, align="center")
        z.goto(z.xcor() + 90, z.ycor())


def pins_hit_(pins_remaining, frame, screen):
    # Prompts for pins hit. Returns it.
    # Generates random number from remaining pin if null string entered.
    # Uses current pins remaining if number >= entered.
    pins = screen.textinput("Are you ready to bowl!?\
                             Frame {}" .format(frame + 1),
                            "Enter of # pins you just took down.\
                             Hit enter (null string) for random.")
    if pins == '':
        pins_hit_ = random.randint(0, pins_remaining)
    elif int(pins) >= pins_remaining:
        pins_hit_ = pins_remaining
    else:
        pins_hit_ = int(pins)

    return pins_hit_


def pinknockdown(z, pins_hit, pinlocation):
    # If no pins hit, returns current list unaltered.
    if pins_hit == 0:
        return pinlocation

    # Puts number in pin location list if not "hit."
    # Marks pin location with white dot if chosen to be "hit."
    pin = 0
    while pin < pins_hit:
        pin_choice = random.randint(0, 9)
        if pinlocation[pin_choice] != "hit":
            z.goto(pinlocation[pin_choice])
            z.pendown()
            z.dot(55, "white")
            z.penup()
            pinlocation[pin_choice] = "hit"
            pin += 1
    return pinlocation


def spare_strike_pins_remain(pinlist, pins_hit, frame,
                             throw, pins_remaining, pinindex):
    # Resets spare and strike booleans from previous throws.
    spare, strike = False, False

    # Determines if strike or spare, calculates pins_remaining.
    if pins_hit == 10 and throw == 0:
        strike = True
    elif throw == 1\
            and pinlist[pinindex - 1] + pinlist[pinindex] == 10\
            and pinlist[pinindex - 1] != 10:
        spare = True
    elif throw == 2\
            and pinlist[pinindex - 1] + pinlist[pinindex] == 10\
            and pinlist[pinindex - 1] != 10\
            and pinlist[pinindex - 2] == 10:
        spare = True
    elif pins_hit == 10:
        strike = True

    if throw == 1 or spare or strike and frame != 9:
        pins_remaining = 10
    elif spare or strike:
        pins_remaining = 10
    else:
        pins_remaining = pins_remaining - pins_hit

    return strike, spare, pins_remaining


def displayscore(z, pinlist, strike, spare,
                 frame, throw, pinindex):
    # Reference location in the scoreboard: lower middle of large box.
    xcor5, ycor5 = 45, 85

    if strike or spare:
        Strike_Spare(z, frame, throw, strike)
    else:
        display_normal_throw(z, throw, frame, pinlist, pinindex)

    if frame == 9:
        # Displays final score in 10th frame if game over.
        # Checks if 1st and 2nd throw not spare/strike or 3rd throw.
        if (throw == 1 and not(spare or strike)
                and pinlist[pinindex - 1] != 10) or throw == 2:
            z.goto(xcor5 + (frame * 90), ycor5)
            z.write("{}" .format(finalScore(pinlist)))


def Strike_Spare(z, frame, throw, strike):
    # Reference location in the scoreboard: right below frames.
    xcor, ycor = 45, 45
    # Reference location in the scoreboard: bottom left corner of small box.
    xcor2, ycor2 = 60, 145

    if strike:
        text = "Strike!"
    else:
        text = "Spare!"

    if frame != 9:
        # Goes to relevant location and writes Spare/Strike.
        z.goto(xcor + (frame * 90), ycor)
        z.write("{}" .format(text), False, align="center")
        # Goes to relevant small box for frames 0-8.
        z.goto(xcor2 + (frame * 90), ycor2)
    else:
        # Goes to relevant location and writes Spare/Strike.
        z.goto(xcor + (frame * 90), ycor + (throw * -15))
        z.write("{}" .format(text), False, align="center")
        # Goes to relevant small box for frame 9; varies with throw.
        z.goto(xcor2 + (frame * 90) + (-60 + 30 * throw), ycor2)
    draw_Strike_Spare(z, strike)


def draw_Strike_Spare(z, strike):
    z.pendown()
    if strike:
        # Draws an X.
        z.goto(z.xcor() + 30, z.ycor() + 30)
        z.goto(z.xcor(), z.ycor() - 30)
        z.goto(z.xcor() - 30, z.ycor() + 30)
    else:
        # Draws a /.
        z.goto(z.xcor() + 30, z.ycor() + 30)
    z.penup()


def display_normal_throw(z, throw, frame, pinlist, pinindex):
    # Reference location in the scoreboard: right below frames.
    xcor, ycor = 45, 45
    # Reference location in the scoreboard: left of small box.
    xcor3, ycor3 = 40, 145
    # Reference location in the scoreboard: middle of small box.
    xcor4, ycor4 = 75, 145

    if frame != 9:
        if throw == 0:
            # Displays pins hit in area before small box; varies with frame.
            z.goto(xcor3 + (frame * 90), ycor3)
        else:
            # Writes "Open Frame"; varies with frame.
            z.goto(xcor + (frame * 90), ycor)
            z.write("Open Frame", False, align="center")
            # Display pins hit in small box; varies with frame.
            z.goto(xcor4 + (frame * 90), ycor4)
    else:
        if throw == 1:
            # Current throw not strike or spare, previous throw wasn't a strike.
            if pinlist[pinindex - 1] != 10:
                # Writes "Open Frame"; varies with frame.
                z.goto(xcor + (frame * 90), ycor + (throw * -15))
                z.write("Open Frame", False, align="center")

        # Display pins hit in small box; varies with frame and throw.
        z.goto(xcor4 + (frame * 90) - 60 + (throw * 30), ycor4)

    if pinlist[pinindex] == 0:
        z.write("-")
    else:
        z.write("{}" .format(pinlist[pinindex]))


def finalScore(pinlist):
    index, score, frame = 0, 0, 0
    while frame != 10:
        # The current frame is a strike.
        if pinlist[index] == 10:
            if not index + 1 > len(pinlist) - 1\
                    and not index + 2 > len(pinlist) - 1:
                score += pinlist[index] + pinlist[index+1] + pinlist[index+2]
                index += 1
        # The current frame is a spare.
        elif pinlist[index] + pinlist[index+1] == 10:
            if not index + 1 > len(pinlist) - 1:
                score += pinlist[index] + pinlist[index+1] + pinlist[index+2]
                index += 2
        else:
            score += pinlist[index] + pinlist[index+1]
            index += 2
        frame += 1

    return score


def finalscoretest():
    pinlists = [[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                [0,0,10,1,2,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                [0,0,2,8,9,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,10,10,10],
                [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2,8,10],
                [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2,7],
                [10,9,1,5,5,7,2,10,10,10,9,0,8,2,9,1,10],
                [10,10,10,10,10,10,10,10,10,10,10,10]]

    results = [0,16,28,30,20,9,187,300]

    for result in range(len(results)):
        assert(finalScore(pinlists[result]) == results[result])


if __name__ == '__main__':
    main()
