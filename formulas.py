def gained_profit(buying_price , selling_price):
    profit_gained = ((selling_price-buying_price)/buying_price)
    return profit_gained
def potential_profit(last_traded_price,buying_price):
    potential_profit = ((last_traded_price-buying_price)/buying_price)
    return potential_profit
def potential_risk_percentage(stop_loss_price,buying_price):
    risk = ((stop_loss_price-buying_price)/buying_price)
    return risk
"""
estimate_type = db.Column(db.String(20), nullable=True) #نوع سیگنال
symbol_name = db.Column(db.String(50), nullable=False) # نماد
buying_price = db.Column(db.Integer, nullable=False) #‌ قیمت پیشنهادی خرید
expected_gain = db.Column(db.Integer, nullable=True) # حد سود انتظاری | Expected profit limit
stop_loss_price = db.Column(db.Integer, nullable=False) # حد ضرر انتظاری | Expected loss limit
period = db.Column(db.Integer, nullable=True) # مدت زمان انتظار-ماه
potential_profit = db.Column(db.Integer, nullable=True) # بازدهی اولیه
gained_profit = db.Column(db.Integer, nullable=True) # بازدهی ثانویه
risk = db.Column(db.Integer, nullable=True) # ریسک
date_benchmark = db.Column(db.DateTime, nullable = False, default = datetime.now()) # زمان ثبت
sell_time = db.Column(db.String(20), nullable=True) #زمان خروج
sell_price = db.Column(db.String(20), nullable=True) #قیمت خروج
position_status = db.Column(db.String(20), nullable=True) #باز یا بسته بودن موقعیت
symbol_status = db.Column(db.String(20), nullable=True) #باز یا بسته بودن نماد
close_price = db.Column(db.String(20), nullable=True) #قیمت پایانی
last_price = db.Column(db.String(20), nullable=True) #قیمت اخرین معامله
"""