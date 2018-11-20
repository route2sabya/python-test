from datetime import date
from nsepy import get_history
infy = get_history(symbol='INFY',
                   start=date(2015,1,1),
                   end=date(2015,12,31))
#print (infy)
#print (infy.columns)

tcs = get_history(symbol='TCS',
                   start=date(2015,1,1),
                   end=date(2015,12,31))
#print (tcs.columns)


# NIFTY Next 50 index
nifty_it = get_history(symbol="NIFTY IT",
                            start=date(2015,1,1),
                            end=date(2015,12,31),
                            index=True)
"""
# Part - 1
#   Task 1
def rolling_windowSize(week_factor):

    window_size_list = []
    for i in range(0,52):
        window_size = (i+1) * week_factor
        if window_size < 53:
            window_size_list.append(window_size)
    return (window_size_list)
        
    
def calc_moving_avg(close_fieldname,window_list,df):
    closing = close_fieldname
    for i in window_list:
        ma_closing = 'moving_avg_{0}_{1}'.format(close_fieldname,i)
        df[ma_closing] = df[closing].rolling(window=i).mean()
        #infy[ma_closing] = infy[closing].rolling(window=30).mean()
        #nifty_it[ma_closing] = nifty_it[closing].rolling(window=30).mean()

    print (df.columns)
    return df

week_list = rolling_windowSize(4)
df_niftyIt = calc_moving_avg('Close',week_list,nifty_it)
df_infy = calc_moving_avg('Close',week_list,infy)
df_tcs = calc_moving_avg('Close',week_list,tcs)



print (df_niftyIt.columns)

# Task 2
# rolling window

# generate 10 day, 20 day , 30 day, 40 day, 50 day, 60 day, 75 day moving average
new_week_list = [10,20,30,40,50,60,75]
df_ma_tcs = calc_moving_avg('Close',new_week_list,df_tcs)
df_ma_infy = calc_moving_avg('Close',new_week_list,df_infy)
df_ma_niftyIt = calc_moving_avg('Close',new_week_list,df_niftyIt)

"""
"""
# Task 3
# sub-task 1 ++++++++++++++

infy['Volume_Shock'] = 0
infy['Volume_Change'] = 0
infy['Volume_Direction'] = 1
infy['Volume_Shock'][0] = infy['Volume'][0]
infy['Volume_Shock'] = ((infy['Volume']/infy['Volume'].shift(1))*100) - 100
infy['Volume_Change'] = ((infy['Volume']/infy['Volume'].shift(1))*100) - 100

#print (infy['Volume_Shock'].head(10))


for i in range(1, len(infy)):
    if (infy['Volume_Shock'][i] > 10) or (infy['Volume_Shock'][i] < -10) :
        infy['Volume_Shock'][i] = 1
                        
    else:
        infy['Volume_Shock'][i] = 0
#print (infy['Volume_Shock'])
for i in range(1, len(infy)):
    if infy['Volume_Change'][i] > 0:
        infy['Volume_Direction'] [i] = 1
    else:
        infy['Volume_Direction'] [i] = 0
#print (infy['Volume_Direction'])
#print (infy.columns)
"""

# sub-task 2 ++++++++++++++

"""    
infy['Price_Shock'] = 0
infy['Price_Change'] = 0
infy['Price_Direction'] = 1
infy['Price_Shock'][0] = infy['Close'][0]
infy['Price_Shock'] = ((infy['Close']/infy['Close'].shift(1))*100) - 100
infy['Price_Change'] = ((infy['Close']/infy['Close'].shift(1))*100) - 100


for i in range(1, len(infy)):
    if (infy['Price_Shock'][i] > 2) or (infy['Price_Shock'][i] < -2) :
        infy['Price_Shock'][i] = 1
                        
    else:
        infy['Price_Shock'][i] = 0
#print (infy['Volume_Shock'])
for i in range(1, len(infy)):
    if infy['Price_Change'][i] > 0:
        infy['Price_Direction'] [i] = 1
    else:
        infy['Price_Direction'] [i] = 0
print (infy['Price_Direction'])
print (infy['Price_Shock'])
print (infy['Price_Change'])
"""
"""
"""
def calc_deriv(fieldname,df,threshold):

    shock = 'Shock'
    change = 'Change'
    direction = 'Direction'

    field_shock = '{0}_{1}'.format(fieldname,shock)
    field_change = '{0}_{1}'.format(fieldname,change)
    field_direction = '{0}_{1}'.format(fieldname,direction)
    df[field_shock] = 0
    df[field_change] = 0
    df[field_direction] = 0
    df[field_shock][0] = df[fieldname][0]
    df[field_shock] = ((df[fieldname]/df[fieldname].shift(1))*100) - 100
    df[field_change] = ((df[fieldname]/df[fieldname].shift(1))*100) - 100
    for i in range(1, len(df)):
        if (df[field_shock][i] > threshold) or (df[field_shock][i] < -(threshold)) :
            df[field_shock][i] = 1
                        
        else:
            df[field_shock][i] = 0

    for i in range(1, len(df)):
        if df[field_change][i] > 0:
            df[field_direction] [i] = 1
        else:
            df[field_direction] [i] = 0
    return df
    
infy_vol_deriv = calc_deriv('Volume',infy,10)
#print (infy_vol_deriv.columns)
infy_close_deriv = calc_deriv('Close',infy_vol_deriv,2)
#print (infy_close_deriv.columns)
infy_Prevclose_deriv = calc_deriv('Prev Close',infy_close_deriv,2)
print (infy_Prevclose_deriv.columns)


import warnings
warnings.filterwarnings('ignore')
from bokeh.plotting import figure, show, output_file, output_notebook
from bokeh.palettes import Spectral11, colorblind, Inferno, BuGn, brewer
from bokeh.models import HoverTool, value, LabelSet, Legend, ColumnDataSource,LinearColorMapper,BasicTicker, PrintfTickFormatter, ColorBar
import datetime
import pandas as pd
print (infy)
infy['datetime'] = infy.index
infy['month'] = pd.DatetimeIndex(infy['datetime']).month
"""
TOOLS = 'save,pan,box_zoom,reset,wheel_zoom,hover'
p = figure(title="Daily closing", y_axis_type="linear", plot_height = 400,
           tools = TOOLS, plot_width = 800)
p.xaxis.axis_label = 'month'
p.yaxis.axis_label = 'Closing value'
#p.circle(2010, infy.Close.min(), size = 10, color = 'red')

p.line(infy.month, infy.Close,line_color="blue", line_width = 2)
p.select_one(HoverTool).tooltips = [
    ('month', '@x'),
    ('Closing value', '@y'),
]

output_file("line_chart.html", title="Line Chart")
show(p)
#['date'] = pd.to_datetime(df['date'], format='%d%b%Y')
"""
tcs['datetime'] = tcs.index
tcs['month'] = pd.DatetimeIndex(tcs['datetime']).month

nifty_it['datetime'] = nifty_it.index
nifty_it['month'] = pd.DatetimeIndex(nifty_it['datetime']).month

"""
TOOLS_mp = 'crosshair,save,pan,box_zoom,reset,wheel_zoom'
mp = figure(title="Category-wise stock measures through Time", y_axis_type="linear",x_axis_type='datetime', tools = TOOLS_mp)

mp.line(infy['month'], infy.Volume_Shock, legend="Volume Shock Dummy INFY", line_color="purple", line_width = 3)
mp.line(tcs['month'], tcs.Volume_Shock, legend="Volume Shock Dummy TCS", line_color="blue", line_width = 3)
mp.line(nifty_it['month'], nifty_it.Volume_Shock, legend="Volume Shock Dummy NIFTY IT", line_color="red", line_width = 3)
#mp.line(vehicle_theft['Date'], vehicle_theft.IncidntNum, legend="vehicle_theft", line_color = 'coral', line_width = 3)

#mp.line(larceny['Date'], larceny.IncidntNum, legend="larceny", line_color='green', line_width = 3)

#mp.line(vandalism['Date'], vandalism.IncidntNum, legend="vandalism", line_color="gold", line_width = 3)

#mp.line(arson['Date'], arson.IncidntNum, legend="arson", line_color="magenta",line_width = 3)

mp.legend.location = "top_left"

mp.xaxis.axis_label = 'Month'
mp.yaxis.axis_label = 'Values'


output_file("multiline_plot.html", title="Multi Line Plot")

show(mp)
"""
"""
import numpy as np
from bokeh.plotting import figure, show
from bokeh.models import ColumnDataSource, LinearColorMapper


TOOLS='pan,wheel_zoom,box_zoom,reset'
p = figure(tools=TOOLS)

x = np.linspace(-10,10,200)
#y = -x**2

data_source = ColumnDataSource({'':x,'y':y})

color_mapper = LinearColorMapper(palette='Magma256', low=min(y), high=max(y))

# specify that we want to map the colors to the y values, 
# this could be replaced with a list of colors
p.scatter(x,y,color={'field': 'y', 'transform': color_mapper})

show(p)
"""
