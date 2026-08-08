"""JSON serialization utilities for shared models."""

import json
from typing import Dict, Any, Type, Union
from pydantic import BaseModel
from datetime import datetime


def serialize_to_json(model: BaseModel) -> str:
    """Serialize a Pydantic model to JSON.
    
    Args:
        model: The Pydantic model instance to serialize
        
    Returns:
        JSON string representation of the model
    """
    return model.model_dump_json(indent=2)


def deserialize_from_json(model_class: Type[BaseModel], json_string: str) -> BaseModel:
    """Deserialize a JSON string to a Pydantic model.
    
    Args:
        model_class: The Pydantic model class to deserialize into
        json_string: JSON string to deserialize
        
    Returns:
        Instance of the specified model class
    """
    data = json.loads(json_string)
    return model_class(**data)


def serialize_dict_to_json(data: Dict[str, Any]) -> str:
    """Serialize a dictionary to JSON.
    
    Args:
        data: Dictionary to serialize
        
    Returns:
        JSON string representation of the dictionary
    """
    return json.dumps(data, ensure_ascii=False, indent=2, default=str)


def deserialize_json_to_dict(json_string: str) -> Dict[str, Any]:
    """Deserialize a JSON string to a dictionary.
    
    Args:
        json_string: JSON string to deserialize
        
    Returns:
        Dictionary representation of the JSON
    """
    return json.loads(json_string)