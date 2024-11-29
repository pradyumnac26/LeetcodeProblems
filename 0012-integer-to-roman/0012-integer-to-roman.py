class Solution:
    def intToRoman(self, num: int) -> str:
        value_to_roman = [
        (1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'),
        (100, 'C'), (90, 'XC'), (50, 'L'), (40, 'XL'),
        (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'), (1, 'I')
        ]
    
        result = []
    
        for value, roman in value_to_roman:
        # Append the Roman numeral as many times as the value fits into num
            while num >= value:
                result.append(roman)
                num -= value
    
        return ''.join(result)

        