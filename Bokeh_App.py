from bokeh.io import curdoc
from bokeh.plotting import figure
from bokeh.layouts import widgetbox, row
from bokeh.models import Slider, ColumnDataSource, Select
from bokeh.models.widgets import DataTable, DateFormatter, TableColumn
import pandas as pd
import numpy as np

tom = [300,400,200,400,500]
fertility = [3,5,5,5,6]
fertility = np.array(fertility)
female_literacy = np.array([3,3,2,1,5])
population = np.array([100,330,200,400,500])
source = ColumnDataSource(data={
    'x' : fertility,
    'y' : female_literacy
})

# Create a new plot: plot

# Add circles to the plot
source = ColumnDataSource(data={
    'x' : fertility,
    'y' : female_literacy
})
columns = [
        TableColumn(field="x", title="2018"),
        TableColumn(field="y", title="2019"),
    ]
data_table = DataTable(source=source, columns=columns, width=400, height=280, index_header = " ")


# Define a callback function: update_plot
def update_table(attr, old, new):
    # If the new Selection is 'female_literacy', update 'y' to female_literacy
    if new == 'female_literacy':
        source.data = {
            'x' : fertility,
            'y' : female_literacy
        }
    # Else, update 'y' to population
    else:
        source.data = {
            'x' : tom,
            'y' : population
        }

# Create a dropdown Select widget: select
select = Select(title="distribution", options=['female_literacy', 'tom'], value='female_literacy')

# Attach the update_plot callback to the 'value' property of select
select.on_change('value', update_table)

# Create layout and add to current document
layout = row(select, data_table)
curdoc().add_root(layout)


