# 데이터 전처리
# 데이터 파일은 CSV UTF-8형태로 저장
try:
    import pandas as pd

    student_score = pd.read_csv("./학업_성취도.csv", encoding='utf-8')
    # 빈 정보 삭제
    student_score = student_score.dropna()
    student_score = student_score.drop(['2000','2000.1','2000.2','2000.3','2000.4','2000.5'], axis=1)
    student_score.index = range(len(student_score.index))

    # 연도별 평균 column 추가하기
    pluscolumn = 1
    while pluscolumn<32:
        student_score[student_score.columns[pluscolumn]+"년 평균"] = '-'
        pluscolumn += 6
        
    for i in range(1,len(student_score.index)):
        j = 1
        k = 37
        while j<32:
            yearsum =  0
            fillyear = 0
            for l in range(0,6):
                if (student_score.loc[i][j+l].isnumeric()):
                    yearsum += int (student_score.loc[i][j+l])
                    fillyear += 1
            if fillyear!=0:
                student_score.loc[i][student_score.columns[k]] = yearsum / fillyear
            k += 1    
            j += 6

    # 앞의 detail 정보 삭제하고 연도별 평균만 남기기
    student_score = student_score.drop(student_score.columns[1:37], axis = 1)

    # 전 기간동안 국가 평균 column 추가하고 빈 정보 삭제
    student_score["국가 평균"] = '-'
    for i in range(1,len(student_score.index)):
        totalsum = 0
        totalyear = 0
        country_average = 0
        for j in student_score.columns[1:-1]:
            if student_score.loc[i][j]!='-':
                totalsum += student_score.loc[i][j]
                totalyear += 1
        if totalyear!=0:        
            country_average = totalsum / totalyear
        else:
            country_average = 0
        student_score.loc[i][student_score.columns[-1]] = country_average

    noinforcountry = []
    for i in range(1,len(student_score.index)):
        if student_score.loc[i]["국가 평균"] == 0:
            noinforcountry.append(i)
    student_score = student_score.drop(noinforcountry)

    # 국가 이름을 index로 설정
    student_score.set_index("국가별", inplace = True)
    student_score = student_score.drop("국가별")

    # 전처리 정보 csv로 저장
    student_score.to_csv("학업_성취도_전처리.csv",encoding='utf-8-sig')

except ModuleNotFoundError:
    print("프로그램 실행을 위한 모듈이 설치되어있지 않습니다. 필요한 라이브러리를 설치하고 다시 실행하십시오")

