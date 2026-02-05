## EGFR IC50 Bioactivity Analysis

A Drug Discovery Mini-Project

## Overview

This project analyzes bioactivity data for compounds tested against the Epidermal Growth Factor Receptor (EGFR) using publicly available data from the ChEMBL database. EGFR is a clinically important target in oncology, and IC50 values are commonly used to quantify compound potency in early-stage drug discovery.

The objective of this project is to demonstrate practical skills in bioactivity data cleaning, analysis, visualization, and pharmacological interpretation using Python.

## Dataset

- Source: ChEMBL (public bioactivity database)

- Target: Epidermal Growth Factor Receptor (EGFR)

- Bioactivity Metric: IC50 (nM)

- Description:
The dataset contains IC50 measurements for multiple compounds tested against EGFR. Some compounds have multiple measurements from different experimental assays.

A filtered subset of the dataset is used for this project to ensure reproducibility and comply with GitHub file size limits.

## Methods

 1. Loaded and inspected raw ChEMBL bioactivity data using pandas

2.  Cleaned IC50 values by:

- Removing missing and non-numeric entries

- Excluding negative IC50 values (biologically implausible)

3. Aggregated multiple measurements by computing mean IC50 per compound

4. Visualized:

- Overall IC50 distribution using a histogram

- IC50 trends for the most potent compounds

5. Saved cleaned datasets and plots for reproducibility

## Key Findings

- Compounds with lower mean IC50 values exhibit higher inhibitory potency against EGFR

- Several compounds display sub-micromolar to nanomolar IC50 values, indicating strong bioactivity

- Aggregating IC50 values across multiple assays improves confidence in compound potency assessment

These steps reflect standard workflows used in early-stage anticancer drug discovery.

## Relevance to Drug Discovery

This project demonstrates essential skills used in pharmaceutical and biomedical research, including:

- Handling real-world bioactivity datasets

- Interpreting pharmacological potency metrics

- Performing data-driven comparisons of candidate compounds

The workflow and analysis are directly relevant to drug discovery, pharmacology, and applied biomedicine training.

## Tools & Skills

- Python

- pandas

- matplotlib

- Bioactivity data analysis

- Drug discovery fundamentals

## How To Run
python egfr_ic50_analysis.py

## Future Work

- Compare EGFR bioactivity with other kinase targets

- Extend analysis using log-transformed IC50 (pIC50)

- Integrate SQL-based querying of bioactivity datasets
