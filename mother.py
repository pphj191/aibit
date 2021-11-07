
import time
import rebalance

while(1):
    try:
        rebalance.activate(["ETC", ])
        time.sleep(5)
    except KeyboardInterrupt:
        print("finish")
        break
