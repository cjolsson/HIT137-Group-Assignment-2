
import turtle

def draw_recursive_tree(t, branch_len, left_ang, right_ang, depth, len_reduce):
    if depth > 0:
        t.forward(branch_len)  # Draws the current branch
        t.left(left_ang)  # Sets the left angle of the branch
        draw_recursive_tree(t, branch_len * len_reduce, left_ang, right_ang, depth - 1, len_reduce) #Draws the left subtree
        t.right(left_ang + right_ang) #Takes you back to the original position
        draw_recursive_tree(t, branch_len * len_reduce, left_ang, right_ang, depth - 1, len_reduce) #Draws the right subtree
        t.left(right_ang) #Takes you back to the original position
        t.backward(branch_len) # Brings you back to the original orientation

def user_input():
    left_ang = float(input("Enter left branch angle: "))
    right_ang = float(input("Enter right branch angle: "))
    branch_len = float(input("Enter starting branch length (pixels): "))
    depth = int(input("Enter recursion depth ie. The amount of times you would like the tree to branch out after the last drawn branch: "))
    len_reduce =   float(input("Enter branch length reduction factor (A percentage between 0-1): "))     
    return left_ang, right_ang, branch_len, depth, len_reduce

def main():
    left_ang, right_ang, branch_len, depth, len_reduce = user_input()

    # Sets up the turtle screen
    screen = turtle.Screen()
    screen.setup(800, 600)
    screen.bgcolor("white")

    t = turtle.Turtle()
    t.speed(20) # Sets drawing speed
    t.color("brown") #Colour of the tree
    t.left(90) #Sets the pointer upwards
    t.up() # Instructs turtle to draw up
    t.backward(200) # Instructs turtle to start 200 pixels from the middle of the screen
    t.down() # Brings pointer back down

    draw_recursive_tree(t, branch_len * len_reduce, left_ang, right_ang, depth - 1, len_reduce)

    t.hideturtle()
    screen.mainloop()

if __name__ == "__main__":
    main()
