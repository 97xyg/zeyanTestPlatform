# Create your views here.
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.generics import ListCreateAPIView, UpdateAPIView
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView

from testPlatform.models import TestPlane, TestCase, TestPlaneInfo
from testPlatform.serializer import TestPlaneSerializer, TestPlaneInfoSerializer, TestCaseSerializer
from zeyanTestPlatform.common.paging import MyPageNumberPagination


class TestPlaneView(APIView):
    '''
    get:
    返回测试计划。

    post:
    新建测试计划
    '''

    def get(self, request):
        test_planes = TestPlane.objects.filter(is_show=0, is_enable=1, is_delete=0)  # 获取所有正常数据
        page = MyPageNumberPagination()  # 创建分页对象
        resp = page.paginate_queryset(queryset=test_planes, request=request, view=self)  # 在数据库中获取分页数据
        ser = TestPlaneSerializer(resp, many=True)
        # return Response(ser.data)
        return page.get_paginated_response(ser.data)

    def post(self, request):
        data = request.data  # 获取前端数据
        ser = TestPlaneSerializer(data=data)  # 验证数据
        ser.is_valid(raise_exception=True)  # 验证方法
        ser.save()  # 保存数据
        return Response(ser.data)  # 返回结果


@api_view(['DELETE', 'PUT'])
def test_plane_detail(request, pk):
    """
    测试计划删除更新操作接口
    :param request: 请求对象
    :param pk: 路径参数
    :return:
    """
    try:
        test_plane = TestPlane.objects.get(id=pk)
    except TestPlane.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'DELETE':
        test_plane.is_delete = 1  # 1表示逻辑删除
        test_plane.save()
        return Response({'msg': "删除成功"})

    elif request.method == "PUT":
        ser = TestPlaneSerializer(test_plane, request.data)
        if ser.is_valid():
            test_plane.__dict__.update(**request.data)  # 更新多个字段，传几个更新几个
            test_plane.save()  # 保存结果
            return Response(ser.data)  # 返回结果
        return Response(ser.errors, status.HTTP_400_BAD_REQUEST)


class TestPlaneInfoView(APIView):
    '''
    post:
    测试计划详细信息创建
    '''

    def post(self, request):
        data = request.data  # 获取前端数据
        ser = TestPlaneInfoSerializer(data=data)  # 验证数据
        if ser.is_valid():  # 验证方法
            ser.save()  # 保存数据
            return Response(ser.data, status=status.HTTP_200_OK)  # 返回正常响应结果
        return Response(ser.errors, status=status.HTTP_400_BAD_REQUEST)  # 返回错误响应结果

    def delete(self, request: Request):
        pk = request.query_params.get("test_plane_id")
        try:
            test_plane_info = TestPlaneInfo.objects.get(id=pk)
            test_plane_info.delete()
        except TestPlaneInfo.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        return Response({'msg': "删除成功"})

    def get(self, request: Request):
        test_plane_id = request.query_params.get("test_plane_id")
        test_plane_info: TestPlaneInfo = TestPlaneInfo.objects.filter(test_plane_id=test_plane_id).first()
        ser = TestPlaneInfoSerializer(test_plane_info)
        return Response(ser.data)

    def put(self, request: Request):
        test_plane_id = request.data.get("test_plane_id")
        try:
            test_plane_info = TestPlaneInfo.objects.get(test_plane_id__exact=test_plane_id)
        except TestPlaneInfo.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        ser = TestPlaneInfoSerializer(test_plane_info, request.data)
        if ser.is_valid():
            test_plane_info.__dict__.update(**request.data)
            test_plane_info.save()
            return Response(ser.data)
        return Response(ser.errors)


class TestCaseView(ListCreateAPIView, UpdateAPIView):
    '''
    get:
    获取测试用例

    post:
    创建测试用例
    '''

    queryset = TestCase.objects.all().order_by('-create_time')
    serializer_class = TestCaseSerializer
    pagination_class = MyPageNumberPagination  # 分页

    def put(self, request: Request, *args, **kwargs):
        case_id = request.data.get("id")
        try:
            query_result = TestCase.objects.get(id=case_id)
        except TestCase.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        ser = self.serializer_class(query_result, request.data)
        if ser.is_valid():
            query_result.__dict__.update(**request.data)
            query_result.save()
            return Response(ser.data)
        return Response(ser.errors)
