"""Protocol enumeration."""

from enum import Enum


class ProtocolType(str, Enum):
    """Network protocol types."""
    
    TCP = "tcp"
    UDP = "udp"
    ICMP = "icmp"
    GRE = "gre"
    ESP = "esp"
    AH = "ah"
    SCTP = "sctp"
    OSPF = "ospf"
    IGMP = "igmp"
    PIM = "pim"
    VRRP = "vrrp"
    EIGRP = "eigrp"
    L2TP = "l2tp"
    VXLAN = "vxlan"
    OTHER = "other"