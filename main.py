

#def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
 #   print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.

def rzymska(arabska):
    liczby_rzymskie=[[1,"I"],[4,"IV"],[5,"V"],[9,"IX"],[10,"X"],[40,"XL"],[50,"L"],[90,"XC"],[100,"C"],[400,"CD"],[500,"D"],[900,"CM"],[1000,"M"]]
    liczba=''
    #for i in range(7):
    i=12
    while int(arabska)>0:
        if int(arabska) >= int(liczby_rzymskie[i][0]):
            print(liczby_rzymskie[i][0])
            #print("liczba rzymasa to ",liczby_rzymskie[i][1] )
            liczba=liczba+liczby_rzymskie[i][1]
            #print('Liczba:',liczba)
            arabska = int(arabska)-int(liczby_rzymskie[i][0])
        else:
            i=i-1;
    print('Liczba:',liczba)
if __name__ == '__main__':
    #print_hi('PyCharm')
    liczba = input("Podaj liczbę")
    print("Podana liczba to",liczba)
    rzymska(liczba)
