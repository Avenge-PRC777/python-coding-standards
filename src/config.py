from dataclasses import dataclass
from enum import Enum
from typing import Any
import json

class AvailableOptions(Enum):
    ENABLE_FEATURE1 = "enable_feature1"
    ENABLE_FEATURE2 = "enable_feature2"

@dataclass
class Config:
    dataset_path: str = None
    options = []

    @staticmethod
    def set_values(json_obj: Any) -> 'Config':
        Config.dataset_path = json_obj.get('dataset_path')
        valid_options = [key.value for key in AvailableOptions]
        Config.options = json_obj.get('options', [])
        for option in Config.options:
            assert option in valid_options, f"Invalid option"
        Config.options = [AvailableOptions(option) for option in Config.options]

def set_values_from_jsonobj(config_file_path):
    json_obj = json.loads(open(config_file_path, 'r', encoding='utf-8').read().strip())
    Config.set_values(json_obj)