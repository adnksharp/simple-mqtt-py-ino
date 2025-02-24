from matplotlib.pyplot import ion, ioff, subplots
from tabulate import tabulate
from json import loads

def tab(prints):
    print(tabulate([prints], floatfmt='.5f', tablefmt='simple_grid'))

class Plot():
    def __init__(self):
        self.d = 50000
        self.x, self.y = [0.0] * self.d, [0.0] * self.d
        self.theta = 0.0
        ion()
        self.fig, self.ax = subplots()
        self.line, = self.ax.plot(self.x, self.y, marker='.', color='red', ms=1)

    def index(self, pos):
        self.x.pop(0)
        self.y.pop(0)
        self.x.append(float(pos[0]))
        self.y.append(float(pos[1]))
        self.theta = float(pos[2])

    def get(self, client, userdata, msg):
        data = loads(msg.payload.decode('utf-8'))
        self.index(data['pos'])
        tab(data['pos'])

    def show(self):
        self.line.set_xdata(self.x)
        self.line.set_ydata(self.y)
        self.ax.relim()
        self.ax.autoscale_view()
        self.fig.canvas.draw_idle()
        self.fig.canvas.flush_events()
