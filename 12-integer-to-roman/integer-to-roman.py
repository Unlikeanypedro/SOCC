class Solution(object):
    def intToRoman(self, num):

        def pega_valor(index, digit, tamanho):
            result = int(digit) * (10 ** ((tamanho - index) - 1))
            return result
        
        def retorna_romano(decomposto):
            romano = ""

            i = 0

            while i < len(decomposto):

                if decomposto[i] >= 900:
                    if decomposto[i] == 900:
                        romano += "CM"
                        Uni = 0.9

                    else:
                        Uni = decomposto[i] // 1000
                        romano += Uni * "M"

                    decomposto[i] -= int(Uni * 1000)

                elif decomposto[i] >= 400:
                    if decomposto[i] == 400:
                        romano += "CD"
                        Uni = 0.8

                    else:
                        Uni = decomposto[i] // 500
                        romano += Uni * "D"

                    decomposto[i] -= int(Uni * 500)

                elif decomposto[i] >= 90:
                    if decomposto[i] == 90:
                        romano += "XC"
                        Uni = 0.9

                    else:
                        Uni = decomposto[i] // 100
                        romano += Uni * "C"

                    decomposto[i] -= int(Uni * 100)

                elif decomposto[i] >= 40:
                    if decomposto[i] == 40:
                        romano += "XL"
                        Uni = 0.8

                    else:
                        Uni = decomposto[i] // 50
                        romano += Uni * "L"

                    decomposto[i] -= int(Uni * 50)

                elif decomposto[i] >= 9:
                    if decomposto[i] == 9:
                        romano += "IX"
                        Uni = 0.9

                    else:
                        Uni = decomposto[i] // 10
                        romano += Uni * "X"

                    decomposto[i] -= int(Uni * 10)

                elif decomposto[i] >= 4:
                    if decomposto[i] == 4:
                        romano += "IV"
                        Uni = 0.8

                    else:
                        Uni = decomposto[i] // 5
                        romano += Uni * "V"

                    decomposto[i] -= int(Uni * 5)

                elif decomposto[i] >= 0:
                    if decomposto[i] == 0:
                        romano += ""
                        Uni = 0

                    else:
                        Uni = decomposto[i]
                        romano += Uni * "I"

                    decomposto[i] -= int(Uni)
                
                if decomposto[i] == 0:
                    i += 1

            return romano

        num = str(num)
        decomposto = []

        for index, digit in enumerate(num):
            fator = pega_valor(index, digit, len(num))
            decomposto.append(fator)

        return retorna_romano(decomposto)