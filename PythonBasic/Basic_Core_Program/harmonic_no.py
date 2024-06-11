# 4. Harmonic Number
# a. Desc -> Prints the Nth harmonic number: 1/1 + 1/2 + ... + 1/N
# (http://users.encs.concordia.ca/~chvatal/notes/harmonic.html).
# b. I/P -> The Harmonic Value N. Ensure N != 0
# c. Logic -> compute 1/1 + 1/2 + 1/3 + ... + 1/N
# d. O/P -> Print the Nth Harmonic Value.


def compute_harmonic_number(n):
        harmonic_number=0
        if n>0:
                for i in range(1,n+1):
                        harmonic_number+=1/i
                print(f"The Nth Harmonic Number is :{harmonic_number}")
        else:
                print("N must be a positive integer")

                
                
                


def main():
        n=int(input('Enter the value of N :'))
        compute_harmonic_number(n)


main()