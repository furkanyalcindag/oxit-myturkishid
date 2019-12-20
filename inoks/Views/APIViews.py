from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.views import APIView

from inoks.models import Profile, OrderProduct
from inoks.models.MemberApiObject import MemberApiObject
from inoks.models.OrderProductObject import OrderProductObject
from inoks.serializers.ApiSerializer import OrderMemberSerializer, OrderProductSerializer


@api_view(http_method_names=['POST'])
def get_address_info(request):
    if request.POST:
        try:

            id = request.POST.get('id')
            profile = Profile.objects.get(pk=id)

            member = MemberApiObject(district=profile.district, city=profile.city.id, address=profile.address)

            data = OrderMemberSerializer(member)

            responseData = dict()
            responseData['member'] = data.data

            return JsonResponse(responseData, safe=True)

        except Exception as e:

            return JsonResponse({'status': 'Fail', 'msg': e})


class get_order_products(APIView):

    def get(self, request, format=None):

        try:

            order_products = OrderProduct.objects.filter(order__id=request.query_params['id'])
            products = []

            for product in order_products:
                order_product_object = OrderProductObject(product_name=product.product.name, quantity=product.quantity)
                products.append(order_product_object)

            serializer = OrderProductSerializer(products, many=True)

            return Response(serializer.data, status=status.HTTP_200_OK)

        except Exception as e:

            return JsonResponse({'status': 'Fail', 'msg': e})
