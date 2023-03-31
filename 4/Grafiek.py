import matplotlib.pyplot as plt  # eenmaal importeren is voldoende

fig, ax = plt.subplots()
_ = ax.plot([1, 2, 3, 4], [0, 4, 6, 7])
_ = ax.set_xlabel('tijd (seconden)')
_ = ax.set_ylabel('temperatuur (Kelvin)')
_ = ax.set_title('Temperatuurverloop')
_ = ax.grid(linestyle='--')
_ = ax.legend(['temperatuur'])


fig.show()
fig.savefig('pyplot1');
