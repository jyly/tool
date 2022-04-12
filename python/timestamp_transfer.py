from datetime import datetime
import time


# ts=1515774430
# dt = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(ts))
# print(dt)
# ts=1499825149.257
# ts=1559051666218
# ts=1456402864242
# print(datetime.utcnow())
# print (time.strftime('%Y-%m-%d %H:%Ms:%S.%f', time.localtime(ts)))
# print(datetime.fromtimestamp(ts / 1000.0).strftime('%Y-%m-%d %H:%M:%S.%f'))
ts=1559051666226
print(datetime.fromtimestamp(ts / 1000.0).strftime('%M:%S.%f'))
ts=1559051666220
print(datetime.fromtimestamp(ts / 1000.0).strftime('%M:%S.%f'))
