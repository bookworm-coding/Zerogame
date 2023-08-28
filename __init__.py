from module import *

if __name__ == "__main__":
    number = int(input("제로게임 인원수를 입력하세요: "))
    select = input("엑셀 파일을 원하면 E를, 텍스트 파일을 원하면 T를, 단순 출력을 원하면 P를 입력하세요")
    if select == "E":
        Zero(number).to_excel()
    elif select == "T":
        f = open("result.txt", "w")
        print(Zero(number), file=f)
    elif select == "P":
        print(Zero(number))
    else:
        print("잘못된 입력입니다. 다시 실행해주세요.")
