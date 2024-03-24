from turtle import Turtle, Screen
is_race_on = False
import random
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="which turtle will win the race? Entter the colour: ")
colors = ["Red", "blue", "yellow", "orange", "black", "purple"]
y_positions = [-70, -40, -10, 20, 50, 80]

all_turtle = []


for Tats_index in range(0, 6):
    Tats = Turtle(shape="turtle")
    Tats.penup()
    Tats.goto(x=-230, y=y_positions[Tats_index])
    Tats.color(colors[Tats_index])
    all_turtle.append(Tats)

if user_bet:
    is_race_on = True

while is_race_on:
    for  turtle in all_turtle:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print("You won !")
            else:
                print(f"You lost, {winning_color}")

        random_distance = random.randint(0, 10)
        turtle.forward(random_distance)


screen.exitonclick()