# ORIGINAL TEST CASE
```java
@Test
public void extract() {
    IntArrayList a = new IntArrayList();
    a.appendValue(0);
    a.appendValue(1);
    a.appendValue(0);
    IntArrayList b = new IntArrayList();
    b.appendValue(0);
    b.appendValue(1);
    b.appendValue(0);
    boolean trimFlag = false;
    boolean trimFlag2 = true;
    int[] ex = a.extractValues(trimFlag);
    int[] et = b.extractValues(trimFlag2);
    assertTrue(ex.length >= et.length);
}

```
TEST INPUT: `a`,`trimFlag`


# METHOD UNDER TEST
```java
public int[] extractValues(boolean trim) {
    if (trim) {
        if (_data.length == _size)
            return _data;
        return Arrays.copyOfRange(_data, 0, _size);
    } else
        return _data;
}

```


# REQUIRED DELIVERABLE
Construct five new values for the test input `a`,`trimFlag`. Each new input should explore valid values. Present the code for constructing each new input in the following format:
## New inputN:
```java
    IntArrayList a = new IntArrayList();
    boolean trimFlag = false;
```

Provide the construction code for each of the five new test inputs, and explain why this input is valid. 