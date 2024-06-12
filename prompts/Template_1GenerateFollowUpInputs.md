# Task Description
<SYSTEM MESSAGE: START>
As an expert in Java programming, you are good at understanding code intention, and writing test cases to cover diverse test scenarios. 
Test cases are designed to verify whether the software meets the specified requirements, functions as intended, and handles various scenarios correctly.

Given a test case (denoted as 'ORIGINAL TEST CASE'), the program under test is denoted as 'METHOD UNDER TEST'.
Your goal is to understand the program under test, and infer the relation between the pair of test inputs (denoted as 'SOURCE INPUT' and 'FOLLOW UP INPUT') in the 'ORIGINAL TEST CASE'.
The inferred relation should be generalizable across valid input pairs.

Once you understand the relation, you are to generate corresponding 'FOLLOW UP INPUT' for new 'SOURCE INPUT' that adhere to the inferred relation and ensure that they pass the assertions in the 'ORIGINAL TEST CASE'.
New source inputs are denoted as 'NEW SOURCE INPUTS'.
<SYSTEM MESSAGE: END>


# ORIGINAL TEST CASE
```java
<ORIGINAL TEST CASE>
```
SOURCE INPUT: <SOURCE INPUT>
FOLLOW UP INPUT: <FOLLOW UP INPUT>


# METHOD UNDER TEST
```java
<FOCAL METHOD>
```


# NEW SOURCE INPUTS
<NEW SOURCE INPUTS>


# REQUIRED DELIVERABLE
For each new source input listed under 'NEW SOURCE INPUTS', please construct the corresponding follow-up input that satisfies your inferred relation and pass the assertions in the 'ORIGINAL TEST CASE'. Document the complete code for each new input pair in the format shown below:
## New input pairN:
```java
<A PAIR OF TEST INPUTS>
```

Additionally, for each new source input, provide the code used to generate the follow-up input along with its associated source input code. Please explain why this new input pair satisfies the inferred relation you have identified.