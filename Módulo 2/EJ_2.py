N = int(input())
SO = list(map(int, input().split(", ")))
LA = list(map(int, input().split(", ")))
RIS = list(map(int, input().split(", ")))
PSO = 0
PLA = 0
PRIS = 0

i = 0

while i < N:
    if((SO[i] + LA[i] + RIS[i])%2 == 0):
        if SO[i] % 2 == 0:
            PSO = PSO+1
        if LA[i] % 2 == 0:
            PLA = PLA+1
        if RIS[i] % 2 == 0:
            PRIS = PRIS+1
    if((SO[i] + LA[i] + RIS[i])%2 == 1):
        if SO[i] % 2 == 1:
            PSO = PSO+1
        if LA[i] % 2 == 1:
            PLA = PLA+1
        if RIS[i] % 2 == 1:
            PRIS = PRIS+1
    i = i+1

print(f"SO:{PSO}, LAR:{PLA}, IS:{PRIS}")