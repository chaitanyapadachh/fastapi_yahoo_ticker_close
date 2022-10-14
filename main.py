from fastapi import FastAPI
import yfinance as yf
app = FastAPI()

@app.get('/')
def home():
    return {"message":"running"}

@app.get('/close/{stock_name}')
def stock_price(stock_name):
    try:
        stock = yf.Ticker(stock_name)
        history = stock.history()
        closing_price =  round(history.Close.iloc[-1],1)
        date = history.index[-1].date()
        return {
                    "message":"success",
                    "data":
                    {
                        "ticker":stock_name,
                        "close":closing_price,
                        "date":date
                    }
                }
    except:
        return {"message":"failed","data":None}