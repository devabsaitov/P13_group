import bcrypt

password = "0001"

hash_password = bcrypt.hashpw(password.encode() , salt = bcrypt.gensalt())
print(hash_password)

password2 = "0001"
hash_password2 = bcrypt.hashpw(password2.encode() , salt = bcrypt.gensalt())

check_password  = bcrypt.checkpw(password2.encode(),hash_password )
print(check_password)




