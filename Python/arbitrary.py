def shop(*args, **kwargs):
    for name in args:
        print(name, end=" ")
    print("")
    # for value in kwargs.values():
    #     print(value)

    print(f"{kwargs.get('street')},{kwargs.get('plot')}")
    print(f"{kwargs.get('city')},{kwargs.get('zip')}")


shop("Airaf","Jawed",
     street="Fake st.",
     plot="123",
     city="Bhilai",
     zip="490023")