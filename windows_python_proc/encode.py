# -*- coding:utf-8 -*-

import win32com.client


def encrypt(key, content):  # key:密钥,content:明文
    EncryptedData = win32com.client.Dispatch('CAPICOM.EncryptedData')
    EncryptedData.Algorithm.KeyLength = 5
    EncryptedData.Algorithm.Name = 2
    EncryptedData.SetSecret(key)
    EncryptedData.Content = content
    return EncryptedData.Encrypt()


def decrypt(key, content):  # key:密钥,content:密文
    EncryptedData = win32com.client.Dispatch('CAPICOM.EncryptedData')
    EncryptedData.Algorithm.KeyLength = 5
    EncryptedData.Algorithm.Name = 2
    EncryptedData.SetSecret(key)
    EncryptedData.Decrypt(content)
    str = EncryptedData.Content
    return str


s1 = encrypt('lovebread', 'hello world')
s2 = decrypt('lovebread', s1)
print s1, s2

# MGEGCSsGAQQBgjdYA6BUMFIGCisGAQQBgjdYAwGgRDBCAgMCAAECAmYBAgFABAgq
# GpllWj9cswQQh/fnBUZ6ijwKDTH9DLZmBgQYmfaZ3VFyS/lq391oDtjlcRFGnXpx
# lG7o
# hello world
