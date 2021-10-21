## Oppgave 3: Kjede av srikler - FRIVILLIG
from ezgraphics import GraphicsWindow

## Lag et vindu og tegn et kanvas.
win = GraphicsWindow(500, 500)
canvas = win.canvas()
teller = 0
x_pos = 10
y_pos = 40

while(teller < 9):
    canvas.drawOval(x_pos, y_pos, 50, 50)
    teller += 1
    x_pos += 10
    y_pos += 10 * 3.14

## Vent på at vinduet lukkes
win.wait()