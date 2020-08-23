

def paymentAmount(subsistMoney,tailMoney,backMoney):
	list_s = []
	if float(subsistMoney) > 0:
		list_s.append(1)
	if float(tailMoney) > 0:
		list_s.append(2)
	if float(backMoney) > 0:
		list_s.append(3)
	return list_s



a = paymentAmount('1000.00','0.00','3.00')
print(a)
a.remove(min(a))
print(a)