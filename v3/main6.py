

text = '系统可能不会保存您所做的更改'

# 将中文转换为Unicode编码
text_unicode = text.encode('unicode-escape').decode()
print(text_unicode)

# 将Unicode编码转换为中文
# s = text_unicode.encode('utf-8').decode('unicode_escape')
s = text_unicode.encode().decode('unicode_escape')
print(s)