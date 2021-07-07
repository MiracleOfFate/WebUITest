import yaml

# yaml文件读取的操作
file = open('tests.yaml', encoding='utf-8')
res = yaml.load(file, Loader=yaml.FullLoader)
print(type(res))
for l in res:
    print(type(l))
