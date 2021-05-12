# -*- coding: utf-8 -*-
"""
Created on Tue May 11 20:57:03 2021

@author: Pragi
"""
import pandas as pd
import pickle
df=pd.read_csv("hiring.csv")
df["test_score(out of 10)"].mean()
df["test_score(out of 10)"]=df["test_score(out of 10)"].fillna(df["test_score(out of 10)"].mean())
df["experience"] =df["experience"].fillna("zero")
df["experience"].isnull()
from word2number import w2n
df["experience"]=df["experience"].apply(w2n.word_to_num)
x=df.drop("salary($)",axis="columns")
y=df["salary($)"]
from sklearn.linear_model import LinearRegression
regressor=LinearRegression()
regressor.fit(x,y)
pickle.dump(regressor,open("model.pkl",'wb'))
model=pickle.load(open("model.pkl",'rb'))
print(model.predict([[2,9,6]]))

