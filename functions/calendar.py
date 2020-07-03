import calendar
import numpy as np
from matplotlib.patches import Rectangle
import matplotlib.pyplot as plt
from datetime import datetime, timedelta
plt.style.use("seaborn-dark")


def plot_calendar(days, months):
    plt.figure(figsize=(9, 1.8))
    # non days are grayed

    ax = plt.gca().axes
    weekend_days, weekend_months = get_weekends(2020)

    for i in range(len(weekend_days)):
        ax.add_patch(Rectangle((weekend_days[i], weekend_months[i]), width=.9, height=.9, color='gray', alpha=.3))

    ax.add_patch(Rectangle((30, 6), width=.9, height=.9, color='gray', alpha=.3))

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


def get_data(name):
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


def get_weekends(year):
    weekend_day = []
    weekend_month = [] 
    start = datetime(year, 1, 1)
    for i in range(365):
        day_of_the_year = start + timedelta(days=i)
        if day_of_the_year.weekday() > 4:
            weekend_day.append(day_of_the_year.day)
            weekend_month.append(day_of_the_year.month)
    return weekend_day, weekend_month
