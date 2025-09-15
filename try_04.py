try:
    print('정상코드')
    print('에러발생')
    #raise "내가 발생시킨 에러"
    raise ValueError("테스트중입니다.")
except Exception as e:
    print(f'에러 : {e} {e.__class__} {e.__class__.__name__}')