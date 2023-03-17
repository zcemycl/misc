def convert_int_to_roman(number: int) -> str:
    symbols = list("IVXLCDM")
    result = ""
    while number!=0:
        remainder = number%10
        new = ""
        if remainder==9:
            new = symbols[0]+symbols[2]
        elif remainder==4:
            new = symbols[0]+symbols[1]
        elif remainder!=0:
            new = symbols[0]*(remainder%5)
            if len(symbols) > 1:
                new = symbols[1]*(remainder//5)+new
                
        result = new+result
        number //= 10
        symbols.pop(0)
        if len(symbols)>0:
            symbols.pop(0)
    return result

if __name__ == "__main__":
    for number in [2018, 1999, 3999, 999, 444]:
        print(number, convert_int_to_roman(number))