
import string

#Using maketrans and  translate methond in string

text = """g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr
amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q
ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb.
lmu ynnjw ml rfc spj."""
table = "".maketrans(string.ascii_lowercase,string.ascii_lowercase[2:]+string.ascii_lowercase[:2])
print(text.translate(table))


#Using normal way to solve the approach 

alph = list(string.ascii_lowercase)
new_data = []
challenge = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."

for data in challenge.split(" "):
    val =''
    for d in data:
        if d in alph:
            val = val + alph[(alph.index(d) + 2)%26]
        else:
            val = val+d
    new_data.append(val)
print(" ".join(new_data))           
