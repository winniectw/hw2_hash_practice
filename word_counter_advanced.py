import os
import plotly.graph_objects as go

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

fig = go.Figure(data=[
    go.Bar(
        x=x_labels,
        y=y_values,
        hovertemplate='Word: %{x}<br>Count: %{y}<extra></extra>'
    )
])

fig.update_layout(
    plot_bgcolor='white',
    title=dict(
        text='Word Frequency',
        x=0.5,
        xanchor='center',
        font=dict(size=24, family='Arial Black', color='black')
    ),
    xaxis=dict(
        title=dict(
            text='Word',
            font=dict(size=18, family='Arial Black', color='black')
        ),
        tickfont=dict(size=14, family='Arial'),
    ),
    yaxis=dict(
        title=dict(
            text='Count',
            font=dict(size=18, family='Arial Black', color='black')
        ),
        tickfont=dict(size=14, family='Arial'),
        gridcolor='black',
        zeroline=True,
        zerolinecolor='black'
    ),
    dragmode='pan',
    autosize=True
)

fig.show(config={
    'scrollZoom': True,
    'displaylogo': False})