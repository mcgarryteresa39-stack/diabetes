

# Project: Diabetes Prediction

# **Project Overview**

This project analyses 

## ** Table of Contents**

# **Business Problem Statement / Requirements**


# **Key Business Question:**
- Can survey questions from the BRFSS provide accurate predictions of whether an individual has diabetes?
- What risk factors are most predictive of diabetes risk?
- Can we use a subset of the risk factors to accurately predict whether an individual has diabetes?
- Can we create a short form of questions from the BRFSS using feature selection to accurately predict if someone might have diabetes or is at high risk of diabetes?


# **Dataset:**

About the Dataset
Context
Diabetes is among the most prevalent chronic diseases in the United States, impacting millions of Americans each year and exerting a significant financial burden on the economy. Diabetes is a serious chronic disease in which individuals lose the ability to effectively regulate levels of glucose in the blood, and can lead to reduced quality of life and life expectancy. After different foods are broken down into sugars during digestion, the sugars are then released into the bloodstream. This signals the pancreas to release insulin. Insulin helps enable cells within the body to use those sugars in the bloodstream for energy. Diabetes is generally characterized by either the body not making enough insulin or being unable to use the insulin that is made as effectively as needed.

Complications like heart disease, vision loss, lower-limb amputation, and kidney disease are associated with chronically high levels of sugar remaining in the bloodstream for those with diabetes. While there is no cure for diabetes, strategies like losing weight, eating healthily, being active, and receiving medical treatments can mitigate the harms of this disease in many patients. Early diagnosis can lead to lifestyle changes and more effective treatment, making predictive models for diabetes risk important tools for public and public health officials.

The scale of this problem is also important to recognize. The Centers for Disease Control and Prevention has indicated that as of 2018, 34.2 million Americans have diabetes and 88 million have prediabetes. Furthermore, the CDC estimates that 1 in 5 diabetics, and roughly 8 in 10 prediabetics are unaware of their risk. While there are different types of diabetes, type II diabetes is the most common form and its prevalence varies by age, education, income, location, race, and other social determinants of health. Much of the burden of the disease falls on those of lower socioeconomic status as well. Diabetes also places a massive burden on the economy, with diagnosed diabetes costs of roughly $327 billion dollars and total costs with undiagnosed diabetes and prediabetes approaching $400 billion dollars annually.

Content
The Behavioral Risk Factor Surveillance System (BRFSS) is a health-related telephone survey that is collected annually by the CDC. Each year, the survey collects responses from over 400,000 Americans on health-related risk behaviors, chronic health conditions, and the use of preventative services. It has been conducted every year since 1984. For this project, a csv of the dataset available on Kaggle for the year 2015 was used. This original dataset contains responses from 441,455 individuals and has 330 features. These features are either questions directly asked of participants, or calculated variables based on individual participant responses.

The dataset can be downloaded from here:
https://www.kaggle.com/datasets/alexteboul/diabetes-health-indicators-dataset?utm_source=copilot.com

This dataset contains 3 files:

- diabetes _ 012 _ health _ indicators _ BRFSS2015.csv is a clean dataset of 253,680 survey responses to the CDC's BRFSS2015. The target variable Diabetes_012 has 3 classes. 0 is for no diabetes or only during pregnancy, 1 is for prediabetes, and 2 is for diabetes. There is class imbalance in this dataset. This dataset has 21 feature variables

- diabetes _ binary _ 5050split _ health _ indicators _ BRFSS2015.csv is a clean dataset of 70,692 survey responses to the CDC's BRFSS2015. It has an equal 50-50 split of respondents with no diabetes and with either prediabetes or diabetes. The target variable Diabetes_binary has 2 classes. 0 is for no diabetes, and 1 is for prediabetes or diabetes. This dataset has 21 feature variables and is balanced.

- diabetes _ binary _ health _ indicators _ BRFSS2015.csv is a clean dataset of 253,680 survey responses to the CDC's BRFSS2015. The target variable Diabetes_binary has 2 classes. 0 is for no diabetes, and 1 is for prediabetes or diabetes. This dataset has 21 feature variables and is not balanced.

This project will look exclusively at the first dataset: diabetes _ 012 _ health _ indicators _ BRFSS2015.csv

## **Project Features**

1. **Data loading:** 

. 1 CSV dataset was downloaded and included in this project.

2. **Dataset Features**

All variables are numeric.

Feature	Question	Codes
Diabetes_012	Told by doctor you have diabetes	0=no, 1=pre‑diabetes, 2=diabetes
HighBP	Told you have high blood pressure	0=no, 1=yes
HighChol	Told cholesterol is high	0=no, 1=yes
CholCheck	Cholesterol checked in past 5 years	0=no, 1=yes
BMI	Body Mass Index	12–98; <18.5 underweight; 18.5–24.8 normal; 25–29.9 overweight; ≥30 obese
Smoker	Smoked ≥100 cigarettes in life	0=no, 1=yes
Stroke	Ever told you had a stroke	0=no, 1=yes
HeartDiseaseorAttack	Told you had CHD or heart attack	0=no, 1=yes
PhysActivity	Any physical activity in past month	0=no, 1=yes
Fruits	Eat fruit daily	0=no, 1=yes
Veggies	Eat vegetables daily	0=no, 1=yes
HvyAlcholConsump	Heavy drinking (men>14/wk, women>7/wk)	0=no, 1=yes
AnyHealthcare	Have any health coverage	0=no, 1=yes
NoDocbcCost	Needed doctor but cost prevented visit	0=no, 1=yes
GenHlth	General health rating	1=excellent, 2=very good, 3=good, 4=fair, 5=poor
MentHlth	Days mental health not good (0–30)	0–30
PhysHlth	Days physical health not good (0–30)	0–30
DiffWalk	Serious difficulty walking/climbing stairs	0=no, 1=yes
Sex	Biological sex	0=female, 1=male
Age	Age category	1=18–24, 2=25–29, 3=30–34, 4=35–39, 5=40–44, 6=45–49, 7=50–54, 8=55–59, 9=60–64, 10=65–69, 11=70–74, 12=75–79, 13=80+
Education	Highest education level	1=none/K, 2=grades 1–8, 3=grades 9–11, 4=HS/GED, 5=some college, 6=college grad
Income	Annual household income	1=<$10k, 2=$10–14.9k, 3=$15–19.9k, 4=$20–24.9k, 5=$25–34.9k, 6=$35–49.9k, 7=$50–74.9k, 8=≥$75k

2. **Data cleaning:** 
•	The dataset was clean.

3. **Statistical Analysis:** 

Statistical testing using corr, linear regression xxxxxxxxxx

6. **Visualisation:**: 

Genearting bar charts and histograms in both Python and PowerBi/Tableau

7. **Export:** 

Save analysis results in various formats including CSV, PPT, SQL, Word, Text, Jupyter Source File

# **Installation**

## **Prerequisites**
- Python 3.7 or higher: pandas, numpy, seaborn, matplotlib, scikit learn, statsmodels
- pip
- Trello: Project Management
- VS Code for development
- Power BI / Tableau for dashboarding
- GitHub for version control and portfolio presentation
- Data set: 7 CSV files

## **Screenshots of finished Dashboard**

# **Clone and deploy**

## **Hypotheses to Test and how to validate them**



## **Project Plan**

# **High level steps taken for analysis**
xxxxx

## How the data was managed throughout the collection, processing, nalaysis and interpretation steps


## ** Why the research emthodologies were chosen**


## Rationale to map the business requirements to the Data visualisations


## Analysis techniques used

# Data analysis methods used and their limitation/alternative approaches

# Did hte data limit and did I use an alternativ approach to meet these challenges

# The use of geneartive AI tools to help with ideation, design htinking and code optimisaiton

# **Ethical Considerations**



# **Data privacy, bias or fairness issues with the data**

## Any legal or societal issues


## **Executive Summary**
The key findings from this research are:
xx
xx
xx
xx


## **Dashboards**
List all dashboard pages and their content, either blocks of information or widgets, like buttons, checkboxes, images, or any other item that your dashboard library supports.
Later, during the project development, you may revisit your dashboard plan to update a given feature (for example, at the beginning of the project you were confident you would use a given plot to display an insight but subsequently you used another plot type).
How were data insights communicated to technical and non-technical audiences?
Explain how the dashboard was designed to communicate complex data insights to different audiences.

## **Demographics**


# **Deployment**

Heroku
The App live link is: https://YOUR_APP_NAME.herokuapp.com/
Set the runtime.txt Python version to a Heroku-20 stack currently supported version.
The project was deployed to Heroku using the following steps.
Log in to Heroku and create an App
From the Deploy tab, select GitHub as the deployment method.
Select your repository name and click Search. Once it is found, click Connect.
Select the branch you want to deploy, then click Deploy Branch.
The deployment process should happen smoothly if all deployment files are fully functional. Click now the button Open App on the top of the page to access your App.
If the slug size is too large then add large files not required for the app to the .slugignore file.
Main Data Analysis Libraries
Here you should list the libraries you used in the project and provide an example(s) of how you used these libraries.
Credits
In this section, you need to reference where you got your content, media and extra help from. It is common practice to use code from other repositories and tutorials, however, it is important to be very specific about these sources to avoid plagiarism.
You can break the credits section up into Content and Media, depending on what you have included in your project.
Content
The text for the Home page was taken from Wikipedia Article A
Instructions on how to implement form validation on the Sign-Up page was taken from Specific YouTube Tutorial
The icons in the footer were taken from Font Awesome
Media
The photos used on the home and sign-up page are from This Open-Source site
The images used for the gallery page were taken from this other open-source site
Acknowledgements (optional)
Thank the people who provided support through this project.

## **How to Reproduce**

1.	Clone this repository

2.	Install dependencies:
-		Code
		pip install -r requirements.txt

3.	Place OULAD raw CSVs into /data_raw

4.	Run notebooks in numerical order

5.	Open the dashboard file in Power BI/Tableau

Dashboard
🟨 4. Dashboard Narrative (What your dashboard should answer)
This is the story your visuals will tell.
✅ Page 1 — Overview
•	What is the overall pass/withdrawal rate?
•	Which demographic groups show the highest risk?
•	What are the key KPIs (avg score, avg engagement, withdrawal rate)?
✅ Page 2 — Engagement
•	How does engagement change over time?
•	Do pass/fail/withdraw groups show different patterns?
•	Which activity types drive the most engagement?
✅ Page 3 — Assessment Performance
•	How do scores vary by assessment type?
•	How does lateness affect performance?
•	Are early assessments predictive of final outcomes?
✅ Page 4 — Risk Indicators (Optional)
•	Which features correlate most with withdrawal?
•	Can we identify at risk students by Week 2 or Week 4?
🟪 5. Modeling Question (Optional but impressive)
If you want to include a predictive model:
Can we predict whether a student will pass, fail, or withdraw using demographic, engagement, and assessment features?
This allows you to run:
•	Logistic regression
•	Random forest
•	Feature importance
•	ROC curve
Even a simple model adds huge value to your portfolio.
🟫 6. Executive Summary Structure (Use this in your final report)
Here’s a clean, professional structure:
✅ 1. Purpose
Why the analysis matters (retention, performance, early intervention).
✅ 2. Data
Brief description of OULAD and key tables.
✅ 3. Methods
Python cleaning, feature engineering, EDA, statistics, dashboard.
✅ 4. Key Findings
3–5 bullet points:
•	Engagement is the strongest predictor of success
•	Late submissions correlate with lower scores
•	Early disengagement predicts withdrawal
•	Certain demographic groups show higher risk
✅ 5. Recommendations
•	Early warning system based on engagement
•	Targeted support for high risk groups
•	Monitoring of assessment submission patterns
✅ 6. Dashboard
Screenshots + explanation.
✅ 7. Limitations
•	Observational data
•	No causal inference
•	Missing variables (motivation, external factors)
✅ 8. Next Steps
•	Predictive modeling
•	Intervention testing
•	Longitudinal tracking




## **Tools & Technologies**

The requirements for this project are:
- Trello for project management
- Python (pandas, numpy, seaborn, matplotlib, scikit learn, statsmodels)
- VS Code for development
- Power BI / Tableau for dashboarding
- GitHub for version control and portfolio presentation
- Data sets
- PostGres
Author
Teresa McGarry Analytics Professional Focused on reproducible workflows, executive dashboards, and portfolio ready data storytelling.
 


 