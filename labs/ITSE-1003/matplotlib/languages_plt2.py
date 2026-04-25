import matplotlib.pyplot as plt

languages = ["Python", "Java", "C#", "Go"]
votes = [100, 80, 60, 40]
explode = [0.1, 0, 0, 0]
colors = ["red", "blue", "green", "yellow"]

plt.pie(
    votes,
    explode=explode,
    labels=languages,
    colors=colors,
    autopct="%1.1f%%",
    shadow=True,
    startangle=90,
)
plt.title("Programming Language Votes", fontsize=16, fontweight="bold")
plt.show()
