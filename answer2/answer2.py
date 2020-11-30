start_string = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj\n"

for s in start_string:
    if ord(s) > 96 and ord(s) < 123:
        print(chr((ord(s) - 96 + 2)%26 + 96), end='')
    else:
        print(s, end='')


start_string = "http://www.pythonchallenge.com/pc/def/map.html"
intab ='abcdefghijklmnopqrstuvwxyz'
outtab = 'cdefghijklmnopqrstuvwxyzab'
transtab = str.maketrans(intab, outtab)
out = start_string.translate(transtab)
print(out)
