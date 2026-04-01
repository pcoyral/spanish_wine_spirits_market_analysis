# Spanish Wine & Spirits Market Analysis

> Quantitative analysis of the Spanish Wine & Spirits market combining time series forecasting, Monte Carlo simulation, and LVMH competitive benchmarking

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

## 📊 Project Overview

This project provides a comprehensive quantitative analysis of the Spanish Wine & Spirits (W&S) market, focusing on:

- **Time Series Analysis**: Production, consumption, and export trends (2011-2024)
- **Monte Carlo Simulation**: Risk assessment for market scenarios (2025-2030)
- **LVMH Competitive Analysis**: Benchmarking premium positioning strategies
- **Recommendation System**: Wine pairing and consumer preference modeling
- **Strategic Insights**: Data-driven recommendations for market players

### Key Research Questions

1. How will supply-demand imbalances evolve in the Spanish wine market through 2030?
2. What are the optimal pricing and positioning strategies for premium vs. mass market segments?
3. How does LVMH's W&S portfolio perform relative to the broader Spanish market?
4. What are the risk-adjusted returns for different export market strategies?
5. Can we predict wine quality and prices using product characteristics and reviews?

## 🎯 Business Context

Spain is the **world's 3rd largest wine producer** (28.3M hectoliters in 2023) but faces significant challenges:
- **Oversupply**: Production exceeds domestic demand
- **Shifting preferences**: Consumers moving toward lighter, premium wines
- **Export dependency**: Critical for market balance
- **Climate volatility**: Production uncertainty

**LVMH Context**: As a leading luxury conglomerate, understanding LVMH's positioning in the Spanish W&S market provides insights into premium segment strategies and luxury brand resilience.

## 📁 Project Structure

```
spanish-wine-analysis/
├── README.md
├── requirements.txt
├── .gitignore
├── data/
│   ├── raw/                    # Original datasets
│   ├── processed/              # Cleaned, merged data
│   └── external/               # USDA reports, OIV data
├── notebooks/
│   ├── 01_data_collection.ipynb
│   ├── 02_eda_kaggle_dataset.ipynb
│   ├── 03_eda_oiv_timeseries.ipynb
│   ├── 04_timeseries_forecasting.ipynb
│   ├── 05_monte_carlo_simulation.ipynb
│   ├── 06_lvmh_competitive_analysis.ipynb
│   ├── 07_price_quality_prediction.ipynb
│   └── 08_recommendation_system.ipynb
├── src/
│   ├── __init__.py
│   ├── data_processing.py      # Data cleaning and transformation
│   ├── visualization.py        # Custom plotting functions
│   ├── timeseries_models.py    # ARIMA, VAR, Prophet models
│   ├── monte_carlo.py          # Simulation framework
│   ├── ml_models.py            # Prediction and clustering
│   └── utils.py                # Helper functions
├── reports/
│   ├── figures/                # Generated charts and graphs
│   ├── executive_summary.md
│   └── technical_report.pdf
└── tests/                      # Unit tests (optional)
```

## 🔧 Installation & Setup

### Prerequisites
- Python 3.8 or higher
- Git
- Jupyter Notebook or JupyterLab

### Clone the Repository
```bash
git clone https://github.com/YOUR_USERNAME/spanish-wine-analysis.git
cd spanish-wine-analysis
```

### Create Virtual Environment
```bash
# Using venv
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Or using conda
conda create -n wine-analysis python=3.8
conda activate wine-analysis
```

### Install Dependencies
```bash
pip install -r requirements.txt
```

### Launch Jupyter
```bash
jupyter lab
# or
jupyter notebook
```

## 📊 Data Sources

### Primary Datasets

1. **Kaggle - Spanish Wine Quality Dataset**
   - **Source**: [Kaggle Dataset](https://www.kaggle.com/datasets/fedesoriano/spanish-wine-quality-dataset)
   - **Coverage**: Product-level wine data with ratings, prices, regions, varieties
   - **Use**: Price prediction, quality modeling, recommendation system

2. **OIV (International Organisation of Vine and Wine)**
   - **Source**: [OIV Statistics](https://www.oiv.int/what-we-do/statistics)
   - **Coverage**: Production, consumption, trade data (2011-2023)
   - **Use**: Time series analysis, market trends

3. **USDA Foreign Agricultural Service**
   - **Source**: Spain Wine Sector Reports
   - **Coverage**: Industry analysis, export data, policy context
   - **Use**: Market intelligence, validation

### LVMH-Specific Data
- Company annual reports
- Brand portfolio analysis
- Market positioning data
- Premium segment benchmarks

## 🚀 Methodology

### 1. Time Series Analysis
- **ARIMA/SARIMA**: Univariate forecasting for production and consumption
- **VAR (Vector Autoregression)**: Multi-variable relationships (production ↔ exports ↔ prices)
- **Prophet**: Trend decomposition with seasonality and structural breaks (COVID-19 impact)

### 2. Monte Carlo Simulation
- **Export Revenue Scenarios**: 10,000 simulations with stochastic variables
- **Market Entry Analysis**: NPV distributions for new ventures
- **Portfolio Optimization**: Risk-adjusted product mix strategies

### 3. Machine Learning
- **Regression**: Price and quality prediction (Random Forest, XGBoost)
- **Clustering**: Market segmentation (K-means, hierarchical)
- **NLP**: Sentiment analysis on wine reviews
- **Recommendation System**: Collaborative filtering + content-based

### 4. LVMH Competitive Analysis
- Comparative pricing analysis (premium positioning)
- Distribution channel effectiveness (HRI vs retail)
- Export market strategies (luxury vs mass market)
- Resilience metrics (COVID-19 performance)

## 📈 Key Findings

*(To be updated as analysis progresses)*

### Time Series Insights
- [ ] Production trends and forecasts (2025-2030)
- [ ] Consumption patterns and demand drivers
- [ ] Export market dynamics

### Monte Carlo Results
- [ ] Revenue forecasts with confidence intervals
- [ ] Risk assessment for oversupply scenarios
- [ ] Optimal market entry strategies

### LVMH Benchmarking
- [ ] Price premium quantification
- [ ] Market share in luxury segment
- [ ] Strategic positioning recommendations

### Predictive Models
- [ ] Price prediction accuracy (R² score)
- [ ] Quality score modeling
- [ ] Recommendation system performance

## 🎨 Visualizations

Key visualizations include:
- Interactive time series dashboards (Plotly)
- Monte Carlo probability distributions
- Geographic heat maps of production/consumption
- LVMH vs market comparison charts
- Correlation matrices and feature importance

## 🤝 Contributing

This is an academic/portfolio project, but suggestions and feedback are welcome!

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/analysis-improvement`)
3. Commit changes (`git commit -m 'Add new analysis'`)
4. Push to branch (`git push origin feature/analysis-improvement`)
5. Open a Pull Request

## 📚 References

- OIV Statistical Reports (2011-2023)
- USDA Foreign Agricultural Service - Spain Wine Sector Outlook 2024
- Spanish Wine Market Observatory (OEMV)
- Kaggle Spanish Wine Quality Dataset
- LVMH Annual Reports and Investor Relations

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 👤 Author

**[Your Name]**
- IE University - [Program Name]
- LinkedIn: [Your Profile]
- Email: [Your Email]

## 🙏 Acknowledgments

- IE University faculty for guidance
- Kaggle community for dataset curation
- OIV for comprehensive industry statistics
- USDA FAS for market intelligence reports

---

**Project Status**: 🚧 In Development

Last Updated: April 2026
