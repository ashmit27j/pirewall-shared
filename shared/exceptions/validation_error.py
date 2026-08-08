"""Validation error exceptions."""

class ValidationError(Exception):
    """Exception raised when data validation fails."""
    
    def __init__(self, message: str, field: str = None):
        """
        Initialize validation error.
        
        Args:
            message: Error message
            field: Field that failed validation (optional)
        """
        self.message = message
        self.field = field
        super().__init__(self.message)