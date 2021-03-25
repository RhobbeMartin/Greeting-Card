import turtle

#turtle.Screen allows you to define your screen size
screen = turtle.Screen()
screen.setup(500,500)
screen.bgcolor("#8F6161")

# dictionary of colors (https://htmlcolorcodes.com/) to pick color
colors = {
  "blue":"#358FC8",
  "red":"#FF2D00",
  "pink":"#FF00DC",
  "yellow":"#FCFF00",
  "black":"#000000"
}

artist = turtle.Turtle()
artist.shape("turtle")
artist.color(colors["yellow"])

artist.penup()
artist.goto(0, 0)

#(font-family, font-size, fonyt-style)
style = ("fantasy", 30, "normal")
artist.write("Hello there", font = style, align = "center")
artist.hideturtle()
