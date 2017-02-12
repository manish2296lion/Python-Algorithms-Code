import re
# print re.split(r'\s*',"Hey I am  Manish")
# print re.split(r'(\s*)',"Hey I am  Manish")
# print re.split(r's*',"Hey I am  Manish")
# print re.split(r'[a-f]',"adsdi asasddasdl;as'dlas jddmas;lsdak")
ptn=re.compile(r'\D([0-1]?[0-9]?[0-9]|2[0-4][0-9]|25[0-5])(\.)([0-1]?[0-9]?[0-9]|2[0-4][0-9]|25[0-5])(\.)([0-1]?[0-9]?[0-9]|2[0-4][0-9]|25[0-5])(\.)(25[0-5]|2[0-4][0-9]|[0-1]?[0-9]?[0-9])')
ips=["".join(x) for x in re.findall(ptn,"asdn as nasdjn asj ds123.21.234.234 ,234.12.1.1,127.0.0.1,123.341.21.123")]
print ips
