from bokeh.plotting import figure
from bokeh.layouts import widgetbox, row
from bokeh.models import Slider, ColumnDataSource, Select
from bokeh.models.widgets import DataTable, DateFormatter, TableColumn
import pandas as pd
import numpy as np
from matplotlib.pyplot import figure
figure(num=None, figsize=(8, 6), dpi=250, facecolor='w', edgecolor='k')
x = np.arange(10)

plt.plot(x, x)
plt.plot(x, x*2)
plt.plot(x, x*3)

plt.show()
