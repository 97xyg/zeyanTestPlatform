from django.db import models


# Create your models here.

class TestPlane(models.Model):
    """测试计划表"""
    id = models.AutoField(primary_key=True, verbose_name='测试计划id', help_text='测试计划id')
    test_plane = models.CharField(max_length=20, verbose_name="测试计划名称", help_text='测试计划名称')
    test_plane_description = models.CharField(max_length=100, null=True, verbose_name="测试计划描述", help_text='测试计划描述')
    creator = models.CharField(max_length=10, verbose_name="创建人", help_text='创建人')
    create_time = models.DateTimeField(auto_now_add=True, verbose_name="创建时间", help_text='创建时间')
    is_show = models.CharField(max_length=1, default='0', verbose_name="其余人是否可见,默认为0；0：不可见，1：可见",
                               help_text="其余人是否可见,默认为0；0：不可见，1：可见")
    update_time = models.DateTimeField(auto_now=True, verbose_name="更新时间", help_text='更新时间')
    is_enable = models.CharField(max_length=1, default='1', verbose_name="是否启用；1：启用，0：不启用", help_text="是否启用；1：启用，0：不启用")
    is_delete = models.CharField(max_length=1, default='0', verbose_name="是否删除；1：删除，0：不删除", help_text="是否删除；1：删除，0：不删除")

    class Meta:
        db_table = 'TestPlane'  # 指明数据库表名
        verbose_name = '测试计划表'  # 在admin站点中显示的名称

    def __str__(self):
        """定义每个数据对象的显示信息"""
        return self.test_plane


class TestPlaneInfo(models.Model):
    """测试计划信息表"""
    test_plane_id = models.IntegerField(verbose_name="测试计划id")
    env = models.CharField(max_length=10, default='qa', verbose_name='用例执行环境，qa：测试环境，release：线上环境',
                           help_text='用例执行环境，默认qa；qa：测试环境，release：线上环境')
    test_global = models.CharField(max_length=500, null=True, verbose_name='当前计划全局变量，以字典形式存放；eg：{"host1":"www",}',
                                   help_text='当前计划全局变量，以字典形式存放；eg：{"host1":"www",}')
    login_info = models.CharField(max_length=200, null=True, verbose_name="存放接口验证的token、session、cookie等验证信息",
                                  help_text="存放接口验证的token、session、cookie等验证信息")

    class Meta:
        db_table = 'TestPlaneInfo'
        verbose_name = "测试计划信息表"

    def __str__(self):
        return u"%s"%self.test_plane_id


class TestCase(models.Model):
    """测试用例表"""
    test_plane_id = models.IntegerField(verbose_name="测试计划id", help_text="测试计划id")
    case_name = models.CharField(max_length=50, verbose_name="用例名称", help_text="用例名称")
    case_description = models.CharField(max_length=500, null=True, verbose_name="用例描述", help_text="用例描述")
    host = models.CharField(max_length=50, null=True, verbose_name="接口host", help_text="接口host")
    api = models.CharField(max_length=100, null=True, verbose_name="接口地址", help_text="接口地址")
    request_method = models.CharField(max_length=6, verbose_name="请求方式;eg:get", help_text="请求方式;eg:get")
    request_type = models.CharField(max_length=50, null=True, verbose_name="请求类型;eg:post请求类型的x-www-from-urlencoded",
                                    help_text="请求类型;eg:post请求类型的x-www-from-urlencoded")
    data = models.CharField(max_length=500, null=True, verbose_name="请求数据", help_text="请求数据")
    result = models.CharField(max_length=200, verbose_name="断言（预期结果）；字典形式存放，eg：{'code':200,'msg':'成功'}",
                              help_text="断言（预期结果）；字典形式存放，eg：{'code':200,'msg':'成功'}")
    creator = models.CharField(max_length=10, verbose_name="创建人", help_text="创建人")
    create_time = models.DateTimeField(auto_now_add=True, verbose_name="创建时间", help_text="创建时间")
    is_enable = models.CharField(max_length=1, default='1', verbose_name="是否启用；1：启用，0：不启用",
                                 help_text="是否启用；默认为1；1：启用，0：不启用")
    update_time = models.DateTimeField(auto_now=True, verbose_name="更新时间", help_text="更新时间")
    is_delete = models.CharField(max_length=1, default='0', verbose_name="是否删除；1：删除，0：不删除",
                                 help_text="是否删除；默认为0；1：删除，0：不删除")

    class Meta:
        db_table = 'TestCase'
        verbose_name = "测试用例表"

    def __str__(self):
        return self.case_name
