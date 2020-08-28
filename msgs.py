import twet
from datetime import datetime

messages = ["Maintain 6ft (2m) distance from others!", "Wear a face covering over your nose and mouth!", "Cough or sneeze into your elbow or a tissue!", "Wash your hands often and use hand sanitizer!", "Avoid touching your eyes, nose, and mouth!", "Stay in if you don't feel well!", "We are NU strong!", "Wear a mask, Don't be a knucklehead!", "Wash your hands for at least 20 seconds!", "Students should contact Health Services to arrange for a test. Health Services will directly inform students of test results and delineate an appropriate strategy for care based on the result of their test.", "Turn on notifications for everything COVID @NorthwesternU !", "UPDATE: WE ARE STILL IN A pandemic"]


now = datetime.now()
c = int(now.strftime("%d"))
ar = c%len(messages)



twet.tweetIt(messages[ar])

