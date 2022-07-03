import matplotlib.pyplot as plt
from numpy import NaN
import pandas as pd
import pycountry
# Read "joined_recs_freeze_march.xlsx" with Pandas
df = pd.read_excel('joined_recs_freeze_march.xlsx', sheet_name='Sheet1')

# Filter out Offtopic papers
df = df[df.Offtopic == "No"]

# Journals at least in right dataset (right_only and both) can use directly the "Correspondence address" to extract country
df["Correspondence Address"]

for country in pycountry.countries:
    for address in df["Correspondence Address"]:
        if !address.isna():
            if country.name in address:
                print(country.name)



# Journals which are only in left dataset (left_only) need to use another thing.... they are only 4!




# We take the journals from the left data set and only add on top those which are in "right_only"
journal_left = df['Source Title'].value_counts()
journal_right = df.loc[df['_merge'] == "right_only"]['Source title'].value_counts()
journals = journal_right.add(journal_left, fill_value=0).astype("int").sort_values(ascending=False)

# Adding results from duplicate journals
pub_MM = journals["MICROPROCESSORS AND MICROSYSTEMS"] + journals["Microprocessors and Microsystems"]
journals["Microprocessors and Microsystems"] = pub_MM
journals = journals.drop("MICROPROCESSORS AND MICROSYSTEMS")

# Adding results from duplicate journals
pub_IEEEAccess = journals["IEEE Access"] + journals["IEEE ACCESS"]
journals["IEEE Access"] = pub_IEEEAccess
journals = journals.drop("IEEE ACCESS")

# Adding results from duplicate journals
pub_Electronics = journals["ELECTRONICS"] + journals["Electronics (Switzerland)"]
journals["Electronics (Switzerland)"] = pub_Electronics
journals = journals.drop("ELECTRONICS")

# Adding results from duplicate journals
pub_Sensors = journals["Sensors (Switzerland)"] + journals["Sensors"]
journals["Sensors (Switzerland)"] = pub_Sensors
journals = journals.drop("Sensors")

# Adding rest
pub_others = journals.sum() - (journals["Sensors (Switzerland)"] + journals["Electronics (Switzerland)"] + journals["IEEE Access"] + journals["Microprocessors and Microsystems"])
journals["Others"] = pub_others

journals = journals[["IEEE Access","Microprocessors and Microsystems","Electronics (Switzerland)","Applied Sciences (Switzerland)","Sensors (Switzerland)","ACM Journal on Emerging Technologies in Computing Systems", "JOURNAL OF CIRCUITS SYSTEMS AND COMPUTERS", "ACM TRANSACTIONS ON EMBEDDED COMPUTING SYSTEMS", "Others"]]

pubs = ["ACM Transactions on\nEmbedded Computing Systems","Journal of Circuits\nSystems and Computers","ACM Journal on Emerging\nTechnologies in\nComputing Systems","Sensors","Applied Sciences","Electronics","Microprocessors\nand Microsystems","IEEE Access", "Others"]

# Resorting journals one more time
journals = journals.sort_values()

plt.barh(pubs, journals)
plt.ylabel('Journal title')
plt.xlabel('Number of articles published')
#plt.show()
plt.tight_layout()
plt.savefig('figures/journal.pdf')