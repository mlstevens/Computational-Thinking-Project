"""
Created on Sun Dec  4 21:04:17 2022

@author: MaxStevens, HunterLawless, ZackLasek
"""

#Import Libaries
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

#DataFrame
df = pd.read_csv("diabetes.csv")

#Data Preprocessing--Dropping unneeded columns
to_drop = ['SkinThickness',
          'Insulin']

df.drop(to_drop, inplace=True, axis=1)

#Question 1: What is the percentage for each kind of outcome in the dataset? (1 = got diabetes, 0 = did not)

def getOutcome():

    #Select Data
    diabetes_y = df[df["Outcome"]==1].shape[0]
    diabetes_n = df[df["Outcome"]==0].shape[0]

    #Assign Data
    labels = ["Diabetes", "No Diabetes"]
    sizes = np.round(([ diabetes_y,diabetes_n]),4)

    #piechart
    fig1, ax1 = plt.subplots()
    ax1.pie(sizes, labels=labels,autopct='%1.1f%%', shadow=True, startangle=90)
    patches, texts, auto = ax1.pie(sizes, shadow=True, startangle=90, autopct='%1.1f%%' )
    plt.legend(patches, labels, loc="best")

    ax1.axis("equal")
    ax1.set_title("Diabetes Ratio in the Dataset")

    #Save figure
    fig1 = plt.gcf()
    plt.show()
    fig1.savefig("Outcome.png")

#Question 2: What is the breakdown of age groups in our dataset

def getAgeBreakdown():

    #Select Data
    adult = df[df["AgeGroup"]==1].shape[0]
    young_adult = df[df["AgeGroup"]==0].shape[0]

    #Assign Data
    labels = ["Adult", "Young Adult"]
    sizes = np.round(([adult,young_adult]),4)

#piechart
    fig1, ax1 = plt.subplots()
    ax1.pie(sizes, labels=labels,autopct='%1.1f%%', shadow=True, startangle=90)
    patches, texts, auto = ax1.pie(sizes, shadow=True, startangle=90, autopct='%1.1f%%' )
    plt.legend(patches, labels, loc="best")

    ax1.axis("equal")
    ax1.set_title("Age Breakdown in the Dataset")

    #Save figure
    fig1 = plt.gcf()
    plt.show()
    fig1.savefig("AgeBreakdown.png")
    
#Question 3: Is there a correlation between BMI and Diabetes Pedigree Function?

def getBMI():

    #Select Data
    bmi = df["BMI"]
    func = df["DiabetesPedigreeFunction"]

    #Scatterplot
    plt.title("BMI and Diabetes Pedigree Function")
    plt.scatter( bmi, func, color = "turquoise" )
    plt.xlabel("BMI")
    plt.ylabel("Diabetes Pedigree Function")

    #Save figure
    fig1 = plt.gcf()
    fig1.savefig("Scatter.png")
    
 
#Question 4: Breakdown of each age group and what proportion has diabetes

def getAgeGroup():

    df_val = df.groupby("AgeGroup")["Outcome"].size()

    #Select Data
    adult = df[df["AgeGroup"]==1].shape[0]
    adult_diabetes = df[(df["AgeGroup"]==1) & (df["Outcome"]==1)].shape[0]

    #Select Data
    young_adult = df[df["AgeGroup"]==0].shape[0]
    young_adult_diabetes = df[(df["AgeGroup"]==0) & (df["Outcome"]==1)].shape[0]

    #Populate plots
    labels = ["Adult (30+)","Young Adult (18-29)"]
    values = np.round(([adult_diabetes/adult*100, young_adult_diabetes/young_adult*100]),4)

    #Bar chart
    plt.figure(figsize = (10,5))
    plt.bar(labels, values, color = "blue", edgecolor = "black", width = .5)
    plt.xlabel("Age Group")
    plt.ylabel("Percentage with Diabetes")
    plt.title("Diabetes Breakdown by Age Group")

    #Save figure
    fig1 = plt.gcf()
    plt.show()
    fig1.savefig("AgeGroup.png")

#Question 5: Breakdown of each weight category and what proportion has diabetes

def getObesity():

    df_val = df.groupby("Obesity")["Outcome"].size()

    #Select data
    obese = df[df["Obesity"]==1].shape[0]
    obese_diabetes = df[(df["Obesity"]==1) & (df["Outcome"]==1)].shape[0]

    #Select data
    not_obese = df[df["Obesity"]==0].shape[0]
    not_obese_diabetes = df[(df["Obesity"]==0) & (df["Outcome"]==1)].shape[0]

    #Populate data
    labels = ["Obese","Not Obese"]
    values = np.round(([obese_diabetes/obese*100, not_obese_diabetes/not_obese*100]),4)

    #Bar Chart
    plt.figure(figsize = (10,5))
    plt.barh(labels, values, color = "gold")
    plt.xlabel("Percentage with Diabetes")
    plt.ylabel("Classification")
    plt.title("Diabetes Breakdown by Obesity")

    #Save figure
    fig1 = plt.gcf()
    plt.show()
    fig1.savefig("Obesity.png")