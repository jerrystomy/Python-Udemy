import turtle as tt
import random

tim = tt.Turtle()
tt.colormode(255)
# colors = ["DeepSkyBlue", "wheat"]
# directions = [0, 90, 180, 270]
tim.speed("fastest")
# tim.pensize(20)

def random_colors():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    random_color = (r, g, b)
    return random_color


def draw_spirograph(size_of_gap):
    for _ in range(int(360 / size_of_gap)):
        tim.color(random_colors())
        tim.circle(100)
        tim.setheading(tim.heading() + size_of_gap)


draw_spirograph(5)




# def random_walk():
#     for _ in range(200):
#         tim.color(random_colors())
#         tim.forward(40)
#         tim.setheading(random.choice(directions))

# def draw_shapes(No_of_sides):
#     angle = 360 / No_of_sides
#     for _ in range(No_of_sides):
#         tim.forward(100)
#         tim.right(angle)
# random_walk()


screen = tt.Screen()
tt.exitonclick()