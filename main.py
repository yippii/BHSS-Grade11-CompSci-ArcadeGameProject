import subprocess
import time
import sys
import shutil
import turtle
import rich.prompt as prompt

# setup screen
screen = turtle.Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("fate: the crimson isle")
screen.setup(width=600, height=400, startx=-1, starty=0)
screen.getcanvas().winfo_toplevel().call('wm', 'attributes', '.', '-topmost', '1')

# setup title turtle
title = turtle.Turtle()
title.hideturtle()
title.speed(0)
title.penup()
title.color("crimson")

def scroll_text(text):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.05)
    print()

def clear_screen():
    subprocess.call('cls' if sys.platform == 'win32' else 'clear', shell=True)
    time.sleep(0.5)

def clear_gui():
    screen.clearscreen()
    screen.bgcolor("black")

def ask_fixed_bottom(question, choices, lines_above):
    height = shutil.get_terminal_size().lines
    blank_lines = max(0, height - len(lines_above) - 2)
    for line in lines_above:
        scroll_text(line)
    print("\n" * blank_lines, end='')
    return prompt.Prompt.ask(question, choices=choices)

def title_screen():
    # draw title
    title.goto(0, 80)
    title.write("fate", align="center", font=("courier", 48, "bold"))

    title.goto(0, 30)
    title.write("the crimson isle", align="center", font=("courier", 24, "normal"))

    # subtitle
    title.color("white")
    title.goto(0, -40)
    title.write("a terminal roguelike adventure", align="center", font=("arial", 14, "italic"))

    # start instruction
    title.goto(0, -100)
    title.write("click anywhere to begin", align="center", font=("arial", 16, "bold"))

    #decorative line
    title.goto(-200, 10)
    title.pendown()
    title.color("crimson")
    title.pensize(3)
    title.forward(400)
    title.penup()

    # click to exit
    def start_game(x, y):
        continueOnTerminal()
        game_init()
        drawMap()
        room1()


    screen.onclick(start_game)

    # keep window open
    turtle.done()

def continueOnTerminal():
    clear_gui()
    # draw title
    title.goto(0, 80)
    title.write("fate", align="center", font=("courier", 48, "bold"))

    title.goto(0, 30)
    title.write("the crimson isle", align="center", font=("courier", 24, "normal"))

    title.color("white")
    title.goto(0, -40)
    title.write("continue on terminal", align="center", font=("arial", 14, "italic"))

def drawMap():
    clear_gui()

    pen = turtle.Turtle()
    pen.pensize(5)
    pen.hideturtle()
    pen.speed(0)
    pen.penup()
    pen.color("white")
    pen.goto(-200, 200)
    pen.pendown()
    pen.forward(400)
    pen.right(90)
    pen.forward(400)
    pen.right(90)
    pen.forward(400)
    pen.right(90)
    pen.forward(400)
    pen.penup()

def room1():
    choice = ask_fixed_bottom(
        "what will you do?",
        choices=["1", "2", "3"],
        lines_above=[
            "you have three options",
            "1. venture into the dark forest",
            "2. explore the ancient ruins",
            "3. seek the wisdom of the old sage",
        ],
    )

    match choice:
        case "1":
            clear_screen()
            scroll_text("you venture into the dark forest, where you encounter a fierce dragon.")
            time.sleep(2)
            scroll_text("you engage in a fierce battle and emerge victorious, earning the respect of the dragon.")
        case "2":
            clear_screen()
            scroll_text("you explore the ancient ruins and discover a hidden treasure.")
        case "3":
            clear_screen()
            scroll_text("you seek the wisdom of the old sage and gain great insight.")

def game_init():
    scroll_text("fate: the crimson isle")
    time.sleep(2)
    scroll_text("you are the explorer, tasked with exploring the single island called the crimson isle.")
    time.sleep(2)
    clear_screen()

if __name__ == "__main__":
    title_screen()