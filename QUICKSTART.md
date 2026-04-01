# Quick Start Guide

## 🚀 Getting Started with Spanish Wine & Spirits Analysis

This guide will help you set up the project and begin your analysis in under 30 minutes.

---

## Step 1: Clone the Repository (After Creating It)

```bash
git clone https://github.com/YOUR_USERNAME/spanish-wine-analysis.git
cd spanish-wine-analysis
```

---

## Step 2: Set Up Python Environment

### Option A: Using venv (Recommended for beginners)
```bash
# Create virtual environment
python -m venv venv

# Activate it
# On Mac/Linux:
source venv/bin/activate
# On Windows:
venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

### Option B: Using Conda
```bash
conda create -n wine-analysis python=3.8
conda activate wine-analysis
pip install -r requirements.txt
```

---

## Step 3: Set Up Kaggle API (for Data Download)

1. **Create Kaggle Account**: Go to [kaggle.com](https://www.kaggle.com)

2. **Get API Token**:
   - Go to Account Settings → API
   - Click "Create New API Token"
   - This downloads `kaggle.json`

3. **Install Token**:
   ```bash
   # Mac/Linux
   mkdir -p ~/.kaggle
   mv ~/Downloads/kaggle.json ~/.kaggle/
   chmod 600 ~/.kaggle/kaggle.json
   
   # Windows
   mkdir %USERPROFILE%\.kaggle
   move %USERPROFILE%\Downloads\kaggle.json %USERPROFILE%\.kaggle\kaggle.json
   ```

---

## Step 4: Run First Notebook

```bash
# Launch Jupyter
jupyter lab

# Open: notebooks/01_data_collection.ipynb
# Run all cells (Shift + Enter)
```

This will:
- Download the Kaggle Spanish Wine dataset
- Create necessary directory structure
- Download USDA reports
- Provide OIV data template

---

## Step 5: Google Colab Alternative (No Setup Required!)

If you prefer Colab:

1. **Upload project to Google Drive**
2. **Open Colab**: [colab.research.google.com](https://colab.research.google.com)
3. **Mount Google Drive**:
   ```python
   from google.colab import drive
   drive.mount('/content/drive')
   ```
4. **Navigate to project**:
   ```python
   %cd /content/drive/MyDrive/spanish-wine-analysis
   ```
5. **Install requirements**:
   ```python
   !pip install -r requirements.txt
   ```

---

## Step 6: Connect GitHub to Colab

**Best of both worlds**: Use Colab for compute, GitHub for version control

1. **In Colab, connect to GitHub**:
   - File → Open Notebook → GitHub tab
   - Enter: `YOUR_USERNAME/spanish-wine-analysis`
   - Open any notebook

2. **Save changes back to GitHub**:
   - File → Save a copy in GitHub
   - This commits directly to your repo!

---

## Project Workflow

```
Week 1: Data Foundation
├── 01_data_collection.ipynb ✓
├── 02_eda_kaggle_dataset.ipynb
└── 03_eda_oiv_timeseries.ipynb

Week 2: Time Series Analysis
├── 04_timeseries_forecasting.ipynb
└── Production/Consumption/Export forecasts

Week 3: Monte Carlo Simulation
├── 05_monte_carlo_simulation.ipynb
└── Risk scenarios & portfolio optimization

Week 4: LVMH Analysis
├── 06_lvmh_competitive_analysis.ipynb
└── Premium positioning insights

Week 5: Advanced Analytics
├── 07_price_quality_prediction.ipynb
├── 08_recommendation_system.ipynb
└── Final report synthesis
```

---

## Common Issues & Solutions

### Issue 1: Kaggle API Not Working
**Solution**:
```bash
# Check token location
ls ~/.kaggle/kaggle.json

# If missing, re-download from Kaggle and move to correct location
```

### Issue 2: Import Errors
**Solution**:
```bash
# Verify you're in the right environment
which python

# Should show: .../venv/bin/python or .../conda/envs/wine-analysis/bin/python

# Reinstall requirements
pip install -r requirements.txt --upgrade
```

### Issue 3: OIV Data Not Available
**Solution**:
- Manual download required (see notebook 01)
- Fill in the template: `data/external/oiv_spain_template.csv`
- Extract data from PDF reports if needed

### Issue 4: Jupyter Kernel Not Found
**Solution**:
```bash
# Install ipykernel in your environment
pip install ipykernel

# Add your environment to Jupyter
python -m ipykernel install --user --name=wine-analysis
```

---

## Key Files Overview

```
spanish-wine-analysis/
├── README.md                          # Main project documentation
├── QUICKSTART.md                      # This file!
├── requirements.txt                   # Python dependencies
├── notebooks/
│   └── 01_data_collection.ipynb      # Start here!
├── src/
│   └── lvmh_analysis.py              # LVMH competitive analysis utilities
└── data/
    ├── raw/                           # Kaggle dataset goes here
    └── external/                      # OIV & USDA data here
```

---

## Recommended Learning Path

### If you're new to data science:
1. Start with notebook 01 (data collection)
2. Move to notebook 02 (EDA - understand the data)
3. Focus on visualization and descriptive statistics
4. Build simple models first (linear regression)
5. Then advance to time series and Monte Carlo

### If you're experienced:
1. Run notebook 01 to get data
2. Skim notebook 02 for context
3. Jump to notebook 04 (time series) or 05 (Monte Carlo)
4. Customize analyses for your specific research questions
5. Focus on LVMH competitive analysis (notebook 06)

---

## Next Steps

After setup:

1. **Customize README.md**:
   - Add your name and links
   - Update project description if needed

2. **Create GitHub Issues** for tasks:
   - "Download OIV data"
   - "Build ARIMA model"
   - "LVMH brand data collection"

3. **Set Up Project Board** (optional):
   - GitHub Projects for task tracking
   - Columns: To Do, In Progress, Done

4. **Start Analysis**:
   - Run notebook 01
   - Explore the Kaggle dataset
   - Brainstorm specific research questions

---

## Getting Help

- **Documentation**: Check README.md and notebook markdown cells
- **Code Comments**: All functions have docstrings
- **Community**: Kaggle forums for dataset questions
- **Issues**: Create GitHub issues for bugs or questions

---

## Pro Tips

1. **Commit Often**: 
   ```bash
   git add .
   git commit -m "Completed data collection"
   git push
   ```

2. **Use Markdown Cells**: Document your thought process in notebooks

3. **Save Figures**: All visualizations should go to `reports/figures/`

4. **Version Your Data**: If you clean data, save to `data/processed/`

5. **Test on Small Samples**: Use `.head(1000)` while developing code

---

## Success Checklist

- [ ] Environment set up and tested
- [ ] Kaggle API configured
- [ ] Data downloaded successfully
- [ ] First notebook runs without errors
- [ ] Can create and save visualizations
- [ ] GitHub repository created and synced
- [ ] Project structure makes sense

---

## Ready to Start?

```bash
jupyter lab notebooks/01_data_collection.ipynb
```

**Let's build something amazing! 🍷📊**

---

Last Updated: April 2026
