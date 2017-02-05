#Simple RSA encryption demonstration in Python 2.7

This program demonstrates using RSA asymmetric encryption (public key, private key encryption). Asymmetric encryption is used in protocol like OpenPGP.

The RSA encyption scheme uses two random prime numbers to generate a public and private key. With large enough primes (unimaginably large, in fact), breaking the encryption becomes practically impossible.

This demonstration uses trivially small prime numbers. There is also an upper limit to the size of prime numbers used in this demonstration due to unicode character constraints.

The following videos present a good walkthrough of the RSA encryption and key generation process:
1. [RSA Encryption Algorithm - Computing an Example](https://www.youtube.com/watch?v=4zahvcJ9glg)
2. [RSA Encryption Algorithm - Generating the Keys](https://www.youtube.com/watch?v=oOcTVTpUsPQ)
