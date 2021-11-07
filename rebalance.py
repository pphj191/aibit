
import bit_inq_mybalance, bit_buysell
import bit_inq_price

# 5초에 한번씩 실행될것

# 리밸런싱에 쓸 종목 = ["", ""]
using_market = ["ETC", ]

# 내정보 가져오기 >> 설정금액, 가상금액 [{'currency':'ETH', 'balance':300} , {}]
coins_now, KRW_balance = bit_inq_mybalance.get_balance(using_market)

# 현재가 가져오기
for coin in coins_now:
    coin.update(bit_inq_price.get_price(coin['currency']))

# for (종목별) : 리밸런싱 >> 매매 >> 확인
# ETH balance - KRW balance(가상 balance) 차이가 10000원 나면 매수매도1호가로 5000원 매매
# if 매수1호가Xbalance - KRW balance > 10000
#KRW balance는 DB로 저장할까? 일단 한 코인만 할까? << 한코인만
if coins_now[0]['bid_price']*coins_now[0]['balance'] - KRW_balance >= 10000 : #코인이 KRW보다 더크면 팔자(바로팔게 매수호가 기준)
    #매도
    volume = round(10000/coins_now[0]['bid_price'], 4)
    bit_buysell.sell(coins_now[0]['currency'], volume, coins_now[0]['bid_price'])
    
    #telegram 연락

elif coins_now[0]['ask_price']*coins_now[0]['balance'] - KRW_balance <= -10000 : #코인이 KRW보다 더크면 팔자(바로팔게 매수호가 기준)
    #매수
    volume = round(10000/coins_now[0]['ask_price'], 4)
    bit_buysell.buy(coins_now[0]['currency'], volume, coins_now[0]['ask_price'])

else :
    #넘어가기
    pass

#결과출력
#결과

#연습


#그래프화