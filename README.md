# SDOH-Type-2-Diabetes

## INTRODUCTION

• The International Diabetes Federation estimates 693 million people will 
have type 2 diabetes by 2045 if growth continues [1]. Type 2 diabetes 
burdens the US. It will cost $327 billion in 2017, $237 billion in direct 
medical costs and $90 billion in loses [2]. 

• There have been survey-based models predict type 2 diabetes, however 
due to its causal complexity, they require improve [3, 4]. 

• SAS logistic regression was performed on 2015 BRFSS type 2 diabetes 
dataset. Comparing Python machine learning techniques such 
multivariate logistic regression, multilayer perceptron classifier, random 
forest, gaussian naive bayes, k-neighbors, and decision tree classifier. 

• The ROC curve and AUC scores may be used to compare the two analyses 
to determine which strategy is best at predicting socioeconomic 
determinants of health in type 2 diabetes.

## MATERIALS / METHODS

• A cross-sectional survey of 253,680 persons with 22 feature variables is available 
at https://www.kaggle.com/datasets/cdc/behavioral-risk-factor-surveillancesystem. 

• 35,346 of these entries were diabetic, whereas 218,334 were not. Most of the 21 
feature characteristics were linked to risk factors (high blood pressure, smoking) 
and lifestyle decisions (physical activity, fruits, and vegetables).

• Microsoft Excel, SAS 9.4, and Python 3.12 used for analysis. Microsoft Excel was 
utilized in the data cleaning stages of the analysis by removing all the variables 
that are not significant with social determinants of health, null values, and 
missing values.

• Social determinates of health variables: diabetes_binary, anyhealthcare, 
nodocbccost, sex, age, income, and education.

## SAS Frequency Distribution Tables

![image](https://user-images.githubusercontent.com/50633694/208808463-f21b4176-ca50-414b-8eb1-1c4e2d1e2b61.png)

## RESULTS(FREQUENCY)

• Table 1 shows that females age groups 1–13 have a 57% chance of not having 
diabetes, while males have 43%. Table 2 shows that females age groups 1–13 
have a 52% chance of having diabetes, while males have 48%.

• Table 3 shows that patients with higher income ($75,000 or more) and 
education (college for four years or more) are less likely to have diabetes 
than those with lower income ($25,000-$35,000) and education (high school 
graduate). Table 4 shows that patients with higher income ($35,000-
$75,000+) and education (college for 1–4 years or technical school) are more 
likely to have diabetes than those with lower income ($10,000-$15,000) and 
education (high school graduate). 

• Table 5 shows that patients without health insurance and a primary care 
physician have a lower chance of not having diabetes (3.22%) and a higher 
chance (88.71%). Table 6 shows that 2.27% of patients without health 
insurance and a primary care physician have diabetes, while 87.71% do.

## SAS Logistic Regression

![image](https://user-images.githubusercontent.com/50633694/208808877-df119cc0-de98-4961-93a6-d9167bb8d7cf.png)

## RESULTS (LOGISTIC REGRESSION)

• Table 7 is for the significance test of association.
We reject the null hypothesis that AnyHealthcare, NoDocbcCost, Sex, Age, 
Education, Income, and the responder variable diabetes_binary are not statistically 
significant because of the low p-value of 0.0001.

• Table 8 tells if the independent variables (AnyHealthcare, NoDocbcCost, Sex, Age, 
Education, and Income) are associated with the target outcome 
(diabetes_binary=1). Diabetes_binary = 1 is significantly associated with all 
independent variables (the p-value for all variables is 0.0001 < 0.05). 

We reject the null hypothesis that AnyHealthcare, NoDocbcCost, Sex, Age, 
Education, Income, and the responder variable diabetes_binary are not statistically 
significant.

• Table 9 tells us that most of the independent variable’s groups (AnyHealthcare, 
NoDocbcCost, Sex, Age, Education, and Income) are associated with the target 
outcome (diabetes_binary=1). The majority of the independent variable groups 
are associated with the outcome diabetes_binary = 1 (The p-value for most of the 
independent variable’s groups = 0.0001<0.05). 

Accept the alternative hypothesis that AnyHealthcare, NoDocbcCost, Sex, Age, 
Education, Income, and the responder variable diabetes_binary are statistically 
significant.

• Table 10 shows the odds ratio estimates that a person in the groups of age 1–7 vs. 
9, sex 0 vs 1, AnyHealthcare 0 vs 1, NoDobcCost 0 vs 1, and age 8 and 13 vs 9 has a 
range of 0.054–0.892 times the odds of having diabetes. 

Diabetes odds are 1.128–1.945 times higher in age 10-12 vs 9, education 1-5 vs 6, and 
income 5-7 vs 8. Finally, those with incomes between 1-4 vs. 8 are 2.298-3.212 times 
more likely to have diabetes

![image](https://user-images.githubusercontent.com/50633694/208809177-5077b307-6ab8-4545-939f-9a1e43d36fcd.png)

## Discussion

• On Figure 1, the SAS ROC Curve and AUC Score for Logistic Regression 
are both 0.7100. On Table 11, MLP had the highest AUC score at 0.7107, 
while KNeighbors had the lowest at 0.6081. Python and SAS AUCs are 
comparable. 

• According to Xie et al., they concluded that, of all their machine 
learning models for predicting type 2 diabetes, the neural network 
was the most accurate due to the potential type 2 diabetes risk factor 
of checkup frequency [7]. 

• Comparing the results of my logistic regression to another study 
conducted by Wu et al., their logistic regression model was more 
accurate [8]. This is because Wu et al. [8] conducted this analysis using 
the WEKA toolkit and another high-quality dataset. 

• Study limitations exist. BRFSS data was cross-sectional, making 
causation impossible. Our prediction models may be hampered by 
BRFSS data's self-reporting and memory bias. Clinical data and 
biomarkers may improve type 2 diabetes prediction algorithms.

## Conclusion

• The application of machine learning models to forecast a diabetes survey 
dataset is, in conclusion, a promising field of study. 

• With the availability of clinical data and biomarkers, there is enormous 
potential for these models to be further developed and refined. 

• Future research should concentrate on enhancing the models' precision and 
generalizability by including more data sources, such as electronic health 
records, and exploring alternative model designs. 

• In addition, additional research should be performed to uncover potential 
biases in the datasets used to train these models and to create ways for their 
mitigation. 

• With additional research, machine learning models can become potent tools 
for creating more accurate and precise diabetes survey dataset predictions.

## References

[1] Hernandez C. The Diabetes Epidemic Prediction in 2045. Word--Health. 
2018.https://wordofhealth.com/2018/11/30/the-diabetes-epidemic-prediction-in-2045/ (accessed 26 Nov 2022).

[2] The Cost of Diabetes | ADA. https://diabetes.org/about-us/statistics/cost-diabetes (accessed 26 Nov 2022).

[3] Tabaei BP, Herman WH. A multivariate logistic regression equation to screen for diabetes: development and 
validation. Diabetes Care 2002;25:1999–2003. doi:10.2337/diacare.25.11.1999

[4] Collins GS, Mallett S, Omar O, et al. Developing risk prediction models for type 2 diabetes: a systematic review of 
methodology and reporting. BMC Med 2011;9:103. doi:10.1186/1741-7015-9-103

[5] Delwiche LD, Slaughter SJ. The Little SAS Book: A Primer, Sixth Edition. SAS Institute 2019. 

[6] PROC LOGISTIC: Confidence Intervals for Parameters :: SAS/STAT(R) 9.3 User’s Guide. 
https://support.sas.com/documentation/cdl/en/statug/63962/HTML/default/viewer.htm#statug_logistic_sect040.h
tm (accessed 26 Nov 2022).

[7] Xie Z, Nikolayeva O, Luo J, et al. Building Risk Prediction Models for Type 2 Diabetes Using Machine 
Learning Techniques. Prev Chronic Dis 2019;16:E130. doi:10.5888/pcd16.190109

[8] Wu H, Yang S, Huang Z, et al. Type 2 diabetes mellitus prediction model based on data mining. Inform 
Med Unlocked 2018;10:100–7. doi:10.1016/j.imu.2017.12.006
