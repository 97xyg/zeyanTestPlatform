# coding: utf-8
# -----------------------
# @project：zeyanTestPlatform
# @Author ： lizheyan
# @File ：responeContent.py
# @Time ： 2021/05/22 20:25:52
# -----------------------

def my_response(flag:bool,data,msg:str=None):
    """

    :param flag: 操作成功与否标识符
    :param data: 返回给前端的数据
    :param msg: 响应消息，成功可不传
    :return:
    """
    resp_content = {}
    if flag:
        resp_content['code'] = 200
        msg = msg if msg is not None else 'success'
        resp_content['msg'] = msg
        resp_content['data'] = data
    else:
        resp_content['code'] = 400
        msg = msg if msg is not None else 'fail'
        resp_content['msg'] = msg
        resp_content['data'] = data

    return resp_content