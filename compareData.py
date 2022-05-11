try:
    import pandas as pd
    
except ModuleNotFoundError:
    print("프로그램 실행을 위한 모듈이 설치되어있지 않습니다. 필요한 라이브러리를 설치하고 다시 실행하십시오")

def findSame(df1, df2):
    '''두 개의 dataframe에서 공통된 국가들의 list를 반환'''    
    same_country = [x for x in df1.index if x in df2.index]
    return same_country


def makesameList(df1, df2):
    '''두 개의 dataframe에서 공통된 국가들의 국가 평균 값으로 이루어진 리스트 반환'''
    a=[]
    b=[]
    ratio = 1
    same_country = findSame(df1, df2)
    # 데이터간 scale 맞추기 위해 한국을 기준으로 ratio값 구해 곱함
    ratio = float(df2.loc["한국"]["국가 평균"])/float(df1.loc["한국"]["국가 평균"])
    for i in same_country:
        a.append(round(float(df1.loc[i]["국가 평균"])*ratio))
        b.append(round(float(df2.loc[i]["국가 평균"])))
    return [a,b]


def makesameDf(df1, df2, xlabel, ylabel):
    '''두 개의 dataframe에서 공통된 국가들의 평균 데이터 값으로 이루어진 데이터 프레임 반환'''
    df = pd.DataFrame(makesameList(df1,df2),columns = findSame(df1, df2))
    df.index = [xlabel, ylabel]
    # 행열 전환하여 리턴 (산점도 그래프 그리기 위해)
    return df.transpose()


def makefullDf(df):
    '''데이터 결함이 없는 나라들만 추리고 국가 평균을 삭제한 데이터 프레임 리턴'''
    droplist=[]
    for i in df.index:
        lists = df.loc[i]
        j=0
        while j<len(lists):
            # 하나라도 결함 있는 국가는 삭제 리스트에 포함
            if lists[j]=='-':
                droplist.append(i)
                break
            j += 1
            
    newdf = df.drop(droplist)
    newdf = newdf.drop(["국가 평균"], axis=1)
    # column명 연도만 표기하는 정수로 변경
    newdf.columns = [int(x.split("년")[0]) for x in newdf.columns]
    
    return newdf

def makecountryList(df1, df2, country):
    '''두 개의 dataframe에서 공통된 한 국가의 데이터 값으로 이루어진 리스트 반환'''
    a=[]
    b=[]
    ratio = 1
    # 데이터간 scale 맞추기 위해 처음값 기준으로 ratio값 구해 곱함
    ratio = float(df2.loc[country][df2.columns[0]])/float(df1.loc[country][df1.columns[0]])
    for i in df1.loc[country]:
        a.append(round(float(i)*ratio))
    for j in df2.loc[country]:
        b.append(round(float(j)))
    
    return [a,b]

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
    '''여러개의 dataframe에서 공통된 국가들의 평균 데이터 값으로 이루어진 리스트 반환'''
    a=[[] for x in range(len(dflist))]
    same_country = findSamemore(dflist)
    
    for i in same_country:
        for j in range(len(dflist)):
            a[j].append(round(float(dflist[j].loc[i]["국가 평균"])))
    return a


def makesameDfmore(dflist, labellist):
    '''여러개의 dataframe에서 공통된 국가들의 평균 데이터 값으로 이루어진 데이터 프레임 반환'''
    df = pd.DataFrame(makesameListmore(dflist),columns = findSamemore(dflist))
    df.index = labellist
    # 행열 전환하여 리턴 (산점도 그래프 그리기 위해)
    return df.transpose()
