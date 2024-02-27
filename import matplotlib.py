import matplotlib.pyplot as plt

languages = ['Rust', 'Python', 'TypeScript', 'Kotlin', 'Go', 'Java', 'C#', 'C++', 'PHP', 'Ruby']
percentages = [66.7, 66.4, 65.6, 65.2, 64.8, 64.1, 63.5, 62.7, 62.4, 61.8]

colors = ['#DEA584', '#306998', '#007ACC', '#4D97FF', '#00ADD8', '#5382A1', '#68217A', '#00599C', '#8892BF', '#CC342D']

plt.figure(figsize=(8, 8))
plt.pie(percentages, labels=languages, colors=colors, autopct='%1.1f%%', startangle=140)
plt.axis('equal')  

plt.title('Programming Languages Popularity''\n ')

plt.show()
