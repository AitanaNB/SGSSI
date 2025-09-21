cadena = "RIJ AZKKZHC PIKCE XT ACKCUXJHX SZX, E NZ PEJXKE, PXGIK XFDKXNEQE RIPI RIPQEHCK ET OENRCNPI AXNAX ZJ RKCHXKCI AX CJAXDXJAXJRCE AX RTENX, E ACOXKXJRCE AXT RITEQIKERCIJCNPI OKXJHXDIDZTCNHE AX TE ACKXRRCIJ EJEKSZCNHE. AZKKZHC OZX ZJ OERHIK AX DKCPXK IKAXJ XJ XT DEDXT AX TE RTENX IQKXKE XJ REHETZJVE XJ GZTCI AX 1936. DXKI AZKKZHC, RIPI IRZKKX RIJ TEN DXKNIJETCAEAXN XJ TE MCNHIKCE, JI REVI AXT RCXTI. DXKNIJCOCREQE TE HKEACRCIJ KXvITZRCIJEKCE AX TE RTENX IQKXKE. NZ XJIKPX DIDZTEKCAEA XJHKX TE RTENX HKEQEGEAIKE, KXOTXGEAE XJ XT XJHCXKKI PZTHCHZACJEKCI XJ QEKRXTIJE XT 22 AX JIvCXPQKX AX 1936, PZXNHKE XNE CAXJHCOCRERCIJ. NZ PZXKHX OZX NCJ AZAE ZJ UITDX IQGXHCvI ET DKIRXNI KXvITZRCIJEKCI XJ PEKRME. NCJ AZKKZHC SZXAI PEN TCQKX XT REPCJI DEKE SZX XT XNHETCJCNPI, RIJ TE RIPDTCRCAEA AXT UIQCXKJI AXT OKXJHX DIDZTEK V AX TE ACKXRRCIJ EJEKSZCNHE, HXKPCJEKE XJ PEVI AX 1937 TE HEKXE AX TCSZCAEK TE KXvITZRCIJ, AXNPIKETCLEJAI E TE RTENX IQKXKE V OERCTCHEJAI RIJ XTTI XT DINHXKCIK HKCZJOI OKEJSZCNHE."

letras=dict()
cont=0

for letra in cadena:
        if letra.isalpha(): #igorar los caracteres que no son letras
            if letra in letras:
                if letras[letra]==1:
                    cont +=1
                letras[letra]+=1
            else:
                letras[letra]=1

print('Frecuencia de letras:')
letras= sorted(letras, key=letras.get, reverse=True)
print(letras)
print('\n')
print(cadena)
print('\n')

frecs= ['E', 'A', 'O', 'S', 'N', 'R', 'I', 'L', 'D', 'C', 'T', 'U', 'M', 'P', 'B', 'G', 'V', 'Y', 'Q', 'H', 'F', 'Z', 'J', 'Ñ', 'X', 'K', 'W']
reps=  ['X', 'E', 'A', 'C', 'I', 'J', 'K', 'T', 'Z', 'R', 'N', 'H', 'P', 'D', 'Q', 'O', 'S', 'G', 'V', 'U', 'M', 'F', 'L'] #caracteres mas repetidos


    
# cadena1=cadena.replace('X','E') no se puede hacer porque se vuelven a sustituir los caracertes, mejor ir uno por uno

texto_descifrado = ""
for caracter in cadena:
    match caracter:                         #caracteres originales
        case 'X': texto_descifrado += 'E'
        case 'E': texto_descifrado += 'A'
        case 'A': texto_descifrado += 'D'   #o
        case 'C': texto_descifrado += 'I'   #s
        case 'I': texto_descifrado += 'O'   #n
        case 'J': texto_descifrado += 'N'   #r
        case 'K': texto_descifrado += 'R'   #i
        case 'T': texto_descifrado += 'L'   #l
        case 'Z': texto_descifrado += 'U'   #d,i
        case 'R': texto_descifrado += 'C'
        case 'N': texto_descifrado += 'S'   #t
        case 'H': texto_descifrado += 'T'   #u
        case 'P': texto_descifrado += 'M'
        case 'D': texto_descifrado += 'P'
        case 'Q': texto_descifrado += 'B'
        case 'O': texto_descifrado += 'F'   #g
        case 'S': texto_descifrado += 'Q'   #v
        case 'G': texto_descifrado += 'J'   #y
        case 'V': texto_descifrado += 'Y'   #q
        case 'U': texto_descifrado += 'G'   #h
        case 'M': texto_descifrado += 'H'   #f
        case 'F': texto_descifrado += 'X'   #z
        case 'L': texto_descifrado += 'Z'   #j
        # case 'Y': texto_descifrado += 'X'
        # case 'W': texto_descifrado += 'K'
        # case 'Ñ': texto_descifrado += 'Ñ'
        case _: texto_descifrado += caracter  # Mantener otros caracteres

print("TEXTO DESCIFRADO:")
print(texto_descifrado)


