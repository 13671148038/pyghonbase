try:
    6 / 0
except Exception as e:
    print(e)
else:
    print('很好')
finally:
    print('我必被执行')