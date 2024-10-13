import requests


# def get_location(ip):
#     url = f"http://ip-api.com/json/{ip}"  # 使用ip-api.com的API获取IP地理位置信息
#     response = requests.get(url)
#     data = response.json()
#     if data["status"] == "success":
#         country = data["country"]
#         region = data["regionName"]
#         city = data["city"]
#         return f"{country}, {region}, {city}"
#     else:
#         return "Unknown"
#
#
# ip = "119.247.130.117"
# location = get_location(ip)
# print(location)


def GetPublicIP():
    rsp = requests.get(f'https://ipinfo.io/ip')
    return rsp.text



def GetIPLocation(ip):
    response = requests.get(f'https://ipinfo.io/{ip}/json')
    data = response.json()
    return data


print(GetPublicIP())
ip=GetPublicIP()
print(GetIPLocation(ip))