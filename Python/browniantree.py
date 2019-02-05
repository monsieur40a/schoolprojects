# Zachary Fortier fort0142

# I understand that this is a graded, individual examination that may not be
# discussed with anyone.  I also understand that obtaining solutions or
# partial solutions from outside sources, or discussing any aspect of the exam
# with anyone is aacademic misconduct and will result in failing the course.
# I further certify that this program represents my own work and that none of
# it was obtained from any source other than material presented as part of the
# course.


import turtle
import random
import math


def main():
    # Initializes turtle and screen attributes
    z, screen = graphicssetup()

    # Prompt user for max particle number in Brownian Tree
    max_particles = int(treesize(screen))

    # Inititializes nested grid list, variables, and seeds "tree"
    particlegrid, curr_particles, cl_radius = \
        seed_and_init_particle_grid(z)

    while curr_particles < max_particles:
        # Places new particle in random position from origin
        xpos, ypos = place_particle_rand(cl_radius)

        # Updates variables based on drunken particle walk results
        particlegrid, curr_particles, cl_radius = \
            drunkenparticle(z, particlegrid, xpos, ypos,
                            curr_particles, cl_radius)

    # Ends Brownian Tree Simulation
    z.goto(0, 180)
    z.color("white")
    z.write("Thanks for Watching! Click Screen to Exit!")
    screen.exitonclick()


def graphicssetup():
    # Instantiates and sets-up screen & turtle objects
    z = turtle.Turtle()
    screen = z.getscreen()

    screen.setworldcoordinates(0, 0, 199, 199)
    screen.colormode(255)
    screen.bgcolor("black")

    z.speed(0)
    z.hideturtle()
    z.penup()

    return z, screen


def treesize(screen):
    max_particles = screen.textinput("Brownian Tree", "How many particles?")

    return max_particles


def seed_and_init_particle_grid(z):
    particlegrid = []

    for row in range(200):
        particlegrid.append([])
        for column in range(200):
            particlegrid[row].append(False)

    particlegrid[100][100] = True
    curr_particles, cl_radius = 1, 0

    z.goto(100, 100)
    z.dot(6, (new_color(cl_radius)))

    return particlegrid, curr_particles, cl_radius


def place_particle_rand(cl_radius):
    # Rounds values to keep them within grid locations
    angle = random.randint(1, 360)
    xpos = 100 + round(math.cos(math.radians(angle)) * (cl_radius + 1))
    ypos = 100 + round(math.sin(math.radians(angle)) * (cl_radius + 1))

    return xpos, ypos


def inGrid(row, column):
    if row >= 0 and row <= 199 and column >= 0 and column <= 199:
        return True
    return False


def drunkenparticle(z, particlegrid, xpos, ypos, curr_particles, cl_radius):
	new_particle, prompt = False, True

	# Checks if current position has neighbor before init drunk "walk"
	if inGrid(xpos, ypos):
		if hasNeighbor(particlegrid, xpos, ypos):
			prompt = False
			new_particle = True
	if prompt:
		step = 0
		while step < 200 and prompt:
			heading = random.randint(1, 4)
			if heading == 1:
				xpos += 1
			elif heading == 2:
				ypos += 1
			elif heading == 3:
				xpos -= 1
			else:
				ypos -= 1

			if inGrid(xpos, ypos):
				if hasNeighbor(particlegrid, xpos, ypos):
					prompt = False
					new_particle = True
			step += 1
	if new_particle:
		# Checks if max radius needs to be updated
		cl_radius = new_radius(cl_radius, xpos, ypos)

		# Goes to new position, sends new radius to get new color
		z.goto(xpos, ypos)
		z.dot(6, (new_color(cl_radius)))
		particlegrid[xpos][ypos] = True

		curr_particles += 1

	return particlegrid, curr_particles, cl_radius


def hasNeighbor(grid, row, column):
    # Tests whether its a corner and then its three neighbors
    if (row, column) == (0, 0):
        if grid[row+1][column]\
                or grid[row+1][column+1]\
                or grid[row][column+1]:
            return True
    elif (row, column) == (0, 199):
        if grid[row+1][column]\
                or grid[row+1][column-1]\
                or grid[row][column-1]:
            return True
    elif (row, column) == (199, 0):
        if grid[row-1][column]\
                or grid[row-1][column+1]\
                or grid[row][column+1]:
            return True
    elif (row, column) == (199, 199):
        if grid[row-1][column]\
                or grid[row-1][column-1]\
                or grid[row][column-1]:
            return True
    # Tests whether its a border cell and its five neighbors
    elif column == 0 and row > 0 and row < 199:
        if grid[row+1][column]\
                or grid[row+1][column+1]\
                or grid[row][column+1]\
                or grid[row-1][column+1]\
                or grid[row-1][column]:
            return True
    elif column == 199 and row > 0 and row < 199:
        if grid[row+1][column]\
                or grid[row+1][column-1]\
                or grid[row][column-1]\
                or grid[row-1][column-1]\
                or grid[row-1][column]:
            return True
    elif row == 0 and column > 0 and column < 199:
        if grid[row][column-1]\
                or grid[row+1][column-1]\
                or grid[row+1][column]\
                or grid[row+1][column+1]\
                or grid[row][column+1]:
            return True
    elif row == 199 and column > 0 and column < 199:
        if grid[row][column-1]\
                or grid[row-1][column-1]\
                or grid[row-1][column]\
                or grid[row-1][column+1]\
                or grid[row][column+1]:
            return True
    # Tests an interior cell and its eight neighbors
    else:
        if grid[row+1][column-1]\
                or grid[row+1][column]\
                or grid[row+1][column+1]\
                or grid[row][column-1]\
                or grid[row][column+1]\
                or grid[row-1][column-1]\
                or grid[row-1][column]\
                or grid[row-1][column+1]:
            return True
    return False


def new_radius(cl_radius, x2, y2):
    # Determines radius: distance from new position to origin
    origin_x, origin_y = 100, 100
    radprev = cl_radius
    radcurr = int(math.sqrt((origin_x - x2)**2 + (origin_y - y2)**2))

    if radcurr >= radprev:
        return radcurr
    else:
        return radprev


def new_color(cl_radius):
    # Goes through shades of red, orange, yellow, green, blue, purple, pink
    if cl_radius in range(0, 5):
        r, g, b = 255, 0, 0
    elif cl_radius in range(5, 21):
        r, g, b = 255, int(cl_radius * (255/20)), 0
    elif cl_radius in range(21, 31):
        r, g, b = 255 - int(((cl_radius/10 - 2) * 200)), 255, 0
    elif cl_radius in range(31, 41):
        r, g, b = 0, 255, int((cl_radius//10) + ((cl_radius/10 - 3) * 251))
    elif cl_radius in range(41, 51):
        r, g, b = 0, 255 - int(((cl_radius/10 - 4) * 200)), 255
    elif cl_radius in range(51, 61):
        r, g, b = int((cl_radius//10) + ((cl_radius/10 - 5) * 249)), 0, 255
    elif cl_radius in range(61, 85):
        r, g, b = 255, 0, 255 - int(((cl_radius/10 - 6) * 99))
    else:
		# White
        r, g, b = 248, 248, 255

    return r, g, b


if __name__ == "__main__":
    main()
