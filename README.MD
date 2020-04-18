# D.E.C.R.Y.P.T

## What it does

Tries to fetch a meaningful word from a string of jumbled letters.   

## How does it do what it does

BruteForce. Fetches all permutations of the provided string. Looks for spell check to identify meaningful words.   

## Execute,

-   docker build -t decrypter .    
   
-   docker run --rm -ti -v ${pwd}/src:/src decrypter python decrypt.py {search}   

## Sample Output,

docker run --rm -ti -v ${pwd}/src:/src decrypter python decrypt.py onjes    
Please wait while we compute and show the final suggestions    
jones    
jones    
jones    
    
    
Final Suggestions!    
jones    
