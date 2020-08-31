
"""
    creater : Rider [MT15]
    date : (31-08-2020)
    title : AI Developer 
    
    thanks you for running my code 
    # Do not copy without permission 

"""


import sys 
import subprocess 

# module installation 
def install(package):

    subprocess.run([
        sys.executable, "-m", "pip", "-q", "install", package
    ])
    
install("pyfiglet")



# function 
def styleyourname(UserInput) :
    
    # import pyfiglet 
    import pyfiglet 
    
    # variable 
    Name = pyfiglet.figlet_format(UserInput.upper())
    
    
    
    print ('if you like my code please upvote its \n')
    
    # printing your name 
    
    print (Name)
    
    print ('THANK YOU')

# Main Function for function running ***
if __name__ == "__main__" :
    
    styleyourname(input())
    
# Thank You Guys 
