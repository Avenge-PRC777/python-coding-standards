from typing import Any, List, Optional, Dict

class CustomDataType:
    value: str = "Hey"
    def __init__(self, value: str):
        self.value = value

def use_custom_data_type(obj: CustomDataType) -> CustomDataType:
    print(obj.value)
    return obj

custom_data_type = CustomDataType("Hello")
use_custom_data_type(custom_data_type)