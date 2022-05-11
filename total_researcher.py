# 데이터 전처리
# 데이터 파일은 CSV UTF-8형태로 저장
try:
    import pandas as pd

    total_researcher = pd.read_csv("./총연구원_수.csv", encoding = 'utf-8')

    # 빈 정보 삭제
    total_researcher.set_index(["국가별"], inplace = True)
    total_researcher = total_researcher.drop(total_researcher.columns[0:13], axis = 1)
    total_researcher = total_researcher.dropna()

    # 전 기간동안 국가 평균 column 추가하고 빈 정보 삭제
    total_researcher['국가 평균'] = '-'
    for i in total_researcher.index:
        totalsum = 0
        count = 0
        for j in total_researcher.columns[:-1]:
            if total_researcher.loc[i][j]!='-':
                totalsum += float(total_researcher.loc[i][j])
                count += 1
        if count!=0:
            totalsum = totalsum / count
        total_researcher.loc[i]["국가 평균"] = totalsum

    noinforcountry = []
    for i in total_researcher.index:
        if total_researcher.loc[i]["국가 평균"] == 0:
            noinforcountry.append(i)
    total_researcher = total_researcher.drop(noinforcountry)

    # 전처리 정보 csv로 저장
    total_researcher.to_csv("./총연구원_수_전처리.csv", encoding = 'utf-8-sig')

except ModuleNotFoundError:
    print("프로그램 실행을 위한 모듈이 설치되어있지 않습니다. 필요한 라이브러리를 설치하고 다시 실행하십시오")

