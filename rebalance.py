
# 5초에 한번씩 실행될것

# 리밸런싱에 쓸 종목 = ["", ""]
using_market = ["ETH-KRW", ]

# 내정보 가져오기 >> 설정금액, 가상금액 [{'market':'ETH', 'balance':300} , {}]
coins_now = bit_inq_mybalance(using_market)

# 현재가 가져오기
for coin in coins_now:
    coin['price'] = bit_inq_price[coin['market']]


# for (종목별) : 리밸런싱 >> 매매 >> 확인

#결과출력
#결과

#연습


#그래프화