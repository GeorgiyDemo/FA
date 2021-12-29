from bs4 import BeautifulSoup
from typing import List
from enum import Enum

class BSTypes(Enum):
    TAG = "tag"
    ATTR = "attribute"

XML_FIELDS_LIST = [
    {"name":"id", "type":BSTypes.TAG},
    {"name":"username", "type" : BSTypes.TAG},
    {"name": "name", "type" : BSTypes.TAG},
    {"name": "sex", "type" : BSTypes.TAG},
    {"name" : "country", "type" : BSTypes.TAG},
    {"name": "mail", "type" : BSTypes.TAG},
    {"name": "registered", "type" : BSTypes.TAG},
    {"name" : "birthdate", "type": BSTypes.TAG},
    {"name": "prefix", "type" : BSTypes.ATTR, "parent" : None},
    {"name": "code", "type" : BSTypes.ATTR, "parent" : "country"},
]

def xml2dict(path: str) -> List[dict]:
    content = open(path,"r").read()
    soup = BeautifulSoup(content,'xml')
    result_list = []
    
    for user in soup.find_all('user'):
        current_dict = {}
        
        for item in XML_FIELDS_LIST:
            
            #Если это обыкновенный тег
            if item["type"] == BSTypes.TAG:
                item_name = item["name"]
                current_obj = user.find(item_name)
                if current_obj is not None:
                    current_dict[item_name] = current_obj.get_text()
            
            # Если это атрибут, то сначала стучимся к родителю
            else:
                
                #Если у элемента нет родителя, то родителем будет сам текущий элемент user
                item_parent = user.find(item["parent"]) if item["parent"] is not None else user
                item_name = item["name"]
                
                #Проверки на None т.к. не факт, что у текущего user будет такой родитель и атрибут
                if item_parent is not None:
                    current_obj = item_parent.get(item_name)
                    if current_obj is not None:
                        current_dict[item_name] = current_obj

        result_list.append(current_dict)
    
    return result_list
