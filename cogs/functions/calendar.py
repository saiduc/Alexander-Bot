import calendar
import numpy as np
from matplotlib.patches import Rectangle
import matplotlib.pyplot as plt
plt.style.use("seaborn-dark")


def plot_calendar(days, months):
    plt.figure(figsize=(9, 1.8))
    # non days are grayed

    ax = plt.gca().axes
    for d, m in zip(days, months):
        ax.add_patch(Rectangle((d, m), 
                               width=0.9, height=0.9, color='C0'))

    plt.yticks(np.arange(1, 13)+.5, list(calendar.month_abbr)[1:])
    plt.xticks(np.arange(1, 32)+.5, np.arange(1, 32))
    plt.xlim(1, 32)
    plt.ylim(6, 11)
    plt.gca().invert_yaxis()
    # remove borders and ticks
    for spine in plt.gca().spines.values():
        spine.set_visible(True)
    plt.tick_params(top=False, bottom=False, left=False, right=False)
    plt.tight_layout()
    plt.savefig("tmp.jpg")

def getData(name):
    names, dates = np.loadtxt("./data/log.dat", delimiter=",", unpack=True, dtype="str")
    data = []
    for i in range(len(names)):
        if names[i] == name:
            data.append(dates[i])

    months = []
    days = []
    for item in data:
        months.append(int(item.split("-")[1]))
        days.append(int(item.split("-")[2]))
    return days, months
