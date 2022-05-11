# 전처리 파일이 있는 경우에만 실행 가능
try:
    import graphs
    import compareData as cd
    import pandas as pd

    edu_cost = pd.read_csv("./교육단계별_연간_학생1인당_공교육비_전처리.csv", encoding = 'utf-8')
    student_score = pd.read_csv("./학업_성취도_전처리.csv",encoding='utf-8')
    patent_enroll = pd.read_csv("./주요국_특허_등록_전처리.csv",encoding='utf-8')
    patent_receipt = pd.read_csv("./주요국_특허_출원_전처리.csv",encoding='utf-8')
    RD_researcher = pd.read_csv("./100만명당_RD_연구개발자_전처리.csv", encoding = 'utf-8')
    total_researcher = pd.read_csv("./총연구원_수_전처리.csv", encoding = 'utf-8')

    # 국가를 index로 변경
    edu_cost.set_index("국가별", inplace = True)
    student_score.set_index("국가별", inplace = True)
    patent_enroll.set_index("국가별", inplace = True)
    patent_receipt.set_index("국가별", inplace = True)
    RD_researcher.set_index("국가별", inplace = True)
    total_researcher.set_index("국가별", inplace = True)

    datadict = {"공교육비":edu_cost,"학업 성취도":student_score,"특허 출원수": patent_receipt, "특허 등록수": patent_enroll, "RD 연구원수": RD_researcher, "총 연구원수": total_researcher}


    df = cd.makesameDfmore(list(datadict.values()), list(datadict.keys()))

    print("각 변수 간 상관지수 확인")
    graphs.plotScattermatrix(df)

except FileNotFoundError:
    print("전처리 파일을 찾을 수 없습니다. 전처리 프로그램을 실행 후 다시 실행하십시오")

except ModuleNotFoundError:
    print("프로그램 실행을 위한 모듈이 설치되어있지 않습니다. 필요한 라이브러리를 설치하고 다시 실행하십시오")

