def translate_integer_to_english(num):
    Combo = {
        1000000000: "Billion",
           1000000: "Million",
              1000: "Thousand",
    }
    Mono = {
               100: "Hundred",
                90: "Ninety",
                80: "Eighty",
                70: "Seventy",
                60: "Sixty",
                50: "Fifty",
                40: "Forty",
                30: "Thirty",
                20: "Twenty",
                19: "Nineteen",
                18: "Eighteen",
                17: "Seventeen",
                16: "Sixteen",
                15: "Fifteen",
                14: "Fourteen",
                13: "Thirteen",
                12: "Twelve",
                11: "Eleven",
                10: "Ten",
                 9: "Nine",
                 8: "Eight",
                 7: "Seven",
                 6: "Six",
                 5: "Five",
                 4: "Four",
                 3: "Three",
                 2: "Two",
                 1: "One",
    }

    def monoToEn(num):
        for n in Mono:
            k, num = divmod(num, n)
            if not k:    continue
            if n == 100: en.append(f"{Mono[k]} {Mono[n]} ")
            else:        en.append(f"{Mono[n]} ")

    if not num: return "Zero"
    en = []
    for n in Combo:
        k, num = divmod(num, n)
        if not k: continue
        monoToEn(k)
        en.append(f"{Combo[n]} ")
    if num: monoToEn(num)
    return "".join(en).rstrip()
