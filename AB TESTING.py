##################
#   AB TESTING   #
##################

import pandas as pd
import statsmodels.stats.api as sms
from scipy.stats import ttest_1samp,shapiro,levene,ttest_ind,mannwhitneyu,pearsonr,spearmanr,kendalltau,f_oneway,kruskal

df_control = pd.read_excel("ab_testing.xlsx",sheet_name="Control Group")
df_control.to_csv("ab_testing_control.csv")
df_control.head()


df_test = pd.read_excel("ab_testing.xlsx",sheet_name="Test Group")
df_test.to_csv("ab_testing_test.csv")
df_test.head()

## GÖREV - 1 ##

# AB Testinin Hipotez Tanımı #

# Maximum Bidding ve Average Bidding ortalamaları arasında istatistiksel olarak anlamlı fark var mıdır?


# HO : M1 = M2 (İki grup ortalamaları arasında istatistiksel olarak anlamı fark yoktur.)
# H1 : M1 != M2 (İki grup ortalamaları arasında istatistiksel olarak anlamı fark vardır.)

# Normallik Varsayımı #

test_stat, pvalue = shapiro(df_control["Purchase"])

print("Test Stat = %.4f, pvalue = %.4f" % (test_stat,pvalue))

# p > 0.05 Normallik Varsayımı Reddedilemez


test_stat, pvalue = shapiro(df_test["Purchase"])

print("Test Stat = %.4f, pvalue = %.4f" % (test_stat,pvalue))

# p > 0.05 Normallik Varsayımı Reddedilemez


# Varyans Homojenliği Varsayımı #

test_stat,pvalue = levene(df_control["Purchase"],
                          df_test["Purchase"])

print("Test Stat = %.4f, pvalue = %.4f" % (test_stat,pvalue))

# p > 0.05 Varyans Homojenliği Varsayımı Reddedilemez


# Hipotezin Uygulanması #

test_stat, pvalue = ttest_ind(df_control["Purchase"],
                              df_test["Purchase"],
                              equal_var = True)


print("Test Stat = %.4f, pvalue = %.4f" % (test_stat,pvalue))

# p > 0.05 HO reddedilemez. Yani iki grup ortalamaları arasında istatistiksel olarak anlamlı bir fark yoktur. #


## GÖREV - 3 ##
"""
1. Adımda (varsayım kontrolü) Normallik Varsayımı işleminde Shapiro-Wilk testini kullandım. 
Daha sonra Varyans Homojenliği testi için Levene testini kullandım. 

2. Adımda (Hipotezin Uygulanması) İki varsayım da sağlandığı için Bağımsız İki Örneklem T Testi(Parametrik Test) kullandım.
"""

## GÖREV - 4 ##

"""
İki grup ortalamaları arasında istatistiksel olarak anlamlı bir fark olmadığı için bir süre daha beklenip değerlerin değişip değişilmeyeceği incelenebilir.
Veya Click/Impression oranlarında inceleme yapılabilir.
"""