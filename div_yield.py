# Calculating dividend yield for a stock
# Welcome to the dividend yield calculator!
print("Welcome to the dividend yield calculator!")

def calc_div_yield(dividend_per_share, stock_price):
    if stock_price <= 0:
        raise ValueError("Stock price must be greater than zero.")
    return (dividend_per_share / stock_price) * 100

def main():
    try:
        dividend_per_share = float(input("Enter the dividend per share: "))
        stock_price = float(input("Enter the stock price: "))
        div_yield = calc_div_yield(dividend_per_share, stock_price)
    except ValueError as e:
        print(f"Input error: {e}")
    except KeyboardInterrupt:
        print("\nInput cancelled.")
    else:
        print(f"The dividend yield is: {div_yield:.2f}%")

if __name__ == "__main__":
    main()
# ...existing code...
