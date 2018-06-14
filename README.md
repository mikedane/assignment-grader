# Assignment Grader

A small python project which takes a folder full of java assignment submissions and compiles and runs them against a series of test cases. Once all assignments have been tested and run, the results of those tests including any compiler errors are spit out into a word document which can then be examined and graded. 

## Usage

### Getting the grading script

type the following command in your terminal
	```$ git clone https://github.com/mikedane/assignment-grader.git```
	```$ cd assignment-grader```
This will clone a copy of the current version of the testing script and cd you into it. Note that this script is written using Python3, so you will need Python 3 installed on your computer to run it. Also this script was written to work on a mac (I haven’t written a windows version) so it will only work on mac. If you don’t have a mac, then there should be some in the library you can use. Or just write a windows version

### Using the grading script

1. Obtain a folder with all of the student submissions from one of the Professors. 
2. Manually look through each student’s folder and write down all versions of the file names. One of the biggest problem (especially in the beginning of the semester) is students not naming their files correctly. In order for the script to work we need to tell it any alternate names the student’s are using. So manually scan through and write down any alternate names. 
3. When you initially cloned the testr program from GitHub you should have gotten a file called Feedback.docx. This is a template that the script will use. Copy that file and paste it into the root directory of the submissions folder. Then using microsoft word, go inside and modify the header and footer to match the current assignment. Save the file and make sure that it’s in the root directory of the submissions folder. 
4. Then, from the command line run the driver.py python file
	$ python3 path/to/file/driver.py
5. Follow the onscreen instructions and the script will start. Note any error messages or compiler warnings that show up. 
6. Look through each newly created feedback document and check to make sure everything worked. This script is still a work in progress so it’s possible that a something went wrong. However if something did go wrong make sure you input everything correctly into the tester program. 


### Tips:

If, when checking the newly generated feedback documents you get an error saying 

ERROR -> Problem interleaving input into results, perhaps an invalid prompt string was used

This means that an incorrect prompt was used for getting input. The default input prompt is “:>”. 


