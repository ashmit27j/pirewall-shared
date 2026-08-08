"""Version error exceptions."""

class VersionError(Exception):
    """Exception raised when version compatibility issues occur."""
    
    def __init__(self, message: str):
        """
        Initialize version error.
        
        Args:
            message: Error message
        """
        self.message = message
        super().__init__(self.message)