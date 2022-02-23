Improve the performance of the matmult.py script using numpy
What is the best performance that you achieved with N=250?

ANS:By using the numpy package apropriately I was able to achieve a runtime of 0.328 seconds. That is more than ten times faster than the 3.954 seconds achieved in the previous methods. A big part of the time used in the improved version is due to print statements. By removing those I find that the improved script runs in 0.135 seconds, while the old one improves to 3.815 seconds.