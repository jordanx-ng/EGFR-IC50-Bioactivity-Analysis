import pandas as pd
import matplotlib.pyplot as plt
import os

#lets create a plots folder if it doesnt exist
if not os.path.exists("plots"):
    os.makedirs("plots")

# ---------------------------
# STEP 1: Load the CSV
# ---------------------------
# I want to prevent dtype warnings
df = pd.read_csv("EGFR_IC50_ChEMBL.csv", sep=';', low_memory=False)
df = df.rename(columns={"Value": "IC50"}) #rename value to IC50 for clarity


# Strip column names of extra spaces
df.columns = df.columns.str.strip()



# ---------------------------
# STEP 2: Clean IC50 values
# ---------------------------
df = df.dropna(subset=["IC50"])   # removes rows where the IC50 value is missing.
df["IC50"] = pd.to_numeric(df["IC50"], errors="coerce") #converts IC50 to numbers
df = df.dropna(subset=["IC50"])               # drop non-numeric
print(f"Number of valid IC50 entries: {len(df)}\n")
# This is because i learned that in drug discovery, you cant calculate or plot IC50 if the value is missing or in text
df = df[df["IC50"] > 0]  # removes rows where IC50 is less than or equal to zero
# IC50 values must be positive, as they represent concentration
print(f"Number of valid positive IC50 entries: {len(df)}\n")

# ---------------------------
# STEP 3: Summary statistics
# ---------------------------
# describe() gives count, mean, std, min, max, quartiles of IC50 values
# I do this so it tells us how potent compounds are on average, and the range of potencies

print("Summary statistics for IC50 (nM):")
print(df["IC50"].describe(), "\n")

# ---------------------------
# STEP 4 : Compute mean IC50 per compound
# ---------------------------
mean_value_per_compound = df.groupby("Molecule ChEMBL ID")["IC50"].mean()
print("Top 10 compounds by mean IC50 (nM):")
print(mean_value_per_compound.sort_values().head(10), "\n") #just shows the first 10 compounds mean IC50 values for visualisation
# top 10 compounds with lowest mean IC50 values since its in ascending order, potency is highest to lowest

# ---------------------------
# STEP 5: Count measurements per compound 
# ---------------------------
compound_counts = df.groupby("Molecule ChEMBL ID")["IC50"].count()
print("Number of IC50 measurements per compound (top 10):")
print(compound_counts.sort_values(ascending=False).head(10), "\n")

# ---------------------------
# STEP 6: Plot IC50 distribution histogram
# ---------------------------
plt.figure(figsize=(8,5))
plt.hist(df["IC50"], bins=50, color="skyblue", edgecolor="black")
plt.xlabel("IC50 (nM)")
plt.ylabel("Number of Compounds")
plt.title("EGFR IC50 Distribution")
plt.tight_layout()
plt.savefig("plots/EGFR_IC50_hist.png", dpi=300)
plt.show()

# ---------------------------
# STEP 7: Top 5 compounds trend plot
# ---------------------------
top5 = mean_value_per_compound.nsmallest(5).index # get top 5 compounds with lowest mean IC50(most potently) .index gets the 5 compound IDs, top 5 is the list of the top 5 compound IDs
df_top5 = df[df["Molecule ChEMBL ID"].isin(top5)]

plt.figure(figsize=(8,5))

for compound in top5:
    values = df_top5[df_top5["Molecule ChEMBL ID"] == compound]["IC50"]
    plt.scatter([compound] * len(values), values)

plt.yscale("log")
plt.ylabel("IC50 (nM, log scale)")
plt.xlabel("Compound")
plt.title("Top 5 EGFR Compounds IC50 Trend")
plt.tight_layout()
plt.savefig("plots/top5_ic50_trend.png", dpi=300)
plt.show()

# ---------------------------
# STEP 8: Save cleaned CSV
# ---------------------------
df.to_csv("EGFR_IC50_cleaned.csv", index=False)
print("Cleaned dataset saved as 'EGFR_IC50_cleaned.csv'")