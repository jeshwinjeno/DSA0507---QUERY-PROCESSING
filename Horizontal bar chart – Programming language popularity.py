import matplotlib.pyplot as plt

# Data
languages = ['Java', 'Python', 'PHP', 'JavaScript', 'C#', 'C++']
popularity = [22.2, 17.6, 8.8, 8.0, 7.7, 6.7]

# Plot
plt.barh(languages, popularity)
plt.xlabel("Popularity Percentage")
plt.ylabel("Programming Languages")
plt.title("Popularity of Programming Languages (Horizontal Bar Chart)")
plt.show()
