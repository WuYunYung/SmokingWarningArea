import binascii

user_title = "test"

user_slug = str(binascii.b2a_hex(
                user_title.encode('utf-8')))[2:- 2]

print(user_slug)
