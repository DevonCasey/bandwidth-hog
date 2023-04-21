import pandas as pd
from matplotlib import pyplot as plt
import matplotlib.ticker as ticker
import tk 
from tkinter.filedialog import askopenfilename

columns = ['Hostname', 
           'NIC1', 'BandwidthNIC1', # A column for every NIC
           'NIC2', 'BandwidthNIC2',
           'NIC3', 'BandwidthNIC3',
           'NIC4', 'BandwidthNIC4',
           'NIC5', 'BandwidthNIC5',
           'NIC6', 'BandwidthNIC6',
           'NIC7', 'BandwidthNIC7',
           'NIC8', 'BandwidthNIC8',
           'Time', 'Date'] # Bandwidth is in MB
filename = askopenfilename()
df = pd.read_csv(filename , usecols=columns)
hostname = df.Hostname[1]
print('Selected: ' + filename)
df = df.tail(-1) # there is a null row at the top of the table, lets delete it.

x_ticks = 250 # a tick every 250 cycles
y_ticks = 5 # a tick every 5 MB
fig = plt.figure(figsize=(20, 4))
ax = fig.add_subplot(111)
ax.plot(df.Time, df.BandwidthNIC1, label=hostname)
ax.xaxis.set_major_locator(ticker.MultipleLocator(x_ticks)) # set the ticks
ax.yaxis.set_major_locator(ticker.MultipleLocator(y_ticks))
plt.legend()
plt.show()