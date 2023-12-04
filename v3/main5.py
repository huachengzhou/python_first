str_data = r'\u8bf7\u5148\u767b\u5f55'


str_data_to_zh = str_data.encode('utf-8').decode('unicode_escape')
print(str_data_to_zh)

