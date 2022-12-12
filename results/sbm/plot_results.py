import pandas as pd
import matplotlib.pyplot as plt
import os

# Data Load
file_name = "cycle_results_5_1000_0.01.csv"
df = pd.read_csv(file_name, sep=',', skipinitialspace=True)

# Plot (p_over_q vs. rand)
for num_eigen, group in df.groupby("eigenvectors"):
    # if num_eigen % 3 != 1:
        # continue

    plt.plot(group["poverq"], group["rand"], label=f"{num_eigen} vectors")
plt.legend()
plt.xlabel(r"$p/q$")
plt.ylabel("Correctly Classified")
plt.show()
