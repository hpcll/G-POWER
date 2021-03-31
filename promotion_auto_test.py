import requests

bundle_id = 'com.followqrcode.fastlink.bestlikes'
t = 0
discountTypeId = []             # 用户等级          # "promCategory"pro类
promDuration = []               # promotion时长,
promExtraSize = []              # pro加的金币数及天数
promExtraType = []              # 对应promExtraSize的类型(test)
default_duration = 40           # 默认promotion时长
# 设置不同用户的session,循环取去发送request
user_session = {'101': 'MzE0MjMyNDY7cGF5bWVudHRlc3Q7MTU4MTY1MjQ4OTU5MTsw',
                '201': 'MjgzNTQ5OTA7bWNpY2kxMjMxOzE1ODE2NTI1NDI1Nzg7MA',
                '202': 'MjgzNTUwMjA7bWNpY2kxMjMyOzE1ODE2NTI1OTI3MTE7MA',
                '203': 'Mjg2NDcyNjE7bWNpY2kxMjM0NTE7MTU4MTY1MjY0MzgwMzsw',
                '204': 'MjgzNTU3MDg7bWNpY2kxMjM0NTI7MTU4MTY1MjY3ODQ4Nzsw',
                '205': 'Mjg1MTU2OTg7bWNpY2kxMjM0NTM7MTU4MTY1MjcxODcwNzsw',
                '206': 'MjgzNTU3ODM7bHV4dWZlaTMzMDY7MTU4MTY1Mjc2NzMwNDsw',
                '207': 'MjU5OTY3ODA7bWNpY2kxMjM0NTsxNTgxNjUyODExNjE1OzA'}
iap_session = user_session['101']
#   0-5 coins; 6,7 Days; 8-13 Likes; 14-19 Followers
promExtraSize_101 = [100, 1000, 3000, 8000, 25000, 60000, 2, 2,
                     25, 250, 750, 2000, 6250, 15000, 5, 50, 150, 400, 1250, 3000]
#   ['Coins', 'Days', 'Days', 'Likes', 'Followers']
promExtraSize_201 = [1000, 2, 2, 250, 50]
#   ['Coins', 'Days', 'Days', 'Likes', 'Followers']
promExtraSize_202 = [2100, 2, 2, 525, 105]
#   ['Coins', 'Days', 'Days', 'Likes', 'Followers']
promExtraSize_203 = [5600, 2, 2, 1400, 280]
#   ['Coins', 'Days', 'Days', 'Likes', 'Followers']
promExtraSize_204 = [12500, 2, 2, 3125, 625]
#   ['Coins', 'Days', 'Days', 'Likes', 'Followers']
promExtraSize_205_207 = [30000, 2, 2, 7500, 1500]
default_promExtraSize = [promExtraSize_101, promExtraSize_201,
                         promExtraSize_202, promExtraSize_203,
                         promExtraSize_204, promExtraSize_205_207,
                         promExtraSize_205_207, promExtraSize_205_207]

for grade, session in user_session.items():
    url = 'http://api.solotech.me/promotion/info?session='+session+'&productId='+bundle_id
    r = requests.get(url)
    d = r.json()
    len_p = len(d['promotionList'])

    for i in range(len_p):
        len_promExtraSize = len(d['promotionList'][i]['productPromotionIaps'])
        discountTypeId = d['promotionList'][i]['discountTypeId']            # 用户等级
        promDuration = d['promotionList'][i]['promDuration']                # promotion时长
        for j in range(len_promExtraSize):                                  # 一个用户类型下pro加的金币数及天数
            promExtraSize.append(d['promotionList'][i]['productPromotionIaps'][j]['promExtraSize'])
            promExtraType.append(d['promotionList'][i]['productPromotionIaps'][j]['promExtraType'])

    if promExtraSize == default_promExtraSize[t]:
        print('{}等级用户promotion校验正确:'.format(discountTypeId))
        print(promExtraSize)
        print('promotion时长:{}'.format(promDuration))
        print(promExtraType)
        print('------------------------------')
    else:
        print('{}等级用户校验错误,\n当前配置为:{}\n默认配置为:{}'.format(discountTypeId, promExtraSize, default_promExtraSize[t]))
        print('promotion时长:{}'.format(promDuration))
        print(promExtraType)
        print('------------------------------')
    promExtraSize.clear()
    promExtraType.clear()
    t += 1


# store = "1"
# getCoinsBottom = "2"
# loveForever = "3"
# noCoins = "4"
# betrayLimit = "5"
# popup = "6"
