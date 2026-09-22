    #
    # Solved by mang-s
    # Date: 22/08/25
    #
    # https://projecteuler.net/problem=32
    # https://github.com/mang-s/Project-Euler-Solutions
    #

def pandigital_products(rangemax: int) -> int:
    
    res = set()
    for i in range(1, rangemax):
        if "0" not in str(i):
            components = get_components(i)
            if is_product_pandigital(components):
                res.add(i)
    
    return sum(res)

def get_components(product: int) -> list(tuple()): 
    # obtains a list with all the tuples containing multiplicand, multiplier, and product for the given number

    res = []
    
    for i in range(2, product // 2 + 1):
        if product % i == 0:
            multiplier = i
            multiplicand = product // i
            res.append((multiplicand, multiplier, product))

    return res

def is_product_pandigital(identities: list(tuple())) -> bool:
    # identities is a list of tuples containing all combinations of mutiplicand, multiplier and product

    res = False
    for multiplicand, multiplier, product in identities:
        numbers = f"{multiplicand}{multiplier}{product}"

        if len(numbers) == 9 and set(numbers) == set("123456789"):
            # Pandigitals 1 through 9 cannot contain 0 or have more/less than 9 unique digits
            res = True
            break

    return res

if __name__ == "__main__":

    print(pandigital_products(rangemax = 9999))