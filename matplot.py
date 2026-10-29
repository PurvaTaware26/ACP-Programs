
import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y = [10, 20, 15, 25, 30]
data = [10, 12, 15, 15, 18, 20, 20, 22, 25, 30]

plt.figure(figsize=(10, 8))

# 1. Line Graph
plt.subplot(3, 2, 1)
plt.plot(x, y, marker='o')
plt.title("Line Graph")

# 2. Bar Graph
plt.subplot(3, 2, 2)
plt.bar(x, y)
plt.title("Bar Graph")

# 3. Scatter Plot
plt.subplot(3, 2, 3)
plt.scatter(x, y)
plt.title("Scatter Plot")

# 4. Pie Chart
plt.subplot(3, 2, 4)
plt.pie(y, labels=x, autopct='%1.1f%%')
plt.title("Pie Chart")

# 5. Histogram
plt.subplot(3, 2, 5)
plt.hist(data, bins=5)
plt.title("Histogram")

plt.tight_layout()
plt.show()
