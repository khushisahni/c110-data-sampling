import plotly.figure_factory as ff
import plotly.graph_objects as go
import statistics
import random
import pandas as pd
import csv

df = pd.read_csv("data.csv")
data = df["temp"].tolist()

population_mean = statistics.mean(data)
std_result = statistics.stdev(data)
print(population_mean)
std_result

def show_fig(mean_list):
    df = mean_list

    fig = ff.create_distplot([data], ["temp"], show_hist=False)
    fig.add_trace(go.Scatter(x = [mean,mean],y = [0,1],mode = "lines", name= "MEAN"))
    fig.show()

#code to find mean and std deviation of 100 data points
dataset = []
for i in range(0, 100):
     random_index= random.randint(0,len(data))
     value = data[random_index]
     dataset.append(value)
mean = statistics.mean(dataset)
std_deviation = statistics.stdev(dataset)

print("Mean of sample:- ",mean)
print("std_deviation of sample:- ",std_deviation)
