# Task Description
<SYSTEM MESSAGE: START>
As an expert in Java programming, you excel at understanding the intentions behind code and developing functions that convert provided inputs into desired outputs.
In metamorphic testing, input transformation functions are crafted to automatically generate additional test inputs (denoted as 'FOLLOW UP INPUT') from initial test inputs (denoted as 'SOURCE INPUT') based on defined metamorphic relations (MRs).

Given the program under test (denoted as 'METHOD UNDER TEST') and an MR-encoded test case (denoted as 'TEST CASE'),
your task is to analyze the program under test and the provided test case, deduce the relationship between 'SOURCE INPUT' and 'FOLLOW UP INPUT' in the test case, and create a function that transforms 'SOURCE INPUT' into 'FOLLOW UP INPUT'.

The deduced relation and generated transformation function should be applicable to other potential pairs of source and follow-up inputs with similar characteristics.
Considering potential input pairs with boundary values as well.
<SYSTEM MESSAGE: END>


# METHOD UNDER TEST
```java
<FOCAL METHOD>
```


# TEST CASE
```java
<ORIGINAL TEST CASE>
```
SOURCE INPUT: <SOURCE INPUT>
FOLLOW UP INPUT: <FOLLOW UP INPUT>



# OUTPUT FORMAT
```java
public class $ITransClass$ {
 $ITransFunction$ {
        // TODO
 $returnTransformedInputs$
 }
}
```
Your task is to deduce the relationship between 'SOURCE INPUT' and 'FOLLOW UP INPUT' in the test case, and create a function that transforms 'SOURCE INPUT' into 'FOLLOW UP INPUT'.
The deduced relation and generated transformation function should be applicable to other potentail input pairs with similar characteristics.
Generate the transformation function by complementing the above code skeleton in 'OUTPUT FORMAT'.
