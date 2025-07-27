def get_bmi():
    height = float(input('請輸入身高120-250cm):'))
    if not (120 <= height <= 250):
        print('身高範圍輸入錯誤')
        raise Exception
    weight = float(input('請輸入體重30-200kg):'))
    if not (30 <= weight <=200):
        print('體重範圍輸入錯誤')
        raise Exception
    bmi = (weight / ((height  / 100) **2))
    print(f'您的BMI值為{round(bmi,1)}')
    return bmi

def get_status(bmi):
    if bmi < 18.5:
        x = '體重過輕'
    elif 18.5 <= bmi < 24:
        x = '正常範圍'
    elif 24 <= bmi < 27:
        x = '體重過重'
    elif 27 <= bmi < 30:
        x = '輕度肥胖'
    elif 30 <= bmi < 35:
        x = '中度肥胖'
    elif bmi >= 35:
        x = '重度肥胖'
    print('您的BMI範圍為',x)

def main():
    try:
        while True:
            try:
                bmi = get_bmi()
                get_status(bmi)
                break
            except ValueError:
                print('請輸入數字')
                continue
            except Exception as e :
                print(e)
                continue
    finally:
        print('程式結束')

if __name__ == "__main__":
    main()