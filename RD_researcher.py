# 데이터 전처리
# 데이터 파일은 CSV UTF-8형태로 저장
try: 
    import pandas as pd

    RD_researcher = pd.read_csv('./100만명당_RD_연구개발자.csv', encoding = 'utf-8')

    # 빈 정보 삭제
    RD_researcher.set_index(["국가별"], inplace = True)
    RD_researcher = RD_researcher.drop(['1996','1997','1998','1999'], axis = 1)
    RD_researcher = RD_researcher.dropna()

    # 전 기간동안 국가 평균 column 추가하고 빈 정보 삭제
    RD_researcher['국가 평균'] = '-'
    for i in RD_researcher.index:
        totalsum = 0
        count = 0
        for j in RD_researcher.columns[:-1]:
            if RD_researcher.loc[i][j]!='-':
                totalsum += float(RD_researcher.loc[i][j])
                count += 1
        if count!=0:
            totalsum = totalsum / count
        RD_researcher.loc[i]["국가 평균"] = totalsum

    noinforcountry = []
    for i in RD_researcher.index:
        if RD_researcher.loc[i]["국가 평균"] == 0:
            noinforcountry.append(i)
    RD_researcher = RD_researcher.drop(noinforcountry)

    # 전처리 정보 csv로 저장
    RD_researcher.to_csv('./100만명당_RD_연구개발자_전처리.csv', encoding = 'utf-8-sig')

except ModuleNotFoundError:
    print("프로그램 실행을 위한 모듈이 설치되어있지 않습니다. 필요한 라이브러리를 설치하고 다시 실행하십시오")
