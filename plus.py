import pandas as pd

def findSamemore(dflist):
    '''여러개의 dataframe에서 공통된 국가들의 list를 반환'''
    same_country = []
    for x in dflist[0].index:
        i=1
        appends = True
        while i<len(dflist):
            if x not in dflist[i].index:
                appends = False
                break
            i+=1
        if  appends:
            same_country.append(x)
    return same_country


def makesameListmore(dflist):
    '''두 개의 dataframe에서 공통된 국가들의 평균 데이터 값으로 이루어진 리스트 반환'''
    a=[[] for x in range(len(dflist))]
    same_country = findSamemore(dflist)
    
    for i in same_country:
        for j in range(len(dflist)):
            a[j].append(round(float(dflist[j].loc[i]["국가 평균"])))
    return a


def makesameDfmore(dflist, labellist):
    '''두 개의 dataframe에서 공통된 국가들의 평균 데이터 값으로 이루어진 데이터 프레임 반환'''
    df = pd.DataFrame(makesameListmore(dflist),columns = findSamemore(dflist))
    df.index = labellist
    # 행열 전환하여 리턴 (산점도 그래프 그리기 위해)
    return df.transpose()
