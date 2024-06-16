# METHOD UNDER TEST
```java
@Override
public int hashCode() {
    return value;
}

```


# TEST CASE
```java
@Test
void testHashCodeAndEquals() {
    Cost subject = Cost.costOfSeconds(10);
    Cost same = Cost.costOfSeconds(10);
    Cost other = Cost.costOfSeconds(11);
    assertNotEquals(subject.hashCode(), other.hashCode());
}

```
SOURCE INPUT: `subject`
FOLLOW UP INPUT: `other`


# OTHER INPUT PAIRS 
## Input pair1:
```java
Cost subject = Cost.costOfSeconds(10);
Cost other = Cost.costOfSeconds(11);
```

## Input pair2:
```java
Cost subject = Cost.costOfSeconds(1000000);
Cost other = Cost.costOfSeconds(1000001);
```



# OUTPUT FORMAT
```java
public class CostTest_testHashCodeAndEquals {
    public static Cost inputTransformation_testHashCodeAndEquals(Cost subject)  {
        // TODO
        Cost other = 
		return other;
    }
}
```
Your task is to deduce the relationship between 'SOURCE INPUT' and 'FOLLOW UP INPUT' in the test case, and create a function that transforms 'SOURCE INPUT' into 'FOLLOW UP INPUT'.
The deduced relation and generated transformation function should be applicable to addtional input pairs and other potentail input pairs with similar characteristics.
Generate the transformation function by complementing the above code skeleton in 'OUTPUT FORMAT'.