### This does not work in repl.it, use it in real python
### to install: pip install yahoo-finance
try:
    from yahoo_finance import Share
except ImportError:
    err="Try 'pip install yahoo_finance' first!"
    raise ImportError(err)

### Requesting user input
def get_stocksymbol():
  stock_symbol=str(input("Enter stock symbol you wish info from. [0] to stop: "))
  return stock_symbol

### Refreshing the data
def refresh_data(stock_symbol):
  yahoo = Share(stock_symbol)
  yahoo.refresh()
  return yahoo

### Getting the yahoo data, building the dictionary with data
def get_data(stock_symbol):
  count=0
  amount=float(0)

  yahoo = refresh_data(stock_symbol)

  stock_name=yahoo.get_name()
  stock_price=float(yahoo.get_price())

  try:
    stock_div=float(yahoo.get_dividend_share())
  except TypeError:
    stock_div=float(0)
  try:
    stock_div_yield=float(yahoo.get_dividend_yield())
  except TypeError:
    stock_div_yield=float(0)

  if stock_div_yield!=float(0) and stock_div!=float(0):
    while float(amount) < float(stock_price):
      count+=1
      amount+=stock_div

  stockdict={'symbol':stock_symbol,'name':stock_name,'price':stock_price,'dividend':stock_div,'divyield':stock_div_yield,'needed':count}
  return stockdict

### Printing all the data on the screen
def printdata(stockdict):
  print("\n")
  print("Stock symbol: " + stockdict['symbol'])
  print("Stock name: " + str(stockdict['name']))
  print("Stock price: " + str(stockdict['price']))
  if stockdict['dividend']==0.00:
    print("Company does not pay dividends on this stock.")
    print("\n")
  else:
    print("Stock dividend: " + str(stockdict['dividend']) + " per share")
    print("Stock dividend yield: " + str(stockdict['divyield']) + " % per year")
    print("Stocks needed: " + str(stockdict['needed']))
    print("This will give " + str(stockdict['needed']*stockdict['dividend']) + " in dividends.")
    print("Total investment needed: " + str(int(stockdict['price']*stockdict['needed'])))
    print("\n")

while True:
  stock_symbol=get_stocksymbol()
  if stock_symbol==str(0):
    break
  else:
    printdata(get_data(stock_symbol))

