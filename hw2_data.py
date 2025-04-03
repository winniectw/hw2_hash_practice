import os
import matplotlib.pyplot as plt

base_dir = os.path.dirname(os.path.abspath(__file__))
path = os.path.join(base_dir, 'hw2_data.txt')

lines = []

with open(path, 'r', encoding='utf-8') as f:
    for entry in f:
        token = entry.strip().lower()
        if token:
            lines.append(token)

word_totals = {}

for item in lines:
    if item in word_totals:
        word_totals[item] += 1
    else:
        word_totals[item] = 1

sorted_keys = list(word_totals.keys())
sorted_keys.sort(key=lambda w: word_totals[w], reverse=True)

x_labels = []
y_values = []

for key in sorted_keys:
    x_labels.append(key)
    y_values.append(word_totals[key])

plt.figure(figsize=(10, 6))
bars = plt.bar(x_labels, y_values)

for i in range(len(bars)):
    plt.text(i, y_values[i] + 2, str(y_values[i]), ha='center', va='bottom')

plt.title("Word Frequency", fontsize=16, fontweight='bold')
plt.xlabel("Word", fontsize=12, fontweight='bold', labelpad=15)
plt.ylabel("Count", fontsize=12, fontweight='bold', labelpad=15)
plt.tight_layout()
plt.show()