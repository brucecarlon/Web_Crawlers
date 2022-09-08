# Secure-Password-API
This program is a secure password checker, it takes a password input from a user, runs it through the SHA1 hash function and extracts the first five characters of the hash key. we will call these first five characters of the hash key 'the head of the key' and the remaing chacters will be reffered to as 'the tail of the hash key'.

We then compare the head of the hash key to passwords stored on the pwnedpasswords website and request all the passwords who's first five characters match the head of the hash key. From this response we the check to see if any these passwords having a tail that matches the tail of the hash key, If such a password exists then the password is not secure.

The security is ensured by never passing the user password as a a string to the website, neither do we pass the entire hash key to the website but rather we will pass only a portion of the hashed user password that matches to a variety of hash keys.
Program returns the number of times your password has been retrieved in database breach.

