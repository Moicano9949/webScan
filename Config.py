import os

# List of common ports
puertos = [
    9949, 20, 21, 22, 3306, 23, 80, 25, 5432, 139, 445, 111, 5900, 1521, 1433, 27017,
    6379, 9042, 50000, 8091, 11210, 513, 443, 990, 465, 110, 995, 143, 993, 8009, 8080,
    1025, 2049, 2000, 3260, 69, 161, 68, 123, 137, 138, 162, 512, 514, 873, 2048, 3305,
    5433, 8081, 8443, 9080, 9081, 50070, 50075, 50030, 50060, 2222, 8022, 8888, 9090,
    8008, 10000, 54321, 20031, 6660, 6661, 6662, 6663, 6664, 6665, 6666, 6667, 6668, 6669,
    6670, 11211, 9092, 9093, 9094, 9095, 9096, 9097, 9098, 9099,]

# Class for colored terminal output
class C:
    R = "\033[31m"  # Red
    G = "\033[32m"  # Green
    C = "\033[36m"  # Cyan
    W = "\033[97m"  # White
    Y = "\033[33m"  # Yellow
    A = "\033[34m"  # Blue
    S = "\033[1m"   # Bright
    B = "\033[30m"  # Black
    T = "\033[0m"   # RESET
    M = "\033[35m"  # Purple
    N = "\033[38;5;208m"  # Orange
    RS = "\033[38;5;218m"  # Rose
    D = "\033[38;5;220m"  # Gold
    P = "\033[38;5;245m"  # Silver
    MR = "\033[38;5;94m"  # Brown
    TQ = "\033[38;5;45m"  # Turquoise
    BR = "\033[38;5;83m"  # Beryl
    I = "\033[7m"   # Inverted
    GC = "\033[38;5;250m"  # Light gray

    # Intense colors
    R1 = "\033[91m"  # Red (more intense)
    G1 = "\033[92m"  # Green (more intense)
    C1 = "\033[96m"  # Cyan (more intense)
    Y1 = "\033[93m"  # Yellow (more intense)
    A1 = "\033[94m"  # Blue (more intense)
    B1 = "\033[90m"  # Black (more intense)
    M1 = "\033[95m"  # Purple (more intense)

    # Symbols for console output
    AL = f"{R}{S}[{T}{Y}{S}!{T}{R}{S}]{T}"  # Alert
    ALO = f"{A}{S}[{T}{G}{S}+{T}{A}{S}]{T}"  # Arrow
    GN = f"{W}{S}[{T}{W}+{T}{W}{S}]{T}"  # Green node
    ERW = f"{W}{S}[{T}{R}{S}-{T}{W}{S}]{T}"  # Error warning
    LP = f"{C}═══════════════════════════════════{T}"  # Line
    CO = "====================="  # Divider
    L = f"{A}=========================================={T}"  # Line
    dir_A = os.path.dirname(__file__)  # Current directory

    # Help message with color codes
    H = f"""
    {R}R{T} - Red
    {G}G{T} - Green
    {C}C{T} - Cyan
    {W}W{T} - White
    {Y}Y{T} - Yellow
    {A}A{T} - Blue
    {S}S{T} - Bright
    {B}B{T} - Black
    {T}T{T} - RESET
    {M}M{T} - Purple
    {N}N{T} - Orange
    {RS}RS{T} - Rose
    {D}D{T} - Gold
    {P}P{T} - Silver
    {MR}MR{T} - Brown
    {TQ}TQ{T} - Turquoise
    {BR}BR{T} - Beryl
    {I}I{T} - Inverted
    {GC}GC{T} - Light gray
    {R1}R1{T} - Red (more intense)
    {G1}G1{T} - Green (more intense)
    {C1}C1{T} - Cyan (more intense)
    {Y1}Y1{T} - Yellow (more intense)
    {A1}A1{T} - Blue (more intense)
    {B1}B1{T} - Black (more intense)
    {M1}M1{T} - Purple (more intense)
    """

# List of user agents
USER_AGENTS = [
'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36',
'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36',
'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 Safari/537.36',
'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36',
'Mozilla/5.0 (Linux; Android 10; SM-A205U) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.105 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 9; SM-G960U) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.105 Mobile Safari/537.36',
'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36 Edg/86.0.622.63',
'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36',
'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.193 Safari/537.36',
'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36',
'Mozilla/5.0 (Linux; Android 8.0.0; SM-G950U) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.105 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 10; SM-G975U) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.105 Mobile Safari/537.36',
'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36',
'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36',
'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36',
'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36',
'Mozilla/5.0 (Linux; Android 9; SM-G960U) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 10; SM-G975U) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Mobile Safari/537.36',
'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.122 Safari/537.36',
'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36',
'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.122 Safari/537.36',
'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36',
'Mozilla/5.0 (Linux; Android 8.0.0; SM-G950U) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 10; SM-G975U) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Mobile Safari/537.36',
'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36',
'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.97 Safari/537.36',
'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36',
'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.97 Safari/537.36',
'Mozilla/5.0 (Linux; Android 9; SM-G960U) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 10; SM-G975U) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Mobile Safari/537.36',
'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 Safari/537.36',
'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36',
'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 Safari/537.36',
'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36',
'Mozilla/5.0 (Linux; Android 8.0.0; SM-G950U) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 10; SM-G975U) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Mobile Safari/537.36',
'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36',
'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36',
'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36',
'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36',
]
