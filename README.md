EGFR IC50 Bioactivity Analysis (Drug Discovery Mini-Project)
Overview

This project analyzes bioactivity data for compounds tested against the Epidermal Growth Factor Receptor (EGFR) using publicly available ChEMBL data. EGFR is a clinically important target in oncology, and IC50 measurements are commonly used to assess compound potency in early-stage drug discovery.

The goal of this project is to demonstrate practical skills in bioactivity data cleaning, analysis, visualization, and pharmacological interpretation using Python.

Dataset

Source: ChEMBL database (public bioactivity data)

Target: EGFR (Epidermal Growth Factor Receptor)

Bioactivity metric: IC50 values (nM)

Dataset includes multiple IC50 measurements per compound from different experimental assays

For portfolio and GitHub size constraints, a filtered subset of the dataset is used.

Methods

Loaded and inspected raw ChEMBL bioactivity data using pandas

Cleaned IC50 values by:

Removing missing and non-numeric entries

Excluding negative IC50 values (biologically implausible)

Computed mean IC50 per compound to account for repeated experimental measurements

Visualized:

Overall IC50 distribution using a histogram

IC50 trends for the most potent compounds

Saved cleaned datasets and plots for reproducibility

Key Findings & Interpretation

Compounds with lower IC50 values exhibit higher inhibitory potency against EGFR

Several compounds display sub-micromolar to nanomolar IC50 values, indicating strong activity

Aggregating multiple IC50 measurements per compound improves confidence in potency comparisons

These analyses reflect standard workflows used in early-stage anticancer drug discovery.

Relevance to Drug Discovery & MSc Training

This project demonstrates:

Practical handling of real-world bioactivity datasets

Understanding of pharmacological potency metrics (IC50)

Data-driven reasoning applied to therapeutic target evaluation

These skills are directly relevant to Applied Biomedicine, Drug Discovery, Pharmacology, and Translational Research modules at the MSc level.

Tools & Skills

Python

pandas

matplotlib

Bioactivity data analysis

Drug discovery fundamentals
## How to Run

```bash
python analysis.py
