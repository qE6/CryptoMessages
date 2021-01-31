# CryptoMessages
Simple script for cipher your message using RSA

# Installation
**Debian-based**
```sudo apt update && sudo apt install python3-argparse python3-pycryptodome git -y && git clone https://github.com/qE6/CryptoMessages && cd CryptoMessages```

**Arch-based**
```sudo pacman -S python3-argparse pacman3-pycryptodome git && git clone https://github.com/qE6/CryptoMessages && cd CryptoMessages```

# Args
```
-b <1024|2048|4096> - key generation.
-k - Key file. Required for decipher/cipher/key generation'
-em - Text message to cipher
-dm - Text message to decipher
-ef - File to cipher
-df - File to decipher
```

# Examples
**Generate 2048-RSA keys and write to files keys.private keys.public**
```python3 CryptoMessages.py -k keys -b 2048```

**Cipher message**
```python3 CryptoMessages.py -k keys.public -em "Text to cipher"```

**Decipher message**
```python3 CryptoMessages.py -k keys.private -dm H5z905LGM+TwhcQoxw57XV6N+ek0H6DTXx4MOb5wqEnTLOZ0tW9/3o0TGbbuAT7/Zp+hnHfPb7GYIQlVM2Q2P5Q1zJvnpzYoj3x7O9MD9o6Q+6vX8tLAGn8mbqjsql2w1an30iQIkd3pal5XA7QNaxU4os8QekLDL0eiZA6bDoaHXeXV+PM3dfEoJ9ashXcyoUsOiF541X6CGXiaMxv5u19q4TncZKdKOrvEugrz5JLeZvesx+xBnZoxidQZC7NwPMZmBAnbfZeIw6Kpk/qXDvmSoREM3Z+LqM0DoHfHJ6Mz9r5hMkcH+yjwxlz9f5/f0dnHPWDoJv5JbcyfjoCneA==```

**Cipher file**
```python3 CryptoMessages.py -k keys.public -ef <file path>```

**Decipher file**
```python3 CryptoMessages.py -k keys.private -df <file path>```


**Feel free to open issue**
