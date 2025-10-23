import pandas as pd
import matplotlib.pyplot as plt

# Data untuk tabel
data = {
    "Coefficient Range": [
        "0.9 to 1.0",
        "0.7 to 0.9",
        "0.5 to 0.7",
        "0.3 to 0.5",
        "-0.3 to 0.3",
        "-0.5 to -0.3",
        "-0.7 to -0.5",
        "-0.9 to -0.7",
        "-1.0 to -0.9"
    ],
    "Interpretation": [
        "Very strong positive",
        "Strong positive",
        "Moderate positive",
        "Weak positive",
        "Little to no correlation",
        "Weak negative",
        "Moderate negative",
        "Strong negative",
        "Very strong negative"
    ]
}

# Membuat DataFrame
df = pd.DataFrame(data)

# Membuat figure dan axis
fig, ax = plt.subplots(figsize=(8, 3.5))
ax.axis('off')

# Membuat tabel
table = ax.table(cellText=df.values, colLabels=df.columns, cellLoc='center', loc='center')

# Gaya tampilan
table.auto_set_font_size(False)
table.set_fontsize(11)
table.scale(1, 1.5)

# Warna header dan baris
for (i, j), cell in table.get_celld().items():
    if i == 0:
        cell.set_text_props(weight='bold', color='white')
        cell.set_facecolor('#4472C4')
    elif i % 2 == 0:
        cell.set_facecolor('#D9E1F2')
    else:
        cell.set_facecolor('#FFFFFF')

# Tambahkan judul
plt.title("Correlation Coefficient Interpretation", fontsize=14, weight='bold', pad=15)

# Simpan sebagai file PNG
plt.savefig("correlation_coefficient_interpretation.png", bbox_inches='tight', dpi=300)
plt.show()
