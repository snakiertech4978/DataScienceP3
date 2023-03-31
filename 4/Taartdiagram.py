import matplotlib.pyplot as plt  # eenmaal importeren is voldoende
import numpy as np

x = laptops.RAM.value_counts().sort_index()
labels = ['1GB', '2GB', '4GB', '8GB', '16GB']
explode = np.full(len(labels), 0.05)

fig, ax = plt.subplots()
_ = ax.pie(x, labels=labels, explode=explode, shadow=True)
_ = ax.set_title('RAM in laptops')