

def is_pop(pop_count,day_count,open_count,is_pro,save_count):
    if pop_count < 1:#判断弹窗测试
        if day_count >= 3 and open_count>5 and save_count >= 1:#若用户累计登录三天且开启app次数大于5次，则在第一次保存成功后弹出
            print("弹出弹窗")
        elif is_pro == 1 and save_count <= 1:#若用户成为付费用户，则在第一次保存成功后弹出
            print("弹出弹窗")
        elif is_pro == 2 and save_count >=4:#若用户成功保存三次，则在第四次保存成功后弹出
            print("弹出弹窗")
        else:
            print("没有符合弹窗弹出的条件")
    elif pop_count >=1 and  pop_count <= 2:#已经弹出过一次
        if save_count >=10 and click_type != 1:
            print("弹出弹窗")
        else:
            print("保存次数未达到10次或第一次弹出点击了'给个好评/吐槽一下'，所以不能弹出第二次")
    elif pop_count > 2:#已经弹出过两次
            print("弹出次数大于2，不再弹出弹窗")


def is_int(x):
    while True:
        if x.isdigit():
            break
        else:
            x = input("请重新输入(请输入正整数):")
    return x


if __name__ == '__main__':
    pop_count = input("请输入已弹窗次数(请输入正数):")
    pop_count = int(is_int(pop_count))
    day_count = input("请输入累计登陆天数(请输入正整数):")
    day_count = int(is_int(day_count))
    open_count = input("请输入累计打开app次数(请输入正整数):")
    open_count = int(is_int(open_count))
    is_pro = input("是否为付费用户1.'是'，2.'否':")
    is_pro = int(is_int(is_pro))
    save_count = input("请输入保存次数(请输入正整数):")
    save_count = int(is_int(save_count))
    click_type = input("是否点击过 1.给个好评/吐槽一下  2.下次在说（输入其他都为'下次再说'）")
    click_type = int(is_int(click_type))
    is_pop(pop_count, day_count, open_count, is_pro, save_count)