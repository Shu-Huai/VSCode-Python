from swampy.TurtleWorld import *


def koch(t: Turtle, order, size):
    if order == 0:
        t.fd(size)
    else:
        koch(t, order - 1, size / 3)
        t.rt(85)
        koch(t, order - 1, size / 3)
        t.lt(170)
        koch(t, order - 1, size / 3)
        t.rt(85)
        koch(t, order - 1, size / 3)


world = TurtleWorld()
bob = Turtle()
bob.delay = 0
bob.x = 0
bob.y = 160
bob.redraw()
bob.rt(36)
for i in range(5):
    koch(bob, 5, 1000)
    bob.rt(72)
bob.y = -10
bob.heading = 90
bob.redraw()
world.mainloop()