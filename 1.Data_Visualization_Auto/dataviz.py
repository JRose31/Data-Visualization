"""
Created on Wed May 27 13:39:27 2020

@author: jamaine.roseborough
"""

import pandas as pd
import matplotlib.pyplot as plt
from data_manipulation import sort_list

df = pd.read_csv('Automobile_data.csv', na_values = {
        'price':["?", "n.a"],
        'stroke':["?", "n.a"],
        'horsepower':["?", "n.a"],
        'peak-rpm':["?", "n.a"],
        'average-milage':["?", "n.a"]})

car_types = df.groupby('company')

mileageDf = car_types['company', 'average-mileage'].mean()


cars = []
for i in car_types['company']:
    cars.append(i[0])

mpg = []
for i in mileageDf['average-mileage']:
    mpg.append(round(i))

mpg, cars = sort_list(mpg, cars)
cars = [car.capitalize() for car in cars]

plt.style.use('ggplot')
plt.barh(cars, mpg)
plt.title("Avg MPG per Car Brand")
plt.xlabel("Average MPG (miles per gallon)")
plt.ylabel("Car Brand")

for i, v in enumerate(mpg):
    plt.text(v + .4, i - .2, str(v), color='black', fontsize='small', family='sans-serif')

plt.show()
