"""Connection state enumeration."""

from enum import Enum


class ConnectionState(str, Enum):
    """Connection state types."""
    
    NEW = "new"
    ESTABLISHED = "established"
    RELATED = "related"
    INVALID = "invalid"
    UNTRACKED = "untracked"
    SYN_SENT = "syn_sent"
    SYN_RECV = "syn_recv"
    FIN_WAIT_1 = "fin_wait_1"
    FIN_WAIT_2 = "fin_wait_2"
    TIME_WAIT = "time_wait"
    CLOSE_WAIT = "close_wait"
    LAST_ACK = "last_ack"
    CLOSE = "close"