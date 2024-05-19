# using 'pip' module to install 3rd party libraries

# python -m pip : run the pip module
# pip install <package_name>  : install the module
# install --upgrade <package_name>  : upgrade the already installed package

## Testing a Function
# 1. create one file that contains a function
# 2. in the main working file, import the function, and use as required.
# 3. create a file for test cases. 
# 3.1 name of test case file should always begin with 'test_'
# 3.2 follow name of the file with name of function you wanted to test
# 3.3 create a function beginning with name test_<function name>
# 3.4 create test function to test the main function
# pass the main function inside test function, 
# pass the required output from main function, and compare them

# 4. Running the test: go the directory of created files, and run in terminal 'pytest'
''' info seen on the terminal:
1. system info
2. directory where the test is being run from 
3. number of test files found
4. number of tests passed
5. number of dots shows number of test cases passed for 1 parent function
'''

#  Failing scenario
#  if any changes are made in the main function file, then the test case will fail.
# we will get the info about failure in the terminal window itself
'''
1. which case of parent function that has failed
2. test function which has failed
3. line of code the caused failure
4. type of error
'''
#  to fix the failed test case: adjust the test function code with parent function code.


## Adding New Tests: we can add multiple test functions to test the one parent function
# in the same test file, create multiple functions, that represent individual test case 




# A unit test verifies that one specific aspect of a function’s behavior is correct. 
# A test case is a collection of unit tests, that together prove that a function behaves as it’s supposed to, within the full range of situations you expect it to handle.
#  full coverage includes a full range of unit tests covering all the possible ways you can use a function withoot failure.


