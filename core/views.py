from django.shortcuts import render

#import plotting libraries
import pandas as pd
import plotly.express as px

#Read in CSV as a DataFrame
df = pd.read_csv('core/data/co2_mm_mlo.csv')

#function for data analysis of CSV - choose one graph / feature per function.
def chart(request):

    #plot variables into a graph
    fig = px.line(
        
        df, #the dataframe you read in
        x="year", #set x variable to date column
        y="average", #set y variable to average column
        title='Average C02 Levels by Day', #create title for plot
        markers=True, #add point markers to plot

    )

    #convert graph to an html object
    chart = fig.to_html()

    #send html object to the url page
    context = {'chart': chart}
    return render(request, 'core/chart.html', context)