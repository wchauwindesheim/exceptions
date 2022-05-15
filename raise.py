import traceback

def normaleFunctie():
    raise Exception("Er is een fout opgetreden")

def main():
    print("begin ======")
    try:
        normaleFunctie()
    except Exception as err:
        print(f"Fout: {err}")
        print(traceback.print_stack(limit=1))
        print("eind ======")

main()


