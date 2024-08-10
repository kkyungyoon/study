def solution(price, money, count):
    # price : 놀이기구 이용료
    # money : 처음 가지고 있던 금액
    # count : 놀이기구 이용횟수
    total_price = 0
    
    for i in range(1, count+1):
        total_price += i * price
    money -= total_price
    
    if money >= 0:
        return 0
    else: 
        result = abs(money)
        # TypeError: Object of type int64 is not JSON serializable
        # 해결 : 결과를 int로 감싸기
        return int(result)