try:
    import numpy as np
    import matplotlib
    import matplotlib.pyplot as plt
    import seaborn as sns
    from pandas.plotting import scatter_matrix
except ModuleNotFoundError:
    print("프로그램 실행을 위한 모듈이 설치되어있지 않습니다. 필요한 라이브러리를 설치하고 다시 실행하십시오")


# 그래프에서 한글 표시하기 위한 작업
matplotlib.rc('font', family='Malgun Gothic')
matplotlib.rcParams['axes.unicode_minus'] = False

def plotScatter(xlabel,ylabel,df,string):
    '''pyplot과 seaborn으로 산점도 그래프 그리기''' 
    sns.regplot(x=xlabel, y=ylabel, data=df)
    plt.xlim(df[xlabel].min()-1, df[xlabel].max()+1)
    plt.grid()
    plt.title("%s %s와 %s 비교" %(string, xlabel, ylabel))
    plt.show()
 
    z=np.polyfit(df[xlabel], df[ylabel], 1) # 기울기와 절편 확인
    print('기울기:',z[0], '절편:',z[1])
 
def plotLine(label1,label2,lists, stringlist):
    '''line subplot 동시에 그리기'''
    plt.plot(label1,lists[0])
    plt.plot(label2,lists[1])
    plt.title("%s %s(파랑)와 %s(주황) 비교" %(stringlist[0], stringlist[1], stringlist[2]))
    plt.xticks(rotation=75)
    plt.show()

def plotScattermatrix(df):
    '''여러 변수들에 대한 scatter matrix 그래프 그리기'''
    scatter_matrix(df, figsize=(10, 10));
    plt.tight_layout()
    plt.show()
    # df.corr로 각 변수 간 상관지수 출력
    print(df.corr())
