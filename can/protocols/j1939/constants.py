# transport protocol PGNs
PGN_TP_CONNECTION_MANAGEMENT = 0xec00
PGN_TP_DATA_TRANSFER = 0xeb00

# address claim PGNs
PGN_AC_ADDRESS_CLAIMED = 0xee00
PGN_AC_COMMANDED_ADDRESS = 0xfed8

PGN_REQUEST_FOR_PGN = 0xea00

pgn_strings = {
    PGN_TP_CONNECTION_MANAGEMENT: "PGN_TP_CONNECTION_MANAGEMENT",
    PGN_TP_DATA_TRANSFER: "PGN_TP_DATA_TRANSFER",
    PGN_AC_ADDRESS_CLAIMED: "PGN_AC_ADDRESS_CLAIMED",
    PGN_AC_COMMANDED_ADDRESS: "PGN_AC_COMMANDED_ADDRESS",
    PGN_REQUEST_FOR_PGN: "PGN_REQUEST_FOR_PGN"
}

DESTINATION_ADDRESS_NULL = 254
DESTINATION_ADDRESS_GLOBAL = 255

ADDRESS_UNCLAIMED = -1

# connection management message types
CM_MSG_TYPE_RTS = 0x10
CM_MSG_TYPE_CTS = 0x11
CM_MSG_TYPE_EOM_ACK = 0x13
CM_MSG_TYPE_BAM = 0x20
CM_MSG_TYPE_ABORT = 0xff

# connection abort reasons
CM_ABORT_UNKNOWN = 0
CM_ABORT_SESSION_IN_PROGRESS = 1
CM_ABORT_NO_RESOURCES = 2
CM_ABORT_TIMEOUT = 3
CM_ABORT_SAE_RESERVED_START = 4
CM_ABORT_SAE_RESERVED_END = 250
CM_ABORT_J1939_71_RESERVED_START = 251
CM_ABORT_J1939_71_RESERVED_END = 255

INDUSTRY_GROUP_GLOBAL = 0
INDUSTRY_GROUP_HIGHWAY = 1
INDUSTRY_GROUP_AGRICULTURAL = 2
INDUSTRY_GROUP_CONSTRUCTION = 3
INDUSTRY_GROUP_MARINE = 4
INDUSTRY_GROUP_INDUSTRIAL = 5
INDUSTRY_GROUP_RESERVED_1 = 6
INDUSTRY_GROUP_RESERVED_2 = 7

j1939_industry_groups = {
    INDUSTRY_GROUP_GLOBAL: "INDUSTRY_GROUP_GLOBAL",
    INDUSTRY_GROUP_HIGHWAY: "INDUSTRY_GROUP_HIGHWAY",
    INDUSTRY_GROUP_AGRICULTURAL: "INDUSTRY_GROUP_AGRICULTURAL",
    INDUSTRY_GROUP_CONSTRUCTION: "INDUSTRY_GROUP_CONSTRUCTION",
    INDUSTRY_GROUP_MARINE: "INDUSTRY_GROUP_MARINE",
    INDUSTRY_GROUP_INDUSTRIAL: "INDUSTRY_GROUP_INDUSTRIAL",
    INDUSTRY_GROUP_RESERVED_1: "INDUSTRY_GROUP_RESERVED_1",
    INDUSTRY_GROUP_RESERVED_2: "INDUSTRY_GROUP_RESERVED_2"
}
