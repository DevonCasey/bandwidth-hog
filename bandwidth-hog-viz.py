import pandas as pd
from matplotlib import pyplot as plt
import matplotlib.ticker as ticker
import tk 
from tkinter.filedialog import askopenfilename

plt.rcParams["figure.figsize"] = [7,3.5] # creates a figure of given sizes
plt.rcParams['figure.autolayout'] = True
columns = ['Hostname', 'NIC', 'Bandwidth', 'Time', 'Date'] # creates an array of names to use for columns, bandwidth is in MB
filename = askopenfilename() # prompts user to open a .csv
df = pd.read_csv(filename , usecols=columns) # reads the csv into a pandas dataframe
print("Selected: " + filename) # you did it. yay.

df = df.drop(columns=['Hostname','NIC', 'Date']) # get rid of those columns... 
df = df.tail(-1) # there is a NaN row at 0 because of powershell being dumb. get rid of it.

x_ticks = 50 # a tick every 50 seconds 
y_ticks = 5 # a tick every 5 MB
fig, ax = plt.subplots(1,1) 
ax.plot(df.Time, df.Bandwidth, label='Server 1')
ax.xaxis.set_major_locator(ticker.MultipleLocator(x_ticks))
ax.yaxis.set_major_locator(ticker.MultipleLocator(y_ticks))
plt.legend()
plt.show()