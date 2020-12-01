from turtle import Turtle, Screen
import random

is_on= False
screen = Screen()
screen.setup(width=500, height=400)
user_guess = screen.textinput(title="Make your bet.", prompt="Which turtle win the race? Enter a color: ")
is_on=True
colors=["red", "orange", "yellow", "green", "blue", "purple"]
y=-125
turtles=[]


for i in range(0, 6):

    tim = Turtle(shape="turtle")
    tim.color(colors[i])
    tim.pu()
    tim.goto(-240, y)
    y += 50
    turtles.append(tim)
    x=0
while is_on:
    for turtle in turtles:
        nums=[0, 5, 10]
        random_num = random.choice(nums)
        turtle.forward(random_num)

        if turtle.xcor()>230:
            x += 1
            turtles.remove(turtle)
            if user_guess == turtle.pencolor() and len(turtles) == 5:
                print(f"You win... {x}. {turtle.pencolor()} turtle.")
                is_on=False
            elif user_guess == turtle.pencolor() and len(turtles) != 5:
                print(f" {x}. {turtle.pencolor()} turtle.")
                is_on=False
            elif user_guess != turtle.pencolor() and len(turtles) != 5:
                print(f" {x}. {turtle.pencolor()} turtle.")
            else:
                print(f"You lose. Winner is {turtle.pencolor()} turtle.")




screen.exitonclick()