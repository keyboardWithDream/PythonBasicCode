import easygui as eg
import sys


def gui_test():
    title = '这是一个关于GUI的测试'
    choices = ['继续', '返回', '取消']

    eg.msgbox('欢迎进行GUI的测试环节!', title)
    choice = eg.choicebox('请选择内容:', title, choices)
    if choice == '继续':
        title = '欢迎进入下一环节'
        choices = ['重新开始', '退出']
        choice = eg.choicebox('请继续选择', title, choices)
        if choice == '重新开始':
            gui_test()
        else:
            eg.msgbox('测试完成', '测试完成', ok_button='退出')
            sys.exit(0)
    elif choice == '返回':
        gui_test()
    else:
        sys.exit(0)


gui_test()
