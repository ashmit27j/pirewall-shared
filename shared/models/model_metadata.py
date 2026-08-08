"""Model Metadata model for tracking ML model information."""

from __future__ import annotations

from datetime import datetime
from typing import Optional, Dict, Any
from pydantic import BaseModel, Field


class ModelMetadata(BaseModel):
    """Metadata about machine learning models used in the system."""

    # Model identification
    model_id: str = Field(..., description="Unique identifier for the model")
    model_name: str = Field(..., description="Name of the model")
    model_version: str = Field(..., description="Version of the model")
    
    # Model characteristics
    model_type: str = Field(..., description="Type of model (LightGBM, IsolationForest, etc.)")
    training_date: datetime = Field(..., description="Date when the model was trained")
    feature_count: int = Field(..., description="Number of features used by the model")
    
    # Performance metrics
    accuracy: Optional[float] = Field(None, description="Model accuracy (0.0-1.0)")
    precision: Optional[float] = Field(None, description="Model precision (0.0-1.0)")
    recall: Optional[float] = Field(None, description="Model recall (0.0-1.0)")
    
    # Deployment information
    deployed_date: Optional[datetime] = Field(None, description="Date when model was deployed")
    deployment_environment: str = Field(..., description="Environment where the model is deployed")
    
    # Additional metadata
    parameters: Dict[str, Any] = Field(default_factory=dict, description="Model parameters")
    tags: Dict[str, str] = Field(default_factory=dict, description="Tags for categorization")

    class Config:
        """Pydantic configuration."""
        use_enum_values = True
        validate_assignment = True