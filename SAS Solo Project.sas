

ods html;
proc freq data = diabetesproject;
tables diabetes_binary * sex * age / norow nocol;
run;
ods html close;

ods html;
proc freq data = diabetesproject;
tables diabetes_binary * income * education/ norow nocol;
run;
ods html close;

ods html;
proc freq data = diabetesproject;
tables diabetes_binary * anyhealthcare * nodocbccost/ norow nocol;
run;
ods html close;


/*Logistic Regression with Multiple Variables*/
ods html;
ods graphics on;
proc logistic data = diabetesproject plots=(oddsratio(cldisplay=serifarrow) roc);
class AnyHealthcare nodocbccost Sex Age Education Income;
model diabetes_binary = AnyHealthcare nodocbccost Sex Age Education Income/slstay=.05 selection=stepwise risklimits;
run;
ods graphics off;
ods html close;


