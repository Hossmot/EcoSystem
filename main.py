#파일을 통해 개체의 염색체를 저장 및 생존 관리
#만날 확률을 Hide 에 할당
#먹이를 한정 -> 환경
#먹이를 얻을 확률 GetEnergy
#만난다 -> Event
#정기적으로  감소하는 Life

import ObjectManagement as OM
import random as r

class Cell:
    def __init__(self, CellInfo):
        __info = {
            "Code" : CellInfo[0],
            "Life" : CellInfo[1]
        }
    def gets(self, key):
        return self.__info[key]
    
    def CreateBaseList(Num):
        ReturnList = []
        ReturnList.append(Num)
        ReturnList.append(20040322)
        return ReturnList


C_DefCount = OM.count_read('CellDefCount.txt')
C_List = OM.read_file('CellList.txt')

Field = []

Base = Cell.CreateBaseList(C_DefCount)
Field.append(Cell(Base))


