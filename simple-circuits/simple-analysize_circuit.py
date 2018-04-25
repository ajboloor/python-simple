import SchemDraw as schem
import SchemDraw.elements as e
from PySpice.Spice.Netlist import Circuit
from PySpice.Unit import *

circuit_width = 4
circuit_height = 4

node_dict = {(0,0):1, (0,1):2, (0,2):3, (0,3):4, (0,4):5, \
             (1,4):6, (2,4):7, (3,4):8, (4,4):9, \
             (4,3):10, (4,2):11, (4,1):12, (4,0):13, \
             (3,0):14, (2,0):15, (1,0):16}

 # elements of the form:
 # [id (int), type(str), start([int, int]), end([int, int]), value(float)]
elements = [[1, 'W', (0,0), (0,1), 5], [1, 'V', (0,1), (0,2), 10], [1, 'W', (0,2), (0,3), 10], [0, 'W', (0,3), (0,4), 0], \
            [1, 'W', (0,4), (1,4), 0], [1, 'R', (1,4), (2,4), 10], [3, 'W', (2,4), (3,4), 5], [4, 'W', (3,4), (4,4), 5], \
            [1, 'W', (4,4), (4,3), 0], [2, 'R', (4,3), (4,2), 10], [3, 'W', (4,2), (4,1), 5], [4, 'W', (4,1), (4,0), 5], \
            [1, 'W', (4,0), (3,0), 0], [1, 'W', (3,0), (2,0), 5], [3, 'W', (2,0), (1,0), 5], [4, 'W', (1,0), (0,0), 5]]
elements.append([1, 'G', (0,0), (0,0), 0])

draw_scale = 1
d = schem.Drawing()
circuit = Circuit('Voltage Divider')
ctr = 1
for ele in elements:
    # to define the starting and ending points of the elements
    ele_start = [draw_scale*i for i in ele[2]]
    ele_end = [draw_scale*i for i in ele[3]]
    if ele[1][0] == 'R':
        ele_label_top = 'R'+str(ele[0])
        ele_label_bot = str(ele[4])+'K$\Omega$'
        d.add(e.RES, label = ele_label_top, botlabel= ele_label_bot, xy = ele_start, to = ele_end)
        circuit.R(ctr, node_dict[ele[2]], node_dict[ele[3]], ele[4]@u_kΩ)
        ctr = ctr+1
    elif ele[1] == 'W':
        # e.LINE represents wires
        d.add(e.LINE, xy = ele_start, to = ele_end)
        circuit.R(ctr, node_dict[ele[2]], node_dict[ele[3]], 0@u_kΩ)
        ctr = ctr+1
    elif ele[1] == 'V':
        ele_label_top = 'V'+str(ele[0])
        ele_label_bot = str(ele[4])+'V'
        d.add(e.SOURCE_V, label = ele_label_top, botlabel = ele_label_bot , xy = ele_start, to = ele_end)
        circuit.V('input', node_dict[ele[2]], node_dict[ele[3]], ele[4]@u_V)
    elif ele[1] == 'G':
        ele_label_top = 'GND'
        d.add(e.GND, botlabel = ele_label_top, xy = ele_start, d = 'right')

simulator = circuit.simulator(temperature=25, nominal_temperature=25)

analysis = simulator.operating_point()
for node in analysis.nodes.values():
    print('Node {}: {:4.1f} V'.format(str(node), float(node))) # Fixme: format value + unit

d.draw()


#d.save('simple-draw_circuit.eps')
