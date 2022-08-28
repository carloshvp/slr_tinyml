import matplotlib.pyplot as plt
import pandas as pd
# Read "joined_recs_freeze_march.xlsx" with Pandas
df = pd.read_excel('joined_recs_freeze_march.xlsx', sheet_name='Sheet1')

# Filter out Offtopic papers
df = df[df.Offtopic == "No"]

# Extract the countries of publication and count them
countries = df["Country"].value_counts()

countries.plot.bar()
plt.xlabel('Countries of publication')
plt.ylabel('Number of articles published')

#plt.show()
plt.tight_layout()

plt.savefig('figures/country.pdf')