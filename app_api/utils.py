import xml.etree.ElementTree as ET


def dict_to_xml(input_dict, root_tag, node_tag):
    """ 定义根节点root_tag，定义第二层节点node_tag
    第三层中将字典中键值对对应参数名和值
    return: xml的tree结构 """
    root_name = ET.Element(root_tag)
    for (k, v) in input_dict.items():
        node_name = ET.SubElement(root_name, node_tag)
        for key, val in v.items():
            key = ET.SubElement(node_name, key)
            key.text = val
    rough_string = ET.tostring(root_name, 'utf-8')
    return rough_string.decode('utf-8')
