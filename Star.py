# Deigo Magdaleno
# dmmagdal
# Star.py pa2
# creats a n point star

import turtle

x = int(input("Enter an odd integer greate than or equal to 3: "));
wn = turtle.Screen();
wn.bgcolor("white");
wn.title(str(x)+"pointed star");

bell = turtle.Turtle();
bell.color("blue", "red");
bell.shapesize(.5, .5, 0);
bell.pensize(2);
bell.shape("circle");
my_start = (150, 0);
bell.setx(my_start[0]);
bell.sety(my_start[1]);

bell.begin_fill();
for i in range(x):
	bell.fillcolor("red");
	bell.stamp();
	bell.fillcolor("green");
	#bell.right(180-(2*(180-(360/x)))); formula
	#bell.right((720/x)-180); condensed formula?
	#bell.right(360/x); creates n sided shape which is the internal shape of the star
	#bell.right((720/x)); works for up to 5 points only
	bell.right(180-(180/x));
	bell.forward(300);
bell.end_fill();

bell.fillcolor("red");

wn.mainloop();