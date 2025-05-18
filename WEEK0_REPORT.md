# Solar Challenge – Week 0 Interim Report


## ✅ Task 1: Git & Environment Setup

We completed a foundational setup for version control and team collaboration. This included:

- ✅ **Initialized GitHub repo**: `solar-challenge-week1`
- ✅ **Cloned locally**, created a Python virtual environment (`venv`)
- ✅ **Created and merged a feature branch**: `setup-task`
- ✅ **Made at least 3 commits**, including:
  - `init: add .gitignore`
  - `chore: venv setup`
  - `ci: add GitHub Actions workflow`
- ✅ **Configured `.gitignore`**:
  - Ignored `data/`, `*.csv`, `__pycache__/`, `.ipynb_checkpoints/`
- ✅ **Added GitHub Actions CI**:
  - `.github/workflows/ci.yml` installs dependencies from `requirements.txt`
  - Verifies Python installation (`python --version`)


---

## 🔍 Task 2: Profiling, Cleaning & EDA

We are performing **country-wise EDA** with the following standardized approach:

### ✅ EDA Branching
- Each country uses a separate branch:
  - `eda-togo`
  - `eda-sierraleone`
- EDA notebooks:
  - `togo_eda.ipynb`
  - `sierraleone_eda.ipynb`

### 🧪 Step-by-Step EDA Strategy

1. **Summary Statistics**:
   - `df.describe()` on all numeric fields.
   - Null checks using `df.isna().sum()`.
   - Highlighted any columns with >5% missing values.

2. **Cleaning**:
   - Handled outliers using Z-score: `|Z| > 3`.
   - Imputed missing values using **median**.
   - Dropped unusable or extremely corrupted rows.

3. **Time Series Analysis**:
   - Plotted GHI, DNI, DHI, Tamb over `Timestamp`
   - Downsampled data for visualization due to memory limits.

4. **Correlation & Relationships**:
   - Correlation heatmap for solar & climate features.
   - Scatter plots: `WS vs GHI`, `RH vs Tamb`
   - Bubble chart: `GHI vs Tamb` with bubble size = `RH`

5. **Exported Clean Data**:
   - Saved cleaned files to:
     - `data/togo-dapaong_clean.csv`
     - `data/sierraleone-bumbuna_clean.csv`
   - **Note**: Data files are excluded via `.gitignore`.

---

## 📦 Requirements
```bash
pandas
numpy
matplotlib
seaborn
scipy

