# /usr/bin/env python
# Download the twilio-python library from twilio.com/docs/libraries/python
import os
from twilio.rest import Client

# Find these values at https://twilio.com/user/account
# To set up environmental variables, see http://twil.io/secure
account_sid = 'AC1dd3db25ac62230e0e9fb1c676e164dd'
auth_token = 'dd289c57a10b4ac3854b24b04d68287b'

client = Client(account_sid, auth_token)

client.api.account.messages.create(
    to="+12243869303",
    from_="+19165867068",
    body="item added to cart GO TO YOUR COMPUTER NOW")

# TODO validate phone
# client.api.account.messages.create(
#     to="+12248045851",
#     from_="+19165867068",
#     body="item added to cart GO TO YOUR COMPUTER NOW")