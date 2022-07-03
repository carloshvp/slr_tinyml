import matplotlib.pyplot as plt
import pandas as pd
# Read "joined_recs_freeze_march.xlsx" with Pandas
df = pd.read_excel('joined_recs_freeze_march.xlsx', sheet_name='Sheet1')

# Filter out Offtopic papers
df = df[df.Offtopic == "No"]

# Count publications per year in colunt "Year", which is used when _merge is anything than "left_only". Then sort
pub_year_right = df['Year'].value_counts().sort_index()

#Count publications per year where _merge is equal to "left_only"
pub_year_left = df.loc[df['_merge'] == "left_only"]['Publication Year'].value_counts()
#Set publications for 2017 and 2022 to zero and sort
pub_year_left = pub_year_left.append(pd.Series({2017:0, 2018:0, 2020:0, 2022:0})).sort_index()

#Add left and right publications
pub_year = pub_year_left + pub_year_right
#Extrapolate value of 2022 for complete year (otherwise only considered until March)
pub_year[2022] = pub_year[2022]*4

plt.plot(pub_year)
plt.xlabel('Year')
plt.ylabel('Number of articles published')
#plt.show()
plt.savefig('figures/pub_year.pdf')