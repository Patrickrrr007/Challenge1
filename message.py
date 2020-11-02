#寄簡訊到手機
from twilio.rest import Client
import time

#Your account SID from twilio.com/console
account_sid = ''

#Your auth token from twilio.com/console
auth_token = ''

start_time = time.time()
client = Client(account_sid, auth_token)

message = client.messages.create(
	to="",
	from_="",
	body="可以用python寄簡訊囉～～")

end_time = time.time()

print('花了', end_time - start_time, '秒')
print(message.sid)