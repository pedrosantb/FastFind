import enum


class Status(enum.Enum):
    """Enum to represents the status of a item or list."""
    PENDING = "Pending"
    DONE = "Done"
    CANCELLED = "Cancelled"