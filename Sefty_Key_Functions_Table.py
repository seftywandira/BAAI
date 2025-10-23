import pandas as pd
import matplotlib.pyplot as plt

# Data untuk tabel
data = {
    "Function": [
        "pd.read_csv()",
        "df.head()",
        "df.info()",
        "df.describe()",
        "df.isnull().sum()",
        "df.corr()",
        "sns.heatmap()",
        "stats.pearsonr()"
    ],
    "Purpose": [
        "Load CSV data into DataFrame",
        "Display first n rows",
        "Get dataset information",
        "Calculate summary statistics",
        "Count missing values",
        "Calculate correlation matrix",
        "Visualize correlation matrix",
        "Calculate Pearson correlation"
    ]
}

# Membuat DataFrame
df = pd.DataFrame(data)

# Membuat figure dan axis
fig, ax = plt.subplots(figsize=(8, 3))
ax.axis('off')

# Membuat tabel
table = ax.table(cellText=df.values, colLabels=df.columns, cellLoc='left', loc='center')

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

# Simpan sebagai file PNG
plt.savefig("key_functions_table.png", bbox_inches='tight', dpi=300)
plt.show()
