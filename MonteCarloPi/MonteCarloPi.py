import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
from numpy import random

sns.set(rc={'figure.figsize':(8,8)})
sns.set_style("white")

tries = [1,2,3,4,5,6]


def estimate_py(tries):

    points = []

    for i in range(tries):

        point = {}
        x = random.uniform(-1,1)
        y = random.uniform(-1,1)

        point['x_coord'] = x
        point['y_coord'] = y

        if x ** 2 + y ** 2 < 1.0:
            point['status'] = 'circle'
        else:
            point['status'] = 'square'

        points.append(point)


    points_frame = pd.DataFrame(points)

    sns.scatterplot(x= 'x_coord', y = 'y_coord',data=points_frame, hue='status' , linewidth=0, legend=None)

    estimated_pi = len(points_frame[points_frame['status'] == 'circle']) / tries * 4


    plt.title(f'Estimated Pi = {estimated_pi}')
    plt.savefig(f'results/try_{tries}.jpg')


for number in tries:
    estimate_py(10**number)
