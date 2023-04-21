# RSA-Encryption
RSA (Rivest-Shamir-Adleman) is a public-key encryption algorithm that is widely used for secure data transmission. The RSA algorithm uses two keys: a public key and a private key.

The public key is used for encryption and can be freely distributed, while the private key is used for decryption and must be kept secret.
When someone wants to send an encrypted message to a recipient using RSA, they obtain the recipient's public key and use it to encrypt the message. The recipient can then use their private key to decrypt the message.
Conversely, when the recipient wants to send a signed message to someone, they use their private key to sign the message, and the recipient can use the sender's public key to verify the signature.
RSA encryption is based on the mathematical difficulty of factoring large numbers. The security of RSA encryption relies on the fact that it is very difficult to factor a large number into its prime factors, which is required to break the encryption.
