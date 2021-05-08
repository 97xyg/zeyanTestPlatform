# coding: utf-8
# -----------------------
# @project：zeyanTestPlatform
# @Author ： lizheyan
# @File ：paging.py
# @Time ： 2021/05/05 11:35:49
# -----------------------
from rest_framework import pagination


class MyPageNumberPagination(pagination.PageNumberPagination):
    # http://127.0.0.1:8000/students/?page=1&limit=5 一般用它
    page_size = 10               # 每页显示多少条
    page_query_param = 'page'   # 查询参数
    page_size_query_param = 'limit'  # 查询的时候指定每页显示多少条
    max_page_size = 100               # 每页最多显示多少条

class MyLimitOffsetPagination(pagination.LimitOffsetPagination):
    default_limit = 2  # 默认条数
    limit_query_param = 'limit'  # 查询时，指定查询多少条
    offset_query_param = 'offset'  # 查询时，指定的起始位置是哪
    max_limit = 5  # 查询时，最多返回多少条

class MyCursorPagination(pagination.CursorPagination):
    cursor_query_param = 'cursor'  # 查询的时候，指定的查询方式
    page_size = 2  # 每页显示多少条
    ordering = 'id'  # 排序方式,一定要指定排序方式，就是model中的可以排序的字段
    # page_size_query_param = 'size'  # 查询的时候指定每页显示多少条
    # max_page_size = 5  # 每页最多显示多少条