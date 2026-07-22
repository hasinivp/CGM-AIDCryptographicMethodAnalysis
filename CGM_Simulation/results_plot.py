import matplotlib.pyplot as plt
import matplotlib.cbook as cbook

import numpy as np
import pandas as pd

filename = 'results.csv'
dataframe = pd.read_csv(filename)

dataframe.set_index("Encryption_Algorithm", inplace=True)
dataframe["Average_Encryption_Time"] *= 10000000
dataframe["Average_Decryption_Time"] *= 10000000
#Plot 1
#dataframe.set_index("Encryption_Algorithm", inplace=True)
ax = dataframe[["Average_Encryption_Time", "Average_Decryption_Time"]].plot(kind="bar", figsize=(10,6), width=.8)

ax.set_ylabel("Time (microseconds)")
ax.set_xlabel("Encryption Algorithm")
ax.set_title("Encryption/Decryption Time Comparsion")
plt.xticks(rotation=45, ha="right")
plt.tight_layout()
plt.show()
#Plot 2
ax2 = dataframe[["Average_Peak_Encryption_Memory", "Average_Peak_Decryption_Memory"]].plot(kind="bar", figsize=(10,6), width=.8)

ax2.set_ylabel("Memory Used (bytes)")
ax2.set_xlabel("Encryption Algorithm")
ax2.set_title("Encryption/Decryption Memory  Comparsion")
plt.xticks(rotation=45, ha="right")
plt.tight_layout()
plt.show()
