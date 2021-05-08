# coding: utf-8
# -----------------------
# @project：zeyanTestPlatform
# @Author ： lizheyan
# @File ：serializer.py
# @Time ： 2021/05/02 22:31:59
# -----------------------
from rest_framework import serializers

from testPlatform.models import TestCase, TestPlane, TestPlaneInfo


def only_input_0_or_1(value: str):
    if value not in ['0', '1']:
        raise serializers.ValidationError("传参错误;该字段只能传0或1")
    return value


class TestPlaneInfoSerializer(serializers.Serializer):
    '''测试计划信息表序列化器'''

    def validate_env(self, value):  # 单一字段校验 {'env':1,'login_info':'登录信息'}
        if value not in ['qa', 'release']:
            raise serializers.ValidationError("传参错误;env字段只能传qa或release")
        return value

    def validate_test_plane_id(self,test_plane_id_value):
        test_plane_id = [test_plane_id.id for test_plane_id in TestPlane.objects.all()]
        if test_plane_id_value not in test_plane_id:
            raise serializers.ValidationError("test_plane_id不存在")
        return test_plane_id_value

    test_plane_id = serializers.IntegerField(help_text='测试计划id', write_only=True)
    env = serializers.CharField(help_text='用例执行环境，qa：测试环境，release：线上环境', max_length=10)
    test_global = serializers.CharField(help_text='当前计划全局变量，以字典形式存放；eg：{"host1":"www",}', max_length=500)
    login_info = serializers.CharField(help_text='存放接口验证的token、session、cookie等验证信息', max_length=200)

    def create(self, validated_data):
        # 保存数据
        return TestPlaneInfo.objects.create(**validated_data)




class TestPlaneSerializer(serializers.Serializer):
    '''测试计划序列化器'''

    id = serializers.IntegerField(help_text='测试计划id', read_only=True)
    test_plane = serializers.CharField(help_text='测试计划名称', max_length=20)
    test_plane_description = serializers.CharField(help_text='测试计划描述', max_length=100, required=False,allow_null=True)
    creator = serializers.CharField(help_text='创建人', max_length=10)
    create_time = serializers.DateTimeField(help_text='创建时间', read_only=True)
    is_show = serializers.CharField(help_text='其余人是否可见,默认为0；0：不可见，1：可见', max_length=1, validators=[only_input_0_or_1],
                                    required=False)
    update_time = serializers.DateTimeField(help_text='更新时间', read_only=True)
    is_enable = serializers.CharField(help_text='是否启用；1：启用，0：不启用', max_length=1, validators=[only_input_0_or_1],
                                      required=False)
    is_delete = serializers.CharField(help_text='是否删除；1：删除，0：不删除', max_length=1, validators=[only_input_0_or_1],
                                      required=False)

    def create(self, validated_data):
        # 保存数据
        return TestPlane.objects.create(**validated_data)


class TestCaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = TestCase
        fields = '__all__'
