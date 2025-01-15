
import turtle

def draw_recursive_tree(t, branch_len, left_ang, right_ang, depth, len_reduce,):
    if depth > 0:
        t.forward(branch_len)  # Draws the current branch
        t.left(left_ang)  # Sets the left angle of the branch
        draw_recursive_tree(t, branch_len * len_reduce, left_ang, right_ang, depth - 1, len_reduce,) #Draws the left subtree
        t.right(left_ang + right_ang) #Takes you back to the original position
        draw_recursive_tree(t, branch_len * len_reduce, left_ang, right_ang, depth - 1, len_reduce,) #Draws the right subtree
        t.left(right_ang) #Takes you back to the original position
        t.backward(branch_len) # Brings you back to the original orientation

def user_input():
   while True:
        try:
            left_ang = float(input("Enter left branch angle (0-45): ")) # Maximum of 45 degrees ensures that the tree is more asthetically pleasing
            if not (0 <= left_ang <= 45):
                raise ValueError("Left branch angle must be between 0 and 45 degrees.")
            
            right_ang = float(input("Enter right branch angle (0-45): "))# Maximum of 45 degrees ensures that the tree is more asthetically pleasing
            if not (0 <= right_ang <= 45):
                raise ValueError("Right branch angle must be between 0 and 45 degrees.")
            
            branch_len = float(input("Enter starting branch length (pixels, 50-200): "))
            if not (50 <= branch_len <= 200):
                raise ValueError("Branch length must be between 50 and 200 pixels.")
            
            depth = int(input("Enter recursion depth (1-8)ie.The amount of times you would like the tree to branch out after the last drawn branch: "))
            if not (1 <= depth <= 8):
                raise ValueError("Recursion depth must be between 1 and 8:")
            
            len_reduce = float(input("Enter branch length reduction factor (A percentage between 0-1, ie .7): "))
            if not (0 < len_reduce < 1):
                raise ValueError("Branch length reduction factor must be between 0 and 1 (exclusive).")
    
            trunk_colour = input("Enter the colour of the trunk: ").strip()
            branch_colour = input("Enter the colour of the branches: ").strip()
            return left_ang, right_ang, branch_len, depth, len_reduce, trunk_colour, branch_colour
        
        except ValueError as e:# e = error message
            print(e) 

def main():
    left_ang, right_ang, branch_len, depth, len_reduce, trunk_colour, branch_colour = user_input()

        
    screen = turtle.Screen()# Sets up the turtle screen
    screen.setup(800, 600)
    screen.bgcolor("white")

    t = turtle.Turtle()
    t.speed(1) # Sets drawing speed
    t.width(6) # Sets the initial width of the pen

    t.color(trunk_colour) #Colour of the trunk
    t.left(90) #Rotates the pointer upwards
    t.up() # Instructs turtle to lift up the pen
    t.backward(200) # Instructs turtle to start 200 pixels from the middle of the screen
    t.down() # Brings pen back down to page
    t.forward(branch_len) # Draw the trunk

    t.color(branch_colour) # Set the color of the branches
    draw_recursive_tree(t, branch_len * len_reduce, left_ang, right_ang, depth - 1, len_reduce,)

    t.hideturtle()
    screen.mainloop()

if __name__ == "__main__":
    main()
