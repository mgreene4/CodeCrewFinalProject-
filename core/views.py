from django.shortcuts import render

#import plotting libraries
import pandas as pd
import plotly.express as px

#Read in CSV as a DataFrame
df = pd.read_csv('core\data\std-rates-by-state-2024.csv')

#function for data analysis of CSV - choose one graph / feature per function.
def chart(request):

    #plot variables into a graph
    fig = px.bar(
        
        df, #the dataframe you read in
        x="state", #set x variable to date column
        y="STDRatesChlamydiaRatePer100k", #set y variable to average column
        title='Chlamydia Rates by State', #create title for plot

    )

    fig2 = px.bar(

        df,
        x="state",
        y="STDRatesGonorrheaRatePer100k",
        title='Gonorrhea Rates by State',
    )

    fig3 = px.bar(
        df,
        x="state",
        y="STDRatesSyphilisPrimaryAndSecondaryCasesPer100k",
        title= 'Syphilis Rates by State',
    )

    demographics = pd.read_csv('core/data/filtered descriptive analysis(Sheet2).csv')

    demographics = demographics.rename(columns= {
    'Unnamed: 0' : 'Demographic',
    'Unnamed: 2' : '2015%',
    'Unnamed: 4' : '2017%',
    'Unnamed: 6' : 'NDFS%'
    })

    age = demographics[2:9]

    fig4 = px.pie(
        age,
        values= '2015%',
        names= 'Demographic',
        title= 'Age of Students in 2015',
    )

    student_behavior = pd.read_csv('core/data/filtered descriptive analysis(Sheet1).csv')

    student_behavior = student_behavior[~student_behavior.index.isin([1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23])]

    fig5 = px.bar(
        student_behavior,
        x= 'Questions',
        y= '2015',
        title= 'Student Behaviors in 2015'
    )

    #convert graph to an html object
    chart = fig.to_html()
    chart2 = fig2.to_html()
    chart3 = fig3.to_html()
    chart4 = fig4.to_html()
    chart5 = fig5.to_html()

    #send html object to the url page
    context = {'chart': chart, 'chart2': chart2, 'chart3': chart3, 'chart4': chart4, 'chart5': chart5}

    return render(request, 'core/chart.html', context)