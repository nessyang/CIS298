import matplotlib.pyplot as plt

ages = []
totals = []

with open("retirement_results.csv", "r") as file:
    next(file)

    for line in file:
        data = line.strip().split(",")

        ages.append(int(data[0]))
        totals.append(float(data[5]))

plt.plot(ages, totals)
plt.xlabel("Age")
plt.ylabel("Total Savings")
plt.title("Retirement Savings Over Time")
plt.show()