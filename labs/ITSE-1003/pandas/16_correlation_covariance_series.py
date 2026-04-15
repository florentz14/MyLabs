import pandas as pd


seq2 = pd.Series(
    [3, 4, 3, 4, 5, 4, 3, 2],
    index=["2006", "2007", "2008", "2009", "2010", "2011", "2012", "2013"],
)
seq = pd.Series(
    [1, 2, 3, 4, 4, 3, 2, 1],
    index=["2006", "2007", "2008", "2009", "2010", "2011", "2012", "2013"],
)

print("seq.corr(seq2):")
print(seq.corr(seq2))
print()

print("seq.cov(seq2):")
print(seq.cov(seq2))
