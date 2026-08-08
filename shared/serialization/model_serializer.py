"""Model-specific serialization utilities."""

from typing import Type, Union
from pydantic import BaseModel
from .json_serializer import serialize_to_json, deserialize_from_json


def serialize_model(model: BaseModel) -> str:
    """Serialize a Pydantic model to JSON string.
    
    Args:
        model: The Pydantic model instance to serialize
        
    Returns:
        JSON string representation of the model
    """
    return serialize_to_json(model)


def deserialize_model(model_class: Type[BaseModel], json_string: str) -> BaseModel:
    """Deserialize a JSON string to a Pydantic model.
    
    Args:
        model_class: The Pydantic model class to deserialize into
        json_string: JSON string to deserialize
        
    Returns:
        Instance of the specified model class
    """
    return deserialize_from_json(model_class, json_string)