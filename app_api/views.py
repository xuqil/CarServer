from django.http import HttpResponse
from .models import Park, AntiPark
from django.core.exceptions import ObjectDoesNotExist
from django.views import View


from django.forms.models import model_to_dict
import xml.dom.minidom
from xml.dom.minidom import parse


class PushApi(View):

    def get(self, request, *args, **kwargs):
        park_list = {}
        count = Park.objects.all().count()
        for i in range(count):
            statues = {}
            park_data = Park.objects.filter(park_id=i + 1).first()
            if park_data.status:
                anti = AntiPark.objects.filter(license_number=park_data.license_number).first()
                if anti is not None:
                    print(anti.anti_num)
                    statues["anti_number"] = anti.anti_num
                else:
                    statues["anti_number"] = 0
            else:
                statues["anti_number"] = 0
            statues["status"] = park_data.status
            statues["license_number"] = park_data.license_number
            park_list[i+1] = statues
        print(park_list)
        context = None
        return HttpResponse(context, content_type="text/xml")







#
#
#
# def servers_app(request):
#     """
#     服务器与APP的对接函数
#     :param request: 各停车位id
#     :return: 各停车位是否被占用
#     """
#     servers_park_test()
#
#     ls = []
#     try:
#         id_number = Park.objects.all()
#         # print(len(id_number))
#         for id in range(len(id_number)):
#             #linux中该数据库id从0开始
#             id = id
#             # print("id" + str(id + 1))
#             park_offon = Park.objects.all().get(id=id)
#             mydata = model_to_dict(park_offon)
#             # print(mydata)
#             ls.append(mydata)
#             # print(ls)
#
#     except ObjectDoesNotExist:
#         return HttpResponse("error", content_type="text/xml")
#     else:
#         # 在内存中创建一个空的文档
#         doc = xml.dom.minidom.Document()
#         # 创建一个根节点Managers对象
#         root = doc.createElement('park_server')
#         # 设置根节点的属性
#         root.setAttribute('name', 'Park')
#         root.setAttribute('id', 'id')
#         # 将根节点添加到文档对象中
#         doc.appendChild(root)
#         j = 0
#         for i in ls:
#             nodeHeart = doc.createElement('park_part'+str(j))
#             nodeName = doc.createElement('park_id')
#             # 给叶子节点name设置一个文本节点，用于显示文本内容
#             nodeName.appendChild(doc.createTextNode(str(i['id'])))
#
#             nodeTf = doc.createElement("park_tf")
#             nodeTf.appendChild(doc.createTextNode(str(i["park_id"])))
#
#             # 将各叶子节点添加到父节点Manager中，
#             # 最后将Manager添加到根节点Managers中
#             nodeHeart.appendChild(nodeName)
#             nodeHeart.appendChild(nodeTf)
#             root.appendChild(nodeHeart)
#
#             j = j + 1
#
#         with open('park.xml', 'w') as f:
#             doc.writexml(f, addindent=' ', newl='\n', encoding="utf-8")
#
#         # 将xml转为字符串
#         doc = parse('park.xml')
#         doc_xml = doc.toprettyxml(encoding="utf-8")
#
#         return HttpResponse(doc_xml, content_type="text/xml")
#
#
# def servers_park_test():
#     park = []
#
#     with open("F:\资料\广电设\CarServer\\app_api\\a.txt") as f:
#         for lines in f.readlines():
#             data = lines.split('.')
#             print(data)
#             for line in data:
#                 print(line)
#                 if line != '\n':
#                     park.append(line)
#                 print(park)
#         a = 0
#         d = 0
#         if park[0] == 'a0':
#             a = 0
#         else:
#             a = 1
#         if park[1] == 'b0':
#             b = 0
#         else:
#             b = 1
#         print(a)
#         print(b)
#         servers_change(0, a)
#         servers_change(1, b)
#
#
# def servers_change(pk, update):
#     park_offon = Park.objects.get(park_id=pk)
#     park_offon.park_id = update
#     park_offon.save()
#     print("修改成功")
#
#
# def servers_park(request):
#     """
#     服务器对接停车场系统
#     :param request: 停车位id及更新的数据
#     :return: 可有可无
#     """
#     park_id = request.POST.get('pk')
#     park_update = request.POST.get('update')
#     print(park_update)
#     try:
#         park_offon = Park.objects.get(id=park_id)
#         park_offon.park_id = park_update
#         park_offon.save()
#     except ObjectDoesNotExist:
#         return HttpResponse("error", content_type="text/xml")
#     else:
#         print(park_offon)
#     return HttpResponse("修改成功", content_type="text/xml")
#
#
# def servers_test(request):
#     """
#     数据库初始化函数
#     :param request:
#     :return:
#     """
#     park_id = request.POST.get('pk')
#     park_offon = request.POST.get('park_offon')
#     print(park_offon)
#     try:
#         Park.objects.get(id=park_id)
#     except ObjectDoesNotExist:
#         print(park_id)
#         Park.objects.create(id=park_id, park_id=park_offon)
#         return HttpResponse("注入成功", content_type="text/xml")
#     else:
#         return HttpResponse("ID已存在", content_type="text/xml")
#
#
# def servers_delete(request):
#     """
#     数据库删除函数
#     :param request:
#     :return:
#     """
#     park_id = request.POST.get('pk')
#     try:
#         Park.objects.get(id=park_id)
#     except ObjectDoesNotExist:
#         return HttpResponse("ID不存在", content_type="text/xml")
#     else:
#         Park.objects.filter(id=park_id).delete()
#         return HttpResponse("删除成功", content_type="text/xml")
