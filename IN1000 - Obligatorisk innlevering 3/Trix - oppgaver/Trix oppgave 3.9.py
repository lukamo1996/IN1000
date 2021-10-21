## Trix oppgave 3.9 - Flere sirkler
from ezgraphics import GraphicsWindow
win = GraphicsWindow(500, 500)
canvas = win.canvas()
canvas.drawRect(30, 30, 30, 30)
canvas.drawOval(20, 20, 50, 50)
canvas.drawOval(120, 20, 50, 50)
canvas.drawOval(220, 40, 50, 50)
canvas.drawOval(320, 60, 50, 70)
win.wait()