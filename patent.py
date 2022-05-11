# 데이터 전처리
# 데이터 파일은 CSV UTF-8형태로 저장

def rowAverage(df):
    '''국가 평균 column 추가'''
    df["국가 평균"]='-'
    for i in df.index:
        totalsum = 0
        plusyear = 0
        for j in df.columns:
            if df.loc[i][j]!='-' :
                totalsum += int(df.loc[i][j])
                plusyear += 1
        if plusyear!=0:
            totalsum = round(totalsum/plusyear)

        df.loc[i]["국가 평균"] = totalsum
    return df

def deleteNa(df):
    '''국가 평균0인 row 삭제'''
    droplist = []
    for i in df.index:
        if df.loc[i]["국가 평균"] == 0:
            droplist.append(i)
    return df.drop(droplist)

try:
    import pandas as pd

    patent = pd.read_csv('./주요국_특허_출원_·_등록.csv', encoding = 'UTF-8')

    # 빈 정보 삭제 및 국가를 인덱스로
    patent = patent.dropna()
    patent.set_index('국가별', inplace = True)
    patent = patent.drop('국가별')

    # 특허 출원(receipt)과 등록(enroll) 정보 분리
    patent_enroll = patent.drop(patent.columns[::2],axis = 1)
    patent_receipt = patent.drop(patent.columns[1::2],axis = 1)

    # patent enroll column 다듬기 (ex 2008.1 > 2008)
    newcol = []
    for i in range(len(patent_enroll.columns)):
        newcol.append(patent_enroll.columns[i].split(".")[0])
    patent_enroll.columns = newcol

    # 국가 평균 column 추가하고 빈 정보 삭제
    patent_enroll = rowAverage(patent_enroll)
    patent_receipt = rowAverage(patent_receipt)
    patent_enroll = deleteNa(patent_enroll)
    patent_receipt = deleteNa(patent_receipt)

    # 전처리 정보 csv로 저장
    patent_enroll.to_csv('./주요국_특허_등록_전처리.csv', encoding = 'UTF-8-sig')
    patent_receipt.to_csv('./주요국_특허_출원_전처리.csv', encoding = 'UTF-8-sig')

except ModuleNotFoundError:
    print("프로그램 실행을 위한 모듈이 설치되어있지 않습니다. 필요한 라이브러리를 설치하고 다시 실행하십시오")







