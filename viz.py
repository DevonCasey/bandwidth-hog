import pandas as pd
from matplotlib import pyplot as plt
import matplotlib.ticker as ticker
import tk 
from tkinter.filedialog import askopenfilename

plt.rcParams["figure.figsize"] = [7,3.5]
plt.rcParams['figure.autolayout'] = True
columns = ['Hostname', 'NIC', 'Bandwidth', 'Time']
filename = askopenfilename()
df = pd.read_csv(filename , usecols=columns)
print("Selected: " + filename)

df = df.drop(columns=['Hostname','NIC'])
df = df.tail(-1)

x_ticks = 50
y_ticks = 5
fig, ax = plt.subplots(1,1)
ax.plot(df.Time, df.Bandwidth, label='Server 1')
ax.xaxis.set_major_locator(ticker.MultipleLocator(x_ticks))
ax.yaxis.set_major_locator(ticker.MultipleLocator(y_ticks))
plt.legend()
plt.show()