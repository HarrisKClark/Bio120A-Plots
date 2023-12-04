from itertools import chain
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns


# Data

trial_data_1 = [[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,1,0,0,0,0,0],[1,1,0,0,0,0,0,0,0,1],[1,1,1,1,1,1,1,1,0,0],[1,1,1,1,1,1,1,1,1,1]]
trial_data_2 = [[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,1,1,1,0,0,0,0,0],[1,1,1,1,1,1,1,1,1,1],[1,1,1,1,1,1,1,1,1,1]]
trial_data_combined = [[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0],[0,0,1,1,1,0,0,0,0,0,1,1,0,0,0,0,0,0,0,1],[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0],[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]]
trial_data = trial_data_combined
A_values = [-42.5,-30,0,28.5,65.5]

# Data processing

trial_data_y = []
for x in trial_data:
    trial_data_y.append(x)

trial_data_y = list(chain.from_iterable(trial_data_y))

trial_data_x = []
for i in range(0,len(A_values)):
    trial_data_x.append([A_values[i]]*len(trial_data[i]))

trial_data_x = list(chain.from_iterable(trial_data_x))

data = [trial_data_x,trial_data_y]
data_df = pd.DataFrame(data).transpose()

x = data[0]
y = data[1]


#plot

fig, ax = plt.subplots()
plt.title( "Psychometric Function + Scatterplot From Combined Dataset (yk vs A)")
plt.xlabel("A value % (A)")
plt.ylabel("Heavier (yk)")
#ax = sns.regplot(x=x, y=y, data=data_df, ax=ax, ci=None, logistic=True,line_kws={'alpha':0, 'color': 'red'}, scatter_kws={'color': 'black'}, x_jitter=3, y_jitter=0.03)
ax = sns.regplot(x=x, y=y, data=data_df, ax=ax, ci=None, logistic=True,line_kws={'color': 'red'}, scatter_kws={'color': 'black'}, x_jitter=3, y_jitter=0.03)

plt.show()
