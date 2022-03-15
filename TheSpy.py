from bokeh.models.annotations import Tooltip
from numpy import source
from motion_detector import df
from bokeh.plotting import figure
from bokeh.io import show, output_file
from bokeh.models import HoverTool, ColumnDataSource

df["Start_str"]=df["Start"].dt.strftime("%y-%m-%d %h-%M:%S")
df["End_str"]=df["End"].dt.strftime("%y-%m-%d %h-%M:%S")

cds=ColumnDataSource(df)

p=figure(x_axis_type='datetime', height=200, width=1000,  title="Motion Graph")
p.yaxis.minor_tick_line_color=None
#p.ygrid[0].ticker.desired_num_ticks=1

hover=HoverTool(tooltips=[("Start","@Start_str"),("End","@End_str")])
p.add_tools(hover)

q=p.quad(left= "Start", right="End", bottom=0, top=1, color="red", source=cds)

output_file("Graph.html")
show(p)