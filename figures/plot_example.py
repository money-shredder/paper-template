import os
import csv

from matplotlib import rc
from matplotlib import pyplot as plt

# use `usetex=True` to render math symbols with LaTeX
rc('text', usetex=True)
rc('font', **{'family': 'serif', 'serif': ['Times']})


root = os.path.dirname(__file__)


with open(os.path.join(root, '..', 'data', 'example.csv'), 'r') as f:
    reader = csv.reader(f)
    data = list(reader)
    # remove header
    data = data[1:]


x, y = [float(row[0]) for row in data], [float(row[1]) for row in data]
fig = plt.figure(figsize=(4, 3))
ax = fig.add_subplot(111)
ax.plot(x, y, '-', label='data')
ax.set_xlim(min(x), max(x))
ax.grid(True)
ax.set_xlabel(r'\( x \)')
ax.set_ylabel(r'\( \sin(x) \)')
fig.tight_layout()
fig.savefig(os.path.join(root, 'plot_example.pdf'))
