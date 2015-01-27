import requests
import datetime
import urllib2
import pandas as pd


class Stock(object):
    """ Python Class that takes 1 argument - a stock ticker.
        Once initialized you can call many methods
        to pull financial data. 
    """

    def __init__(self, ticker):
        self.ticker = ticker
        self.base = 'http://finance.yahoo.com/d/quotes.csv?s=%s&f=' % self.ticker
        self.base_hist = 'http://ichart.yahoo.com/table.csv?s='
        self.params_hist = '%s&a=%s&b=%s&c=%s&d=%s&e=%s&f=%s&g=%s&ignore=.csv'
        self.month = datetime.date.today().month
        self.year = datetime.date.today().year
        self.day = datetime.date.today().day
        self.f = '&f='
        self.data_keys = {'Ask': 'a'
            , 'Bid': 'b'
            , 'Ask_Realtime': 'b2'
            , 'Bid_Realtime': 'b3'
            , 'Previous_Close': 'p'
            , 'Open': 'o'
            , 'Change': 'c1'
            , 'Change_&_Percent_Change': 'c'
            , 'Change_Realtime': 'c6'
            , 'Change_Percent_Realtime': 'k2'
            , 'Change_in_Percent': 'p2'
            , 'After_Hours_Change_Realtime': 'c8'
            , 'Commission': 'c3'
            , 'Days_Low': 'g'
            , 'Days_High': 'h'
            , 'Last_Trade_Realtime_With_Time': 'k1'
            , 'Last_Trade_With_Time': 'l'
            , 'Last_Trade_Price_Only': 'l1'
            , '1_yr_Target_Price': 't8'
            , 'Days_Value_Change': 'w1'
            , 'Days_Value_Change_Realtime': 'w4'
            , 'Price_Paid': 'p1'
            , 'Days_Range': 'm'
            , 'Days_Range_Realtime': 'm2'
            , '52_Week_High': 'k'
            , '52_week_Low': 'j'
            , 'Change_From_52_Week_Low': 'j5'
            , 'Change_From_52_week_High': 'k4'
            , 'Percent_Change_From_52_week_Low': 'j6'
            , 'Percent_Change_From_52_week_High': 'k5'
            , '52_week_Range': 'w'
            , 'Shares_Owned': 's1'
            , 'Stock_Exchange': 'x'
            , 'Shares_Outstanding': 'j2'
            , 'Volume': 'v'
            , 'Ask_Size': 'a5'
            , 'Bid_Size': 'b6'
            , 'Last_Trade_Size': 'k3'
            , 'Average_Daily_Volume': 'a2'
            , 'Order_Book_Realtime': 'i5'
            , 'Earnings_per_Share': 'e'
            , 'EPS_Estimate_Current_Year': 'e7'
            , 'EPS_Estimate_Next_Year': 'e8'
            , 'EPS_Estimate_Next_Quarter': 'e9'
            , 'Book_Value': 'b4'
            , 'EBITDA': 'j4'
            , 'Price_/_Sales': 'p5'
            , 'Price_/_Book': 'p6'
            , 'P/E_Ratio': 'r'
            , 'P/E_Ratio_Realtime': 'r2'
            , 'PEG_Ratio': 'r5'
            , 'Price_/_EPS_Estimate_Current_Year': 'r6'
            , 'Price_/_EPS_Estimate_Next_Year': 'r7'
            , 'Short_Ratio': 's7'
            , 'Dividend_Yield': 'y'
            , 'Dividend_per_Share': 'd'
            , 'Dividend_Pay_Date': 'r1'
            , 'Ex-Dividend_Date': 'q'
            , 'Last_Trade_Date': 'd1'
            , 'Trade_Date': 'd2'
            , 'Last_Trade_Time': 't1'
            , 'Change_From_200_Day_Moving_Average': 'm5'
            , 'Percent_Change_From_200_Day_Moving Average': 'm6'
            , 'Change_From_50_Day_Moving_Average': 'm7'
            , 'Percent_Change_From_50_Day_Moving Average': 'm8'
            , '50_Day_Moving_Average': 'm3'
            , '200_Day_Moving_Average': 'm4'
            , 'Holdings_Gain_Percent': 'g1'
            , 'Annualized_Gain': 'g3'
            , 'Holdings_Gain': 'g4'
            , 'Holdings_Gain_Percent_Realtime': 'g5'
            , 'Holdings_Gain_Realtime': 'g6'
            , 'More_Info': 'v'
            , 'Market_Capitalization': 'j1'
            , 'Market_Cap_Realtime': 'j3'
            , 'Float_Shares': 'f6'
            , 'Name': 'n'
            , 'Notes': 'n4'
            , 'Symbol': 's'
            , 'Ticker_Trend': 't7'
            , 'Trade_Links': 't6'
            , 'High_Limit': 'l2'
            , 'Low_Limit': 'l3'
            , 'Holdings_Value': 'v1'
            , 'Holdings_Value_Realtime': 'v7'
}

    @staticmethod
    def clean(data):
        """ Strips junk data and line breaks
            Input: String
            Returns: clean data (hopefully)
        """
        return ''.join(x for x in data.text.rstrip() if ord(x) < 128)

    def get_ask(self):
        """ Pulls the ASK price """
        ask = self.clean(requests.get(self.base + self.data_keys['Ask']))
        print "%s's current ASK price: %s" % (self.ticker, ask)

    def get_bid(self):
        """ Pulls the BID price """
        bid = self.clean(requests.get(self.base + self.data_keys['Bid']))
        print "%s's current BID price: %s" % (self.ticker, bid)

    def get_ask_real_time(self):
        """ Pulls the REAL TIME ASK price """
        ask_real_time = self.clean(requests.get(self.base + self.data_keys['Ask_Realtime']))
        print "%s's current REAL TIME ASK price: %s" % (self.ticker, ask_real_time)

    def get_bid_real_time(self):
        """ Pulls the REAL TIME BID price """
        bid_real_time = self.clean(requests.get(self.base + self.data_keys['Bid_Realtime']))
        print "%s's current REAL TIME BID price: %s" % (self.ticker, bid_real_time)

    def get_previous_close(self):
        """ Pulls the PREVIOUS CLOSE price """
        previous_close = self.clean(requests.get(self.base + self.data_keys['Previous_Close']))
        print "%s's current PREVIOUS CLOSE price: %s" % (self.ticker, previous_close)

    def get_open(self):
        """ Pulls the OPEN price """
        open_price = self.clean(requests.get(self.base + self.data_keys['Open']))
        print "%s's current OPEN price: %s" % (self.ticker, open_price)

    def get_change(self):
        """ Pulls the day CHANGE in price """
        change = self.clean(requests.get(self.base + self.data_keys['Change']))
        print "%s's current CHANGE in price: %s" % (self.ticker, change)

    def get_pct_change(self):
        """ Pulls PERCENT CHANGE in price """
        pct_change = self.clean(requests.get(self.base + self.data_keys['Change_in_Percent']))
        print "%s's current CHANGE in price: %s" % (self.ticker, pct_change)

    def get_after_hours_change(self):
        """ Pulls AFTER HOURS CHANGE in price """
        after_hour = self.clean(requests.get(self.base + self.data_keys['After_Hours_Change_Realtime']))
        print "%s's current AFTER HOUR CHANGE in price: %s" % (self.ticker, after_hour)

    def get_days_low(self):
        """ Pulls DAYS LOW price """
        days_low = self.clean(requests.get(self.base + self.data_keys['Days_Low']))
        print "%s's current DAYS LOW price: %s" % (self.ticker, days_low)

    def get_days_high(self):
        """ Pulls DAYS HIGH price """
        days_high = self.clean(requests.get(self.base + self.data_keys['Days_High']))
        print "%s's current DAYS HIGH price: %s" % (self.ticker, days_high)

    def get_52wk_high(self):
        """ Pulls 52 WEEK HIGH """
        wk52_high = self.clean(requests.get(self.base + self.data_keys['52_Week_High']))
        print "%s's 52 WEEK HIGH price: %s" % (self.ticker, wk52_high)

    def get_52wk_low(self):
        """ Pulls 52 WEEK LOW """
        wk52_low = self.clean(requests.get(self.base + self.data_keys['52_week_Low']))
        print "%s's 52 WEEK LOW price: %s" % (self.ticker, wk52_low)

    def get_change_52wk_low(self):
        """ Pulls CHANGE from 52 WEEK LOW """
        change_52wk_low = self.clean(requests.get(self.base + self.data_keys['Change_From_52_Week_Low']))
        print "%s's CHANGE FROM 52 WEEK LOW price: %s" % (self.ticker, change_52wk_low)

    def get_change_52wk_high(self):
        """ Pulls CHANGE from 52 WEEK HIGH """
        change_52wk_high = self.clean(requests.get(self.base + self.data_keys['Change_From_52_week_High']))
        print "%s's CHANGE FROM 52 WEEK HIGH price: %s" % (self.ticker, change_52wk_high)

    def get_pct_change_52wk_low(self):
        """ Pulls PCT CHANGE from 52 WEEK LOW """
        pct_52wk_low = self.clean(requests.get(self.base + self.data_keys['Percent_Change_From_52_week_Low']))
        print "%s's PCT CHANGE FROM 52 WEEK LOW price: %s" % (self.ticker, pct_52wk_low)

    def get_pct_change_52wk_high(self):
        """ Pulls PCT CHANGE from 52 WEEK HIGH """
        pct_52wk_high = self.clean(requests.get(self.base + self.data_keys['Percent_Change_From_52_week_High']))
        print "%s's PCT CHANGE FROM 52 WEEK HIGH price: %s" % (self.ticker, pct_52wk_high)

    def get_stock_exchange(self):
        """ Pulls the Exchange the stock is traded on"""
        exchange = self.clean(requests.get(self.base + self.data_keys['Stock_Exchange']))
        print "%s's is traded on the: %s" % (self.ticker, exchange)

    def get_volume(self):
        """ Pulls the daily trading volume """
        volume = self.clean(requests.get(self.base + self.data_keys['Volume']))
        print "%s's trading volume is: %s" % (self.ticker, volume)

    def get_avg_daily_vol(self):
        """ Pulls average daily volume """
        avg_daily_vol = self.clean(requests.get(self.base + self.data_keys['Average_Daily_Volume']))
        print "%s's average daily trading volume is: %s" % (self.ticker, avg_daily_vol)

    def get_eps(self):
        """ Pulls Earnings Per Share """
        eps = self.clean(requests.get(self.base + self.data_keys['Earnings_per_Share']))
        print "%s's Earnings Per Share is: %s" % (self.ticker, eps)

    def get_book_value(self):
        """ Pulls Book Value """
        book_value = self.clean(requests.get(self.base + self.data_keys['Book_Value']))
        print "%s's Book Value is: %s" % (self.ticker, book_value)

    def get_ebitda(self):
        """ Pulls the EBITDA """
        ebitda = self.clean(requests.get(self.base + self.data_keys['EBITDA']))
        print "%s's EBITDA is: %s" % (self.ticker, ebitda)

    def get_price_sales(self):
        """ Pulls price to sales ratio """
        price_sales = self.clean(requests.get(self.base + self.data_keys['Price_/_Sales']))
        print "%s's Price to Sales Ratio is: %s" % (self.ticker, price_sales)

    def get_price_book(self):
        """ Pulls price to book ratio """
        price_book = self.clean(requests.get(self.base + self.data_keys['Price_/_Book']))
        print "%s's Price to Book Ratio is: %s" % (self.ticker, price_book)

    def get_pe_ratio(self):
        """ Pulls the Price to Earnings Ratio """
        pe = self.clean(requests.get(self.base + self.data_keys['P/E_Ratio']))
        print "%s's Price to Earnings Ratio is: %s" % (self.ticker, pe)

    def get_peg_ratio(self):
        """ Pulls the Price to Earnings Growth Ratio """
        peg = self.clean(requests.get(self.base + self.data_keys['PEG_Ratio']))
        print "%s's Price to Earnings to Growth Ratio is: %s" % (self.ticker, peg)

    def get_short_ratio(self):
        """ Pulls the Short ratio """
        short = self.clean(requests.get(self.base + self.data_keys['Short_Ratio']))
        print "%s's Short Ratio is: %s" % (self.ticker, short)

    def get_div_yield(self):
        """ Pulls the Dividend Yield """
        div_yld = self.clean(requests.get(self.base + self.data_keys['Dividend_Yield']))
        print "%s's Dividend Yield is: %s" % (self.ticker, div_yld)

    def get_div_share(self):
        """ Pulls the Dividend Per Share """
        div_share = self.clean(requests.get(self.base + self.data_keys['Dividend_per_Share']))
        print "%s's Dividend Per Share is: %s" % (self.ticker, div_share)

    def get_div_pay_date(self):
        """ Pulls the Divident Pay Date """
        pay_date = self.clean(requests.get(self.base + self.data_keys['Dividend_Pay_Date']))
        print "%s's Dividend Pay Date is: %s" % (self.ticker, pay_date)

    def get_exdiv_date(self):
        """ Pulls the Ex Dividend Date """
        exdiv = self.clean(requests.get(self.base + self.data_keys['Ex-Dividend_Date']))
        print "%s's Ex-Dividend Pay Date is: %s" % (self.ticker, exdiv)

    def get_chg_200day_mvg(self):
        """ Pulls change from 200-Day moving average """
        _200day = self.clean(
            requests.get(
                self.base + self.data_keys['Change_From_200_Day_Moving_Average']
            ))
        print "%s's Change from the 200 Day Moving Average is: %s" % (self.ticker, _200day)

    def get_pct_200day_mvg(self):
        """ Pulls Percent Change from 200 Day Moving average """
        pct_200day = self.clean(
            requests.get(
                self.base + self.data_keys['Percent_Change_From_200_Day_Moving Average']
            ))
        print "%s's Pct Change from the 200 Day Moving Average is: %s" % (self.ticker, pct_200day)

    def get_chg_50day_mvg(self):
        """ Pulls change from 50-Day Moving average """
        _50day = self.clean(requests.get(self.base + self.data_keys['Change_From_50_Day_Moving_Average']))
        print "%s's Change from the 50 Day Moving Average is: %s" % (self.ticker, _50day)

    def get_pct_50day_mvg(self):
        """ Pulls Percent Change from 50 Day Moving Average """
        pct_50day = self.clean(
            requests.get(
                self.base + self.data_keys['Percent_Change_From_50_Day_Moving Average']))
        print "%s's Percent Change from the 50 Day Moving Average is: %s" % (self.ticker, pct_50day)

    def get_50day_mvg(self):
        """ Pulls 50 day moving average """
        _50day_mvg = self.clean(requests.get(self.base + self.data_keys['50_Day_Moving_Average']))
        print "%s's 50 Day Moving Average is: %s" % (self.ticker, _50day_mvg)

    def get_200day_mvg(self):
        """
        Pulls the 200 day Moving average
        """
        _200day_mvg = self.clean(requests.get(self.base + self.data_keys['200_Day_Moving_Average']))
        print "%s's 200 Day Moving Average is: %s" % (self.ticker, _200day_mvg)

    def get_annualized_gain(self):
        """
        Pulls the Annualized Gain
        """
        annualized = self.clean(requests.get(self.base + self.data_keys['Annualized_Gain']))
        print "%s's Annualized Gain is: %s" % (self.ticker, annualized)

    def get_market_cap(self):
        """
        Pulls the current market capitalization
        """
        market_cap = self.clean(requests.get(self.base + self.data_keys['Market_Capitalization']))
        print "%s's Market Capitlization is: %s" % (self.ticker, market_cap)

    def get_float_shares(self):
        """
        Pulls floating shares
        """
        float_shares = self.clean(requests.get(self.base + self.data_keys['Float_Shares']))
        print "%s's # of Floating Shares is: %s" % (self.ticker, float_shares)

    def get_name(self):
        """
        Pulls the name of the company
        """
        name = self.clean(requests.get(self.base + self.data_keys['Name']))
        print "%s's name is: %s" % (self.ticker, name)

    def get_5day_sales(self):
        """
        Pulls 5 days of sales by day intervals.
        :returns: DateFrame of information
        """
        d_30 = (datetime.date.today() - datetime.timedelta(5)).day
        m_30 = (datetime.date.today() - datetime.timedelta(5)).month
        y_30 = (datetime.date.today() - datetime.timedelta(5)).year

        result = urllib2.urlopen(self.base_hist + self.params_hist % (
            self.ticker, m_30 - 1, d_30, y_30, self.month - 1, self.day, self.year, 'd'))
        return pd.DataFrame.from_csv(result)

    def get_30day_sales(self):
        """
        Pulls 30 days of sales by day intervals.
        :returns: DateFrame of information
        """
        d_30 = (datetime.date.today() - datetime.timedelta(30)).day
        m_30 = (datetime.date.today() - datetime.timedelta(30)).month
        y_30 = (datetime.date.today() - datetime.timedelta(30)).year

        result = urllib2.urlopen(self.base_hist + self.params_hist % (
            self.ticker, m_30 - 1, d_30, y_30, self.month - 1, self.day, self.year, 'd'))
        return pd.DataFrame.from_csv(result)

    def get_90day_sales(self):
        """
        Pulls 90 days of sales by day intervals.
        :returns: DateFrame of information
        """
        d_30 = (datetime.date.today() - datetime.timedelta(90)).day
        m_30 = (datetime.date.today() - datetime.timedelta(90)).month
        y_30 = (datetime.date.today() - datetime.timedelta(90)).year

        result = urllib2.urlopen(self.base_hist + self.params_hist % (
            self.ticker, m_30 - 1, d_30, y_30, self.month - 1, self.day, self.year, 'd'))
        return pd.DataFrame.from_csv(result)

    def get_180day_sales(self):
        """
        Pulls 180 days of sales by day intervals.
        :returns: DateFrame of information
        """
        d_30 = (datetime.date.today() - datetime.timedelta(180)).day
        m_30 = (datetime.date.today() - datetime.timedelta(180)).month
        y_30 = (datetime.date.today() - datetime.timedelta(180)).year

        result = urllib2.urlopen(self.base_hist + self.params_hist % (
            self.ticker, m_30 - 1, d_30, y_30, self.month - 1, self.day, self.year, 'd'))
        return pd.DataFrame.from_csv(result)

    def get_1yr_sales(self):
        """
        Pulls 1 year of sales by day intervals.
        :returns: DateFrame of information
        """
        d_30 = (datetime.date.today() - datetime.timedelta(365)).day
        m_30 = (datetime.date.today() - datetime.timedelta(365)).month
        y_30 = (datetime.date.today() - datetime.timedelta(365)).year

        result = urllib2.urlopen(self.base_hist + self.params_hist % (
            self.ticker, m_30 - 1, d_30, y_30, self.month - 1, self.day, self.year, 'd'))
        return pd.DataFrame.from_csv(result)

    def get_custom_sales(self, year, month, day, year_end, month_end, day_end, interval='d'):
        """
        Enter the start and end date of the time frame
        :param year: string
        :param month: string
        :param day: string
        :return: Pandas DataFrame
        """
        result = urllib2.urlopen(self.base_hist + self.params_hist % (
            self.ticker, month - 1, day, year, month_end - 1, day_end, year_end, interval))
        return pd.DataFrame.from_csv(result)
