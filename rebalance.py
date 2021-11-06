
import bit_inq_mybalance
import bit_inq_price

# 5초에 한번씩 실행될것

# 리밸런싱에 쓸 종목 = ["", ""]
using_market = ["ETH", ]

# 내정보 가져오기 >> 설정금액, 가상금액 [{'currency':'ETH', 'balance':300} , {}]
coins_now = bit_inq_mybalance.get_balance(using_market)

# 현재가 가져오기
for coin in coins_now:
    coin.update(bit_inq_price.get_price(coin['currency']))

# for (종목별) : 리밸런싱 >> 매매 >> 확인
# ETH balance - KRW balance(가상 balance) 차이가 10000원 나면 5000원 매매
# coin['ask_price']

#결과출력
#결과

#연습


#그래프화