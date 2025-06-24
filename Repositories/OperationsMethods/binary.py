
class Binary:
    def __init__(self):
        pass


    def addition(self, value1):
        carry = 1
        result = ''
        for bit in reversed(value1):
            if bit == '0' and carry == 1:
                result = '1' + result
                carry = 0
            elif bit == '1' and carry == 1:
                result = '0' + result
                carry = 1
            else:
                result = bit + result
        if carry == 1:
            result = '1' + result
        return result.lstrip('0') or '0'

    def substraction(self, value1):
        if value1.lstrip('0') == '0':
            return '0'
        borrow = 1
        result = ''
        for bit in reversed(value1):
            if bit == '1' and borrow == 1:
                result = '0' + result
                borrow = 0
            elif bit == '0' and borrow == 1:
                result = '1' + result
                borrow = 1
            else:
                result = bit + result
        return result.lstrip('0') or '0'

        
    def product(self, value1):
        value2='1'
        if not all(c in '01' for c in value1) or not all(c in '01' for c in value2):
            raise ValueError("Solo se aceptan cadenas binarias.")

        if value2.strip('0') == '':
            return '0'

        result = '0'
        
        for i, bit in enumerate(reversed(value2)):
            if bit == '1':
                result = self.binaryAdd(result, value1 + '0' * i)
        return result.lstrip('0') or '0'

    def binaryAdd(self, a, b):
        maxLen = max(len(a), len(b))
        a = a.zfill(maxLen)
        b = b.zfill(maxLen)
        carry = 0
        result = ''
        for i in range(maxLen - 1, -1, -1):
            total = carry + (1 if a[i] == '1' else 0) + (1 if b[i] == '1' else 0)
            result = ('1' if total % 2 == 1 else '0') + result
            carry = total // 2
        if carry:
            result = '1' + result
        return result.lstrip('0') or '0'

    def division(self, value1):
        divisorBin = '1'  
        divisor = 0
        for c in divisorBin:
            divisor = divisor * 2 + (1 if c == '1' else 0)
        if divisor == 0:
            raise ValueError("Divisor no puede ser cero.")

        quotient = ''
        remainder = 0

        for bit in value1:
            remainder = remainder * 2 + (1 if bit == '1' else 0)
            qBit = remainder // divisor
            remainder = remainder % divisor
            quotient += str(qBit)

        quotient = quotient.lstrip('0') or '0'
        return quotient

    @staticmethod
    def greaterOrEquals(a, b):
        a = a.lstrip('0') or '0'
        b = b.lstrip('0') or '0'
        if len(a) > len(b):
            return True
        if len(b) > len(a):
            return False
        return a >= b