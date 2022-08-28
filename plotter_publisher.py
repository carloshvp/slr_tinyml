import matplotlib.pyplot as plt
import pandas as pd
# Read "joined_recs_freeze_march.xlsx" with Pandas
df = pd.read_excel('joined_recs_freeze_march.xlsx', sheet_name='Sheet1')

# Filter out Offtopic papers
df = df[df.Offtopic == "No"]

# We take the publishers from the left data set and only add on top those which are in "right_only"
publisher_left = df['Publisher_x'].value_counts()
publisher_right = df.loc[df['_merge'] == "right_only"]['Publisher_y'].value_counts()
publishers = publisher_right.add(publisher_left, fill_value=0).astype("int").sort_values(ascending=False)

# Adding  "Institute of Electrical and Electronics Engineers Inc." to "IEEE-INST ELECTRICAL ELECTRONICS ENGINEERS INC"
pub_IEEE = publishers["Institute of Electrical and Electronics Engineers Inc."] + publishers["IEEE-INST ELECTRICAL ELECTRONICS ENGINEERS INC"] + publishers["IEEE Computer Society"] + publishers["IEEE COMPUTER SOC"]
publishers["Institute of Electrical and Electronics Engineers Inc."] = pub_IEEE
publishers = publishers.drop("IEEE-INST ELECTRICAL ELECTRONICS ENGINEERS INC")
publishers = publishers.drop("IEEE COMPUTER SOC")
publishers = publishers.drop("IEEE Computer Society")

# Adding  "MDPI AG" to "MDPI"
pub_MDPI = publishers["MDPI AG"] + publishers["MDPI"]
publishers["MDPI"] = pub_MDPI
publishers = publishers.drop("MDPI AG")

# Adding  "Elsevier B.V." to "ELSEVIER"
pub_Elsevier = publishers["Elsevier B.V."] + publishers["ELSEVIER"] + publishers["Elsevier Ltd"]
publishers["Elsevier B.V."] = pub_Elsevier
publishers = publishers.drop("ELSEVIER")
publishers = publishers.drop("Elsevier Ltd")

# Adding  "Association for Computing Machinery" to "ASSOC COMPUTING MACHINERY"
pub_ACM = publishers["Association for Computing Machinery"] + publishers["ASSOC COMPUTING MACHINERY"]
publishers["Association for Computing Machinery"] = pub_ACM
publishers = publishers.drop("ASSOC COMPUTING MACHINERY")

# Adding  "Springer" to "SPRINGER"
pub_Springer = publishers["Springer"] + publishers["SPRINGER HEIDELBERG"] + publishers["SPRINGERNATURE"] + publishers["Springer Science and Business Media Deutschland GmbH"]
publishers["Springer"] = pub_Springer
publishers = publishers.drop("SPRINGER HEIDELBERG")
publishers = publishers.drop("SPRINGERNATURE")
#publishers = publishers.drop("SPRINGER")
publishers = publishers.drop("Springer Science and Business Media Deutschland GmbH")

# Resorting publishers one more time
publishers = publishers.sort_values(ascending=False)

# Adding rest
pub_Others = publishers["WORLD SCIENTIFIC PUBL CO PTE LTD"] + publishers["Ismail Saritas"] + publishers["SAGE Publications Inc."] + publishers["TECH SCIENCE PRESS"] + publishers["KOREAN INST COMMUNICATIONS SCIENCES (K I C S)"]
publishers["Others"] = pub_Others
publishers = publishers.drop("WORLD SCIENTIFIC PUBL CO PTE LTD")
publishers = publishers.drop("Ismail Saritas")
publishers = publishers.drop("SAGE Publications Inc.")
publishers = publishers.drop("TECH SCIENCE PRESS")
publishers = publishers.drop("KOREAN INST COMMUNICATIONS SCIENCES (K I C S)")


pubs = ["IEEE", "MDPI", "Elsevier", "ACM", "Springer", "Others"]

print(publishers)

plt.bar(pubs, publishers)
plt.xlabel('Publishers')
plt.ylabel('Number of articles published')
yint = [0,5,10,15,20]
plt.yticks(yint)
#plt.show()
plt.savefig('figures/publishers_28082022.pdf')