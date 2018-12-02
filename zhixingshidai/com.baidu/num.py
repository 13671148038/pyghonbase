# 小数保留两位
doub = 563 / 8333
print(round(doub, 2))

# 小数转百分比保留两位小数
doub = 563 / 8333
bfb = '{:.2%}'.format(doub)
print(bfb)
