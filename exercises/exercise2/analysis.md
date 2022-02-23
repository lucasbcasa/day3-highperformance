Improve the performance of the matmult.py script using numpy
What is the best performance that you achieved with N=250?

ANS:By using the numpy package apropriately I was able to achieve a **runtime of 0.328 seconds**. That is more than **ten times faster than the 3.954 seconds achieved in the original script**. It is **almost seven times faster than the improved version** of the algorithm, which performed at 2.294.

A big part of the remaining time used in the improved version is due to print statements. By removing those I find that the improved script runs in 0.135 seconds, while the old one improves to 3.815 s, and the improved one without numpy to 2.271 s.