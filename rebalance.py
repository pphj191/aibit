
import bit_inq_mybalance , bit_buysell
import bit_inq_price
import telegram_aibit

# 5초에 한번씩 실행될것

# 리밸런싱에 쓸 종목 = ["", ""]
def activate(using_market):
    # 내정보 가져오기 >> 설정금액, 가상금액 [{'currency':'ETH', 'balance':300} , {}]
    coins_now, KRW_balance = bit_inq_mybalance.get_balance(using_market)  #*****env 필요
    # coins_now, KRW_balance = bit_inq_mybalance.get_balance_test(using_market)  #*****env 필요

    # 현재가 가져오기
    for coin in coins_now:
        coin.update(bit_inq_price.get_price(coin['currency']))

    # for (종목별) : 리밸런싱 >> 매매 >> 확인
    # ETH balance - KRW balance(가상 balance) 차이가 10000원 나면 매수매도1호가로 5000원 매매
    # if 매수1호가Xbalance - KRW balance > 10000
    #KRW balance는 DB로 저장할까? 일단 한 코인만 할까? << 한코인만
    if float(coins_now[0]['bid_price'])*float(coins_now[0]['balance']) - float(KRW_balance) >= 11000 : #코인이 KRW보다 더크면 팔자(바로팔게 매수호가 기준)
        #매도
        volume = round(5500/coins_now[0]['bid_price'], 4)
        bit_buysell.sell(coins_now[0]['currency'], volume, coins_now[0]['bid_price'])
        print("매도완료")

        #telegram 연락
        telegram_aibit.send("Sell // " + "시세="+str(coins_now[0]['bid_price']))

    elif float(coins_now[0]['ask_price'])*float(coins_now[0]['balance']) - float(KRW_balance) <= -11000 : #코인이 KRW보다 더크면 팔자(바로팔게 매수호가 기준)
        #매수
        volume = round(5500/coins_now[0]['ask_price'], 4)
        bit_buysell.buy(coins_now[0]['currency'], volume, coins_now[0]['ask_price'])
        print("매수완료")

        #telegram
        telegram_aibit.send("Buy // " + "시세="+str(coins_now[0]['ask_price'])+" /살크기 "+str(volume) + " /가격 " + str(coins_now[0]['ask_price']) +" /가진양 "+ str(KRW_balance) )

    else :
        #넘어가기
        print("아무일도 안일어남")

        pass

#결과출력
#결과

#연습


#그래프화