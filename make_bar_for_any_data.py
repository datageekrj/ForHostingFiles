import plotly.graph_objects as go
import pandas as pd
import numpy as np
import plotly.io as pio

pio.templates.default = "simple_white"

#Replace this line with the data file of your choice. Enter the full path...

data = pd.read_csv(r"C:\Users\rahul\OneDrive\Desktop\MonthlyToYearly\opencv-sentdex\income_per_person_gdppercapita_ppp_inflation_adjusted.csv")


#Documentation for make_bar_chart_function
'''
    This function can be used with a dataset whose one column
    is categorical for which bar chart is required and other columns
    are various years which will serve as a frame rate.
'''

def make_bar_chart(dataset, categrical_col, start_year, end_year, title , frame_rate = 3):
    names = dataset[categrical_col]
    yvals = dataset.loc[:,start_year]
    def get_rgb_vals():
        r = np.random.randint(1,255)
        g = np.random.randint(1,255)
        b = np.random.randint(1,255)
        return [r,g,b]
    colors = []
    for i in range(len(names)):
        c = get_rgb_vals()
        colors.append("rgb(" + str(c[0]) + ","+ str(c[1]) + ","+ str(c[2]) + ")")
       
    def get_top_10(d):
        df = pd.DataFrame({"names":names, "pop":d, "color":colors})
        data = df.sort_values(by = "pop").iloc[-10:,]
        return data

    listOfFrames = []
    for i in range(int(start_year),int(end_year)+1,frame_rate):
        d = data.loc[:,str(i)]
        pdata = get_top_10(d)
        listOfFrames.append(go.Frame(data = [go.Bar(x = pdata["names"], y = pdata["pop"],
                                                    marker_color = pdata["color"], text = pdata["names"],
                                                    hoverinfo = "none",textposition = "outside",
                                                    texttemplate = "%{x}<br>%{y:s}",cliponaxis = False)],
                                     layout = go.Layout(
                                         font = {"size":20},
                                         height = 700,
                                         xaxis = {"showline":False,"tickangle":-90, "visible":False},
                                         yaxis = {"showline":False, "visible":False},
                                        title = title + " For: "+ str(i))))

    fData = get_top_10(yvals)
    
    fig = go.Figure(
    data = [go.Bar(x = fData["names"], y = fData["pop"],
                   marker_color = fData["color"],text = fData["names"],
                  hoverinfo = "none",textposition = "outside",
                   texttemplate = "%{x}<br>%{y:s}",cliponaxis = False)],
    layout=go.Layout(
        title=title + " For: "+str(start_year),
        font = {"size":20},
        height = 700,
        xaxis = {"showline":False,"tickangle":-90, "visible":False},
        yaxis = {"showline":False, "visible":False},
        updatemenus=[dict(
            type="buttons",
            buttons=[dict(label="Play",
                          method="animate",
                          args=[None])])]
    ),
    frames=list(listOfFrames)
    )
    fig.show()
make_bar_chart(data, "country", "1800", "2040",title = "Income Per Person (in Dollors)", frame_rate = 1)
