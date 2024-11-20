Code Explanation: 
It begins by importing the necessary libraries 'Pygame' for graphics and math since it mathematical functions and 'datetime' to retrieve the current time in the system.
Next is constants which is the height, width, display and radius of the clock face. Also the frames per second for the loop.
Colors : these values deifined using RGB tuples to specify the clock's graphics
Display: the display window is specified by the height and with followed with a caption on the title window
Font: the font is loaded for rendering the hours of the clock face
On the 'draw_clock_face' function: it creates the clocks circular face with the hour markers around it. It calculates using trigonometic functions to adjust the clock's center and radius
It also rendered and positioned at the calculated coordinates.
On the 'draw_hand' function: it is based on the length, angle, width and color. the end position of the hand uses trigonometric functions and a line is drawn at the center of the clock to this position
On the 'draw_clock' function: it retrieves the current time using 'date time'. Also it calculates the angle for the minute and second hands taking into account of the current seconds and minutes.
It calls the 'draw_clock_face()' to draw the clock face and then draws the minute and second hands using the 'draw_hand' function
