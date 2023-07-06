import chardet

def read_file(path):
    """
    파일의 첫번째 줄을 읽어 인코딩을 확인한 뒤,
    인코딩에 맞게 파일을 읽어 리스트로 반환하는 함수
    Args:
        path (string): 파일 경로
    Returns:
        list of string: 라인(\n)단위로 분리된 문자열
    Examples:
        >>> list_str = read_file('./input.txt')
    """
    # encoding 확인
    enc = 'utf-8'
    with open(path, 'rb') as f:
        tmp = f.readline()
        enc = chardet.detect(tmp)['encoding']

    # file 객체 생성
    list_str = list()
    with open(file=path, mode='r', encoding=enc) as f:
        for line in f:
            list_str.append([int(num) for num in line.split(' ')])   

    return list_str

def write_file(path, ObjList):
    enc = 'utf-8'
    with open(path, 'rb') as f:
        tmp = f.readline()
        enc = chardet.detect(tmp)['encoding']

    with open(file=path, mode='w', encoding=enc) as f:
        for Obj in ObjList:
            # 객체의 데이터를 파일에 작성
            line = ' '.join(str(num) for num in Obj) + '\n'
            f.write(line)

def count_read(path):
    with open(file=path, mode='r') as f:
        CountStr = f.read().strip()
        Count = int(CountStr)

    return Count

def count_write(path, count):
    with open(file=path, mode='w') as f:
        f.write(str(count))


if __name__ == '__main__':
    print('module activated')
    count = count_read('ObjCount.txt')
    print(count)
    count = 0
    count_write('ObjCount.txt', count)

