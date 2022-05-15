from decimal import DivisionByZero


try:
    print(1/0)
except ZeroDivisionError as err:
    print(f"Fout: {err}")    
finally:
    print("Sluit dingen af indien nodig")    