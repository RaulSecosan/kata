"""
Jaden Smith, the son of Will Smith, is the star of films such as The Karate Kid (2010) and After Earth (2013). Jaden is also known for some of his philosophy that he delivers via Twitter. When writing on Twitter, he is known for almost always capitalizing every word. For simplicity, you'll have to capitalize each word, check out how contractions are expected to be in the example below.

Your task is to convert strings to how they would be written by Jaden Smith. The strings are actual quotes from Jaden Smith, but they are not capitalized in the same way he originally typed them.

Example:

Not Jaden-Cased: "How can mirrors be real if our eyes aren't real"
Jaden-Cased:     "How Can Mirrors Be Real If Our Eyes Aren't Real"

Testing for 'RBwD A f GfDNFt jLR cj qGJvkOYi QRhlEyROQB gxgHoQ Xzu QlTupo bf trK oyKZjS yeIQ ltgdrepGMG PZyqtJGNI kcMnouKFsm NmIbaEGaUp rTTHChwAh'
Log
 RBwD A F GfDNFt JLR Cj QGJvkOYi QRhlEyROQB GxgHoQ Xzu QlTupo Bf TrK OyKZjS YeIQ LtgdrepGMG PZyqtJGNI KcMnouKFsm NmIbaEGaUp RTTHChwAh
'RBwD A F GfDNFt JLR Cj QGJvkOYi QRhlEyROQB GxgHoQ Xzu QlTupo Bf TrK OyKZjS YeIQ LtgdrepGMG PZyqtJGNI KcMnouKFsm NmIbaEGaUp RTTHChwAh' should equal 'Rbwd A F Gfdnft Jlr Cj Qgjvkoyi Qrhleyroqb Gxghoq Xzu Qltupo Bf Trk Oykzjs Yeiq Ltgdrepgmg Pzyqtjgni Kcmnoukfsm Nmibaegaup Rtthchwah'

"""
from numpy.ma.core import array


# def to_jaden_case(string):
#     text = string.split(" ")
#     txt = ""
#
#     for i in range(len(text)):
#         for j in range(len(text[i])):
#             if j == 0 :
#                 txt += " " + text[i][j].upper()
#             else:
#                 txt += text[i][j].lower()
#     print(txt)
#
#
#     return txt[1:]
def to_jaden_case(string):
    text = string.split(" ")
    txt = ""

    for word in text:
        for ind, letter in enumerate(word):
            # if ind == 0 :
            #     txt += " " + letter.upper()
            # else:
            #     txt += letter.lower()
           txt += " " + letter.upper() if ind == 0 else letter.lower()
    print(txt)

    return txt[1:]


print(to_jaden_case("How can mirrors be real if our eyes aren't real"))