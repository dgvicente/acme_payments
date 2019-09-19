### Project summary
Acme payments is a console application with the purpose of calculating how much ACME company employess should be paid, 
taking as an starting point rates (given by hour ranges during days of week or weekends) and per employee worked hours
(given as a list with hour ranges and days of week). The data should be structured as follows:

#### Monday - Friday
| Initial Time  |End Time       | Rate  |
| ------------- |:-------------:| -----:|
| 00:01         | 09:00         | 25 USD|
| 09:01         | 18:00         | 15 USD|
| 18:01         | 00:00         | 25 USD|
#### Saturday - Sunday
| Initial Time  |End Time       | Rate  |
| ------------- |:-------------:| -----:|
| 00:01         | 09:00         | 30 USD|
| 09:01         | 18:00         | 20 USD|
| 18:01         | 00:00         | 25 USD|

_Table 1_

The employees information should be received as follows:

`RENE=MO10:00-12:00,TU10:00-12:00,TH01:00-03:00,SA14:00-18:00,SU20:00-21:00`

And the output, for the given examples should look like:

`The amount to pay RENE is: 215 USD`

### Project implementation
The solution has 3 main modules in order to perform the required calculations:
* *payments_configuration:* Takes care of loading and translating to the object 
oriented world all predefined configurations of rates by hours (Table 1).
<img src="https://github.com/dgvicente/acme_payments/blob/master/diagrams/payments_configuration.png?raw=true" width="50%">

* *questions:* In charge of loading and translating to the object oriented world
all "questions" about how much employees should be paid (using the format 
previously defined).
<img src="https://github.com/dgvicente/acme_payments/blob/master/diagrams/questions.png?raw=true" width="50%">

* *answers:* It consumes the information from the *payments_configuration* and 
the *questions* module and comes up with the answer about the employees payment.
<img src="https://github.com/dgvicente/acme_payments/blob/master/diagrams/answers.png?raw=true" width="50%">

### Project requirements:
1. Python 3.7.x ([here](https://www.python.org/downloads/release/python-374/))
2. pip3

### To run the project:
1. Navigate in the console to the project directory
2. Install the project requirements contained in requirements.txt (virtualenv is recommended)

   2.1. If you are using a virtualenv, activate it 
3. Execute the command

`python acme_payments.py`

### To run the test suite:
1. Navigate in the console to the project directory
2. Execute the command

`python -m unittest discover`

NOTE: If you are using a virtualenv make sure it is active
