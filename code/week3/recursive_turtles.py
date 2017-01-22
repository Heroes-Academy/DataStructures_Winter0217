import turtle

def getbob():
    bob = turtle.Turtle()
    bob.left(90)
    bob.speed('fastest')
    jump(bob, 0,0)
    return bob

def jump(t, x, y):
    t.penup()
    t.setpos(x,y)
    t.pendown()

def sierpinski(t, length, depth, first=True):
    if first:
        t.setheading(0)


    t.color('black', 'black')
    t.begin_fill()
    for _ in range(3):
        t.forward(length)
        t.left(120)

        if depth > 0:
            sierpinski(t, length/2, depth-1, False)
    t.end_fill()

#

def tree(t, length, branch_num, depth, width=90.0, ratio=2/3.):

    # make the pen size bigger if near top of the tree
    t.pensize(depth+1)
    # go forward for the trunk
    t.forward(length)
    # if not at the base case
    if depth > 0:
        # turn left half of the width
        t.left(width/2)

        # for each branch, make a subtree
        for x in range(branch_num-1):

            # the subtree!
            #        new_length             new_depth
            tree(t, length*ratio, branch_num, depth-1, width, ratio)

            # turn right to match the number of branches
            t.right(width/(branch_num-1))

        # do one final tree because the pattern was supposed to be
        # left, subtree, right, subtree, right, subtree, left
        # for 3 branches
        tree(t, length*ratio, branch_num, depth-1, width, ratio)

        t.left(width/2)

    # back up!
    t.backward(length)




def snowflake(t, n, d, mod=1):
    if d == 0:
        t.forward(n*mod)
    else:
        snowflake(t, n/3, d-1)
        t.left(60)
        snowflake(t, n/3, d-1)
        t.right(120)
        snowflake(t, n/3, d-1)
        t.left(60)
        snowflake(t, n/3, d-1)

def neat(bob):

    bob.setheading(0)
    bob.penup(); bob.setpos(-300,0); bob.pendown()
    bob.begin_fill()
    snowflake(bob, 700, 4)
    bob.setheading(180)
    snowflake(bob, 700, 4, -1)
    bob.end_fill()

    bob.color('black', 'purple')
    bob.setheading(0)
    bob.penup(); bob.setpos(-140,0); bob.pendown()
    bob.begin_fill()
    snowflake(bob, 375, 4)
    bob.setheading(180)
    snowflake(bob, 375, 4, -1)
    bob.end_fill()


    bob.color('black', 'blue')
    bob.setheading(0)
    bob.penup(); bob.setpos(-140*0.4666,0); bob.pendown()
    bob.begin_fill()
    snowflake(bob, 375*0.5357, 4)
    bob.setheading(180)
    snowflake(bob, 375*0.5357, 4, -1)
    bob.end_fill()
#

def circle(t, radius, depth, nb_segments):
    if depth > 0 and nb_segments > 0:
        for i in range(nb_segments):
            t.circle(radius, 360/nb_segments)
            t.left(180)
            circle(t, radius*0.4, depth-1, nb_segments)
            t.right(180)


def run_tree(t, length=200, branch=2, depth=9, angle=140, reduc=0.7):
    tree(t, length, branch, depth, angle, reduc)

bob = getbob()
#jump(bob, 200, 0)
#sierpinski(getbob(), 300, 7)
run_tree(bob)
#neat(bob)
#circle(bob, 100, 4, 6)
turtle.done()