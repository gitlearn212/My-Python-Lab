speed = [
    ('car',100),
    ('boat',20),
    ('bike',8),
    ('skateboard',7),
    ('aircraft',650)

    ]

print(min(speed, key=lambda x: x[1])[1])  


