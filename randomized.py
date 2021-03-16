import pandas as pd
import numpy as numy

def randomizr(df,seed):
    xcd = df.copy()
    col = df.columns.values.tolist()
    df_trans = df.T
    df.trans.index =df_trans.columns.values
    df.trans.columns = col
    return df_trans


def derf(xc):
    xcd = xc.copy()
    hgb =[]
    for x in range(len(xcd)):
        sd = random.choice(xcd)
        bg =[]
        for sd not in bg:
            hgb.append(sd)
            bg.append(sd)

def randomized(df, seed):
    XC = df.copy()
    colums = df.columns()
    for x
    