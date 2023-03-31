import matplotlib.pyplot as plt  # eenmaal importeren is voldoende

x = laptops.RAM.value_counts().sort_index()
labels = ['1GB', '2GB', '4GB', '8GB', '16GB']

fig, ax = plt.subplots(figsize=(10, 5))

_ = ax.bar(x=labels, height=x, color='green')
_ = ax.set_title('RAM in laptops')
_ = ax.set_xlabel('RAM geheugen (Gb)')
_ = ax.set_ylabel('Aantal')

import matplotlib.pyplot as plt  # eenmaal importeren is voldoende

fig, axes = plt.subplots()

_ = axes.hist(laptops.diskspace, edgecolor='black', alpha=0.5, label='RAM')
_ = axes.set_title('Schijfruimte in laptops')
_ = axes.set_xlabel('Schijfruimte (Gb)')
_ = axes.set_ylabel('Aantal')
_ = axes.legend()

"Klassen zelf opgegeven"
fig, axes = plt.subplots()
cutpoints = [0, 185, 375, 750, 1100]

_ = axes.hist(laptops.diskspace, bins=cutpoints, edgecolor='black', alpha=0.5, label='RAM')
_ = axes.set_title('Schijfruimte in laptops met cutpoints')
_ = axes.set_xlabel('Schijfruimte (Gb)')
_ = axes.set_ylabel('Aantal')
_ = axes.legend()