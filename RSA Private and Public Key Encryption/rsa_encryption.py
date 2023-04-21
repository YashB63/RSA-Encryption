import rsa

#public_key, private_key = rsa.newkeys(1024)

#print(private_key)

"""
with open("public.pem", "wb") as f:
    f.write(public_key.save_pkcs1("PEM"))

with open("private.pem", "wb") as f:
    f.write(private_key.save_pkcs1("PEM"))
"""
with open("public.pem", "rb") as f:
    public_key = rsa.PublicKey.load_pkcs1(f.read())

with open("private.pem", "rb") as f:
    private_key = rsa.PrivateKey.load_pkcs1(f.read())

#message = "Hey There! I am using WhatsApp"

#encrypted_message = rsa.encrypt(message.encode(), public_key)
"""

encrypted_message = open("encrypted.message", "rb").read()

with open("encrypted.message", "wb") as f:
    f.write(encrypted_message) 

clear_message = rsa.decrypt(encrypted_message, private_key)
print(clear_message.decode())

"""
message = " Kabhi Kabhi lagta hai Apun ich bhagwani hai!"

signature = rsa.sign(message.encode(), private_key, "SHA-256")

with open("signature", "rb") as f:
    # f.write(signature)
    signature = f.read()


public_key, private_key = rsa.newkeys(1024)

print(rsa.verify(message.encode(), signature, public_key))


