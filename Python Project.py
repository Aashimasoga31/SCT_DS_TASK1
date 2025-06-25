import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
df = pd.read_csv("D:/New folder (3)/covid_vaccine_statewise.csv")
print(df.info(), "\n")

# Keep only needed columns
cols = [
    'State', 'Male(Individuals Vaccinated)', 'Female(Individuals Vaccinated)', 'Transgender(Individuals Vaccinated)',
    '18-44 Years(Individuals Vaccinated)', '45-60 Years(Individuals Vaccinated)', '60+ Years(Individuals Vaccinated)'
]

df = df[cols]
df.dropna(subset=['State'], inplace=True)
df.fillna(0, inplace=True)

# Convert to integers for better readability
df[cols[1:]] = df[cols[1:]].astype(int)

# Group by state
df_grouped = df.groupby("State").sum()

plt.style.use("dark_background")
sns.set_palette("rocket")
print(df.columns.tolist())

# Age-wise bar chart
df_grouped[['18-44 Years(Individuals Vaccinated)', '45-60 Years(Individuals Vaccinated)', '60+ Years(Individuals Vaccinated)']].plot(
    kind='bar', figsize=(15, 6), stacked=True
)
plt.title("Age-wise COVID-19 Vaccinations by State", fontsize=14)
plt.xlabel("State")
plt.ylabel("Total Vaccinations")
plt.xticks(rotation=90)
plt.tight_layout()
plt.grid(True, linestyle='--', alpha=0.4)
plt.show()

# Histogram Chart

plt.figure(figsize=(10, 5))
sns.histplot(df_grouped['Male(Individuals Vaccinated)'], kde=True, bins=15, label='Male', color='skyblue')
sns.histplot(df_grouped['Female(Individuals Vaccinated)'], kde=True, bins=15, label='Female', color='pink')
sns.histplot(df_grouped['Transgender(Individuals Vaccinated)'], kde=True, bins=15, label='Transgender', color='violet')
plt.title("Histogram of Vaccinations by Gender")
plt.xlabel("Vaccination Count")
plt.ylabel("State Frequency")
plt.legend()
plt.tight_layout()
plt.show()


