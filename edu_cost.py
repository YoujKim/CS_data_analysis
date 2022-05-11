# 데이터 전처리
# 데이터 파일은 CSV UTF-8형태로 저장
try:
    import pandas as pd

    edu_cost = pd.read_csv("./교육단계별_연간_학생1인당_공교육비.csv",encoding='utf-8')

    # 빈 정보 삭제
    edu_cost = edu_cost.dropna()
    edu_cost.index = range(len(edu_cost.index))
    edu_cost = edu_cost.drop(['2018','2018.1','2018.2'], axis=1)

    # edu_cost에 연도별 평균 column 추가하기 (초/중/고중 하나라도 빠진 경우 추가X)
    pluscolumn = 1
    while pluscolumn<35:
        edu_cost[edu_cost.columns[pluscolumn]+"년 평균"] = '-'
        pluscolumn += 3

    for i in range(1,len(edu_cost.index)):
        j = 1
        k = 37
        while j<35:
            if edu_cost.loc[i][j].isnumeric() and edu_cost.loc[i][j+1].isnumeric() and edu_cost.loc[i][j+2].isnumeric():
                yearsum =  int(edu_cost.loc[i][j]) + int(edu_cost.loc[i][j+1]) + int(edu_cost.loc[i][j+2])
                edu_cost.loc[i][edu_cost.columns[k]] = yearsum/3
            k += 1    
            j += 3

    # 전 기간동안 국가 평균 column 추가하고 빈 정보 삭제
    edu_cost["국가 평균"] = '-'
    for i in range(1,len(edu_cost.index)):
        totalsum = 0
        totalyear = 0
        country_average = 0
        for j in edu_cost.columns[37:-1]:
            if edu_cost.loc[i][j]!='-':
                totalsum += edu_cost.loc[i][j]
                totalyear += 1
        if totalyear!=0:        
            country_average = totalsum / totalyear
        edu_cost.loc[i][edu_cost.columns[-1]] = country_average

    noinforcountry = []
    for i in range(1,len(edu_cost.index)):
        if edu_cost.loc[i][edu_cost.columns[-1]] == 0:
            noinforcountry.append(i)
    edu_cost = edu_cost.drop(noinforcountry)

    # 앞의 detail 정보 삭제하고 연도별 평균, 국가 평균만 남기기
    edu_cost = edu_cost.drop(edu_cost.columns[1:37], axis = 1)
    edu_cost.set_index('국가별', inplace = True) # 국가를 index로 만들기
    edu_cost = edu_cost.drop('국가별')

    # 전처리 정보 csv로 저장
    edu_cost.to_csv("교육단계별_연간_학생1인당_공교육비_전처리.csv",encoding='utf-8-sig')

except ModuleNotFoundError:
    print("프로그램 실행을 위한 모듈이 설치되어있지 않습니다. 필요한 라이브러리를 설치하고 다시 실행하십시오")
