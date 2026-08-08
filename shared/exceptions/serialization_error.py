"""Serialization error exceptions."""

class SerializationError(Exception):
    """Exception raised when serialization/deserialization fails."""
    
    def __init__(self, message: str):
        """
        Initialize serialization error.
        
        Args:
            message: Error message
        """
        self.message = message
        super().__init__(self.message)