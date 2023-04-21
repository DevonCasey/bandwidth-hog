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
df = pd.read_csv(filename , usecols=columns) # Reads the csv selected above into a pandas dataframe 
hostname = df.Hostname[1] # Creates a variable to use for labeling 
print('Selected: ' + filename)
df = df.tail(-1) # There is a null row at the top of the table, lets delete it.
df = df.fillna(0)
df

x_ticks = 250 # A tick every 250 cycles
y_ticks = 5 # A tick every 5 MB
fig = plt.figure(figsize=(20, 4)) # Creates a figure with size 20 x 4.
ax = fig.add_subplot(111)
ax.plot(df.Time, df.BandwidthNIC1, label=hostname) # Uses the label created earlier
ax.xaxis.set_major_locator(ticker.MultipleLocator(x_ticks))
ax.yaxis.set_major_locator(ticker.MultipleLocator(y_ticks))
plt.legend()
plt.show()