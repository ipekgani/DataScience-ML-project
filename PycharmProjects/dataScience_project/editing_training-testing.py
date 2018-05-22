# import pandas as pd
# labels = pd.Series(['MARIJUANA', 'COCAINE', 'METH', 'OPIATES', 'HEROIN', 'FORGE', 'HALLUCINOGENIC'], index=None)
# labels.to_csv('labels.csv')
#
# fdsfs = pd.read_csv('crimes.csv')
# gfdgdfgdfgdfgdf = pd.read_csv('crimes3.csv')
#
# print(len(fdsfs), len(dfsfdsfsdfsd))
# gfdgdfgdfgdfgdf.rename(columns={'Unnamed: 0': 'Sample num'}, inplace=True)
import pandas as pd

train_df = pd.read_csv('categoriacal/categorical_data_fixed.csv', header=0, index_col=0)
train_df = train_df.iloc[-20000:, :]
train_df = train_df.sample(frac=1)


test_df = pd.DataFrame.copy(train_df.iloc[-1000:, :])
train_df = train_df.iloc[:-1000, :]
print(len(test_df), len(train_df))
pd.DataFrame.to_csv(test_df, 'categoriacal/some_test1.csv')
pd.DataFrame.to_csv(train_df, 'categoriacal/some_train1.csv')
