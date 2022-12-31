#Prime part 3
#Do NOT change any of the code below👇
n = int(input("Check this number: "))

def prime_checker(number):
    hcf_dec = (number - 1);
    times_compositive = [];
    times_loop = 0
    var1 = 1;
    while times_loop+1 < number:
        
        if (number % var1) == 0:
            times_compositive.append("1");
        var1 = var1+1
        times_loop = times_loop + 1 ;
    if (len(times_compositive) > 1):
            print("its Compositive");
    else:
        print(f"its Prime");


prime_checker(number=n)