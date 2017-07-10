# Data Analysis

CSV tasks

1) Open the data.csv using pandas

2) write a function that prints out descriptive statistics for all the variables. This should include mean, median, mode, standard deviation, variance, skew, kurtosis.  Note, you'll have to figure out what to do for categorical variables.  HINT it's not the same as for continuous variables.  (Google is your friend here).

3) create pivot table with pandas that stores the descriptive statistics for each variable.

4) create a bar chart visualizing the range of values of each variable in the csv.

5) create a pie chart visualizing the percentage of values in each bucket, in each column.

6) create a line chart visualization showing the range of values over the index of values.

7) Treat this data as a time series, try to predict the next value in each column.

8) create a data visualization of the results of your time series analysis, include your model.

9) Treat this data as a decision point, try to predict what the next value for the categorical value would be, based on the other columns values are. (Use any model you might like, except a neural network).

10) create a confusion matrix visualization of your classification algorithm.

11) record other descriptive statistics about your classifier, do you trust your results?

12) make use of cross validation to verify your classifier isn't overfitting your data.  Is it?  How can you tell?

13) Regularize your classifier so overfitting is no longer an issue.

14) Use a neural network to classify the data.

15) Feed the results of your neural network into a decision tree, look at what the decision tree generates for rules.  What does this tell you about how the neural network thinks about how to classify your data?

16) Bootstrap your data - re run the binary classifier you chose before.  What changed?  Did you do better or worse?

17) re run your neural network, did you do better or worse?  Why?

18) re run your decision tree classifier, how did the decision rules change?

19) Make use of lime: https://github.com/marcotcr/lime to try to gather more explanatory information about your variables.

20) perform feature engineering on your variables - make use of https://github.com/jundongl/scikit-feature to generate these new features.

21) re run your original classifier with the new features. How do your predictions change?  Make use of Lime, a decision tree and some data visualization.  Try feeding in some new data.  Does it do what you expect?

22) re run your neural network with the new features. How do your predictions change?  Make use of Lime, a decision tree and some data visualization.  Try feeding in some new data.  Does it do what you expect?

23) summarize your results and findings.  




