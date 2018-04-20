import SchemDraw as schem
import SchemDraw.elements as e

d = schem.Drawing()
V1 = d.add(e.SOURCE_V, label='10V')
d.add(e.LINE)
R1 = d.add(e.RES, d='right', label='100K$\Omega$')
C1 = d.add(e.CAP, d='down', botlabel='0.1$\mu$F')
S1 = d.add(e.INDUCTOR, botlabel='0.2mH')
d.add(e.LINE, to=V1.start)
d.add(e.GND)
d.draw()
#d.save('simple-draw_circuit.eps')
