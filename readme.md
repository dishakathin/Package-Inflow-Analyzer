In the 'src' directory, we have 'handler' and 'utils' directories.

In the 'handler' directory, we have 'package_inflow_processor.py'
class 'PackageInflowProcessor' contains the 'process_input' method.
It takes string as input and returns the list of total package inflows.


main.py file contains the code for the GET call and app initiation.
In it, the 'PackageInflowProcessor' object is created and 'process_input' method is called.


In the 'utils' directory, we have the following:
1. 'encoding.py'
It contains the character-to-number mapping used in our problem statement.

2. 'constants.py'
It maintains the constants used in our project.

3. 'helper.py'
It contains some helper functions

4. 'invalid_input_error.py'
It is a user-defined exception class for the invalid input strings


### Building the docker image

1. Go to parent directory, which contains main.py
2. Build docker container using following command: 'docker build -t interview .'
3. Run docker image using following command: 'docker run -p 8080:8000 interview'
# Note: You can use port 8080:8000 instead of 8000:8000 in case it is occupied
4. Check output using http://localhost:8080/docs
# Note: if you are using 8000:8000 port then use http://localhost:8000/docs


### Testing
# Note: Do inside docker 
1. Go inside docker using : 'docker run -it --name my-container interview /bin/bash'
2. Use following command for testing: 'pytest'

In the 'test' directory we have the following::
a. 'test_package_inflow_processor.py'
It provides unit testing for package_inflow_processor.py

b. 'test_get_total_package_inflows.py'
It provides testing for the GET call



