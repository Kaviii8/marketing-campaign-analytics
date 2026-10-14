# Marketing Campaign Analytics & Conversion Prediction

### End-to-End Data Analytics | Python • SQL • Machine Learning • Power BI

An end-to-end data analytics project that transforms digital advertising data into actionable marketing insights through data preprocessing, SQL-based performance analysis, machine learning, and interactive Power BI visualization.

The project evaluates advertising effectiveness, identifies cost-efficient campaigns and audience segments, and explores predictive modeling for advertising conversion outcomes.

## Project Overview

This project analyzes **1,143 Facebook advertising records** from the Sales Conversion Optimization dataset.

The primary objectives are to:

- Evaluate marketing campaign performance using key performance indicators (KPIs).
- Analyze advertising spend, impressions, clicks, leads, and approved conversions.
- Identify cost-efficient campaigns and audience segments.
- Build machine learning models to predict ad-level conversion outcomes.
- Develop an interactive Power BI dashboard for business decision-making.

## Technology Stack

| Category | Technologies |
|---|---|
| Programming | Python |
| Data Processing | Pandas, NumPy |
| Database & Querying | SQLite, SQL |
| Machine Learning | Scikit-learn |
| Data Visualization | Power BI, DAX |
| Development | VS Code, Git, GitHub |

## Project Workflow

**1. Data Collection → 2. Data Cleaning → 3. SQL Analysis → 4. Machine Learning → 5. Power BI Dashboard → 6. Business Insights**

### 1. Data Cleaning & Feature Engineering

Cleaned and validated the dataset using Python and Pandas.

- Analyzed 1,143 advertising records.
- Checked missing values, duplicates, and invalid values.
- Standardized column names and data types.
- Engineered additional performance metrics.

**Engineered features:**

- Click-Through Rate (CTR)
- Cost Per Click (CPC)
- Lead Conversion Rate
- Cost Per Approved Conversion
- Binary Conversion Outcome

### 2. SQL-Based Campaign Analysis

Used SQLite and SQL queries to evaluate marketing performance across campaigns and audience segments.

Analysis included:

- Overall campaign performance
- Advertising spend and conversion efficiency
- Campaign-level comparisons
- Age-based audience performance
- Gender-based conversion analysis

### 3. Marketing Performance Analysis

**Overall Marketing Performance**

| Metric | Value |
|---|---:|
| Advertising Records | 1,143 |
| Total Impressions | 213,434,828 |
| Total Clicks | 38,165 |
| Total Advertising Spend | 58,705.23 |
| Total Leads | 3,264 |
| Approved Conversions | 1,079 |
| Cost Per Approved Conversion | 54.41 |

*Monetary values are reported in the dataset's spending units; a currency is not specified.*

**Campaign Performance**

| Campaign ID | Spend | Approved Conversions | Cost / Conversion |
|---|---:|---:|---:|
| 916 | 149.71 | 24 | 6.24 |
| 936 | 2,893.37 | 183 | 15.81 |
| 1178 | 55,662.15 | 872 | 63.83 |

**Key findings:**

- Campaign **916** achieved the lowest observed cost per conversion.
- Campaign **1178** generated the highest number of approved conversions.
- Campaign **936** offered a lower cost per conversion than Campaign 1178.
- The **30–34 age segment** demonstrated the lowest observed acquisition cost among the age groups analyzed.

These findings describe historical performance and do not establish the causal effect of changing campaign budgets or targeting.

## Machine Learning — Conversion Prediction

Developed classification models to predict whether an advertisement records at least one approved conversion.

**Target variable:** `has_approved_conversion`

**Predictor variables:**

- Campaign ID
- Age group
- Gender
- Interest category

**Models evaluated:**

- Dummy Classifier (baseline)
- Logistic Regression
- Random Forest Classifier

### Model Evaluation

| Model | Accuracy | F1 Score | ROC-AUC |
|---|---:|---:|---:|
| Dummy Classifier | 51.09% | 0.6763 | 0.5000 |
| Logistic Regression | 58.08% | 0.5932 | 0.6074 |
| Random Forest | 59.83% | 0.6102 | 0.5962 |

**Selected model:** Logistic Regression, based on ROC-AUC.

The models demonstrate modest predictive performance. This component is an exploratory classification exercise rather than a production-ready forecasting system.

## Power BI Dashboard

Developed an interactive Power BI dashboard to communicate marketing performance and audience insights.

**Dashboard components:**

- Total Advertising Spend
- Total Leads
- Approved Conversions
- Cost Per Conversion
- Campaign Performance Comparison
- Age-Based Conversion Analysis
- Gender-Based Conversion Distribution
- Interest-Based Advertising Efficiency
- Campaign Performance Summary

**Dashboard Preview**

Add your exported Power BI dashboard screenshot here:

`![Marketing Campaign Dashboard](dashboard/dashboard_preview.png)`

The preview will appear once the image is saved at that location in the repository.

## Business Insights & Recommendations

**1. Campaign Efficiency**

Campaign 916 achieved the lowest cost per approved conversion, although its conversion volume was relatively small.

*Recommendation:* Evaluate whether its efficiency can be maintained at a larger scale through controlled experimentation.

**2. Advertising Budget Allocation**

Campaign 1178 generated the most conversions but required substantially higher advertising expenditure.

*Recommendation:* Investigate its targeting and acquisition efficiency before making budget allocation decisions.

**3. Audience Targeting**

The 30–34 age group recorded the lowest observed cost per conversion.

*Recommendation:* Test audience-specific campaigns to determine whether the observed efficiency is repeatable.

**4. Predictive Analytics**

Logistic Regression demonstrated limited but above-random discrimination based on ROC-AUC.

*Recommendation:* Explore richer behavioral features, additional training data, and more robust model validation.

## Dataset

**Source:** [Sales Conversion Optimization — Kaggle](https://www.kaggle.com/loveall/clicks-conversion-tracking)

The dataset includes advertising impressions, clicks, spend, leads, approved conversions, and audience characteristics.

**Limitations:**

- Revenue data is unavailable; actual ROI and ROAS cannot be calculated.
- No timestamp field is available for reliable time-series forecasting.
- Records are aggregated at advertisement level rather than individual customer level.
- Observational comparisons do not demonstrate causal campaign effectiveness.

## Future Enhancements

- Integrate Google Analytics 4 campaign and website engagement data.
- Implement cross-validation and separate model-selection and test datasets.
- Explore additional audience and campaign features.
- Build conversion forecasting using timestamped marketing data.
- Introduce automated campaign performance reporting.

## Author

**Kavindi Liyanage**

Computer Science Graduate | Data Analytics | Machine Learning | Business Intelligence

[GitHub Profile](https://github.com/Kaviii8)

---

*This project demonstrates an end-to-end analytics workflow, from raw advertising data to SQL analysis, predictive modeling, interactive dashboards, and business recommendations.*