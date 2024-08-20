import os

class C:
    R = "\033[31m"  # Rojo
    G = "\033[32m"  # Verde
    C = "\033[36m"  # Azul Cielo
    W = "\033[97m"  # Blanco
    Y = "\033[33m"  # Amarillo
    A = "\033[34m"  # Azul
    S = "\033[1m"   # Brillante
    B = "\033[30m"  # Negro
    T = "\033[0m"   # RESET
    M = "\033[35m"  # Morado
    N = "\033[38;5;208m"  # Naranja
    RS = "\033[38;5;218m"  # Rosa
    D = "\033[38;5;220m"  # Dorado
    P = "\033[38;5;245m"  # Plateado
    MR = "\033[38;5;94m"  # Marron
    TQ = "\033[38;5;45m"  # Turquesa
    BR = "\033[38;5;83m"  # Berilo
    I = "\033[7m"   # Invertido
    GC = "\033[38;5;250m"  # Gris claro

    R1 = "\033[91m"  # Rojo (más intenso)
    G1 = "\033[92m"  # Verde (más intenso)
    C1 = "\033[96m"  # Azul Cielo (más intenso)
    Y1 = "\033[93m"  # Amarillo (más intenso)
    A1 = "\033[94m"  # Azul (más intenso)
    B1 = "\033[90m"  # Negro (más intenso)
    M1 = "\033[95m"  # Morado (más intenso)

    AL = f"{R}{S}[{T}{Y}{S}!{T}{R}{S}]{T}"
    ALO = f"{A}{S}[{T}{G}{S}+{T}{A}{S}]{T}"
    GN = f"{W}{S}[{T}{W}+{T}{W}{S}]{T}"
    ERW = f"{W}{S}[{T}{R}{S}-{T}{W}{S}]{T}"
    LP = f"{C}═══════════════════════════════════{T}"
    CO = "====================="
    L = f"{A}=========================================={T}"
    dir_A = os.path.dirname(__file__)
    
    H = f"""
    {R}R{T} - Rojo
    {G}G{T} - Verde
    {C}C{T} - Azul Cielo
    {W}W{T} - Blanco
    {Y}Y{T} - Amarillo
    {A}A{T} - Azul
    {S}S{T} - Brillante
    {B}B{T} - Negro
    {T}T{T} - RESET
    {M}M{T} - Morado
    {N}N{T} - Naranja
    {RS}RS{T} - Rosa
    {D}D{T} - Dorado
    {P}P{T} - Plateado
    {MR}MR{T} - Marron
    {TQ}TQ{T} - Turquesa
    {BR}BR{T} - Berilo
    {I}I{T} - Invertido
    {GC}GC{T} - Gris claro
    {R1}R1{T} - Rojo (más intenso)
    {G1}G1{T} - Verde (más intenso)
    {C1}C1{T} - Azul Cielo (más intenso)
    {Y1}Y1{T} - Amarillo (más intenso)
    {A1}A1{T} - Azul (más intenso)
    {B1}B1{T} - Negro (más intenso)
    {M1}M1{T} - Morado (más intenso)
    """