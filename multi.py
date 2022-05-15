try:
    f = open('file.txt')
    s = f.readline()
    i = int(s.strip())
    import blabla
    lijst = []
    print(lijst[0])
    print(1/0)    
except (ZeroDivisionError, ModuleNotFoundError, IndexError) as err:
    print(f"Fout: {err}" )
except OSError as err:
    print("OS error: {0}".format(err))
except Exception as err:
    print(f"Unexpected {err=}, {type(err)=}")    






