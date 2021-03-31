import requests

# 获取iap的json列表
bundle_id = input('输入包名:')
iap_session = 'MjU5OTY3ODA7bWNpY2kxMjM0NTsxNTc0OTM1MTc4NjIzOzA'

def get_iap_list() -> object:
    global len_d,d_iap,s_id,itemtype_list,itemcount_list,iapid_list,totalcost_list,productid
    url_iap = 'http://api.solotech.me/iap/items?productId='+bundle_id+'&lang=zh&session='+iap_session
    r_iap = requests.get(url_iap)
    d_iap = r_iap.json()
    len_d = len(d_iap['items'])
    itemtype_list = []
    itemcount_list = []
    iapid_list = []
    totalcost_list = []

    for i in range(len_d):
        productid = d_iap['items'][i]['productId']      # 取配置的包名
        itemtype = d_iap['items'][i]['itemType']        # 取项目类别
        itemcount = d_iap['items'][i]['itemCount']      # 取项目数量
        iapid = d_iap['items'][i]['iapId']              # 取配置的iap
        totalcost = d_iap['items'][i]['costTotal']      # 取项目总价格
        itemtype_list.append(itemtype)
        itemcount_list.append(itemcount)
        iapid_list.append(iapid)
        totalcost_list.append(totalcost)

    s_id = set([productid])             # 配置的包名集合
    iapid_judge(s_id)

def iapid_judge(s_id):                  # 循环取所有的id,放进集合,=1代表正确
    if bundle_id in s_id and len(s_id) == 1:
        print('✅ iap包名配置正确')
        print('------------------------------')
        iap_list_output()
    else:
        print('❌ iap中配置的包名与填写的包名不符')
        print('------------------------------')

def iap_list_output():
    for i in range(len(iapid_list)):
            if iapid_list[i] is not None:
                print('类型:{} * 数量:{};\n💵 : {};\tIAP ID:{};'.format(itemtype_list[i],
                                                                          itemcount_list[i], totalcost_list[i], iapid_list[i]))
                print('------------------------------')

get_iap_list()