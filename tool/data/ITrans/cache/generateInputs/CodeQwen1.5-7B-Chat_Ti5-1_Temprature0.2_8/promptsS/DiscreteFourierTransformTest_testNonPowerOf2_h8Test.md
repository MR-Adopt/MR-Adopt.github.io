# ORIGINAL TEST CASE
```java
@Test
public void testNonPowerOf2() {
    NumberContext accuracy = NumberContext.of(8);
    for (int dimension = 2; dimension <= 16; dimension++) {
        PhysicalStore<Double> input = Primitive64Store.FACTORY.makeFilled(dimension, 1, Uniform.of(-2, 4));
        DiscreteFourierTransform transformer = DiscreteFourierTransform.newInstance(dimension);
        MatrixStore<ComplexNumber> transformed = transformer.transform(input);
        MatrixStore<ComplexNumber> transformed2 = GenericStore.C128.makeDense(input.size(), 1);
        transformer.transform(input, DiscreteFourierTransform.DEFAULT, (PhysicalStore<ComplexNumber>) transformed2);
        MatrixStore<ComplexNumber> reverted = transformer.inverse(transformed2);
        if (DEBUG) {
            BasicLogger.debugMatrix("Input", input);
            BasicLogger.debugMatrix("Transformed", transformed);
            BasicLogger.debugMatrix("Reverted", reverted);
        }
        TestUtils.assertEquals(input, reverted, accuracy);
    }
}

```
TEST INPUT: `transformer`,`input`


# METHOD UNDER TEST
```java
public MatrixStore<ComplexNumber> transform(final double... input) {
    PhysicalStore<ComplexNumber> output = GenericStore.C128.makeDense(input.length, 1);
    this.transform(ArrayR064.wrap(input), DEFAULT, output);
    return output;
}

public final MatrixStore<ComplexNumber> inverse(final Access1D<ComplexNumber> input) {
    PhysicalStore<ComplexNumber> output = GenericStore.C128.makeDense(input.size(), 1);
    this.transform(input, INVERSE, output);
    return output;
}

```


# REQUIRED DELIVERABLE
Construct five new values for the test input `transformer`,`input`. Each new input should explore valid values. Present the code for constructing each new input in the following format:
## New inputN:
```java
        PhysicalStore<Double> input = Primitive64Store.FACTORY.makeFilled(dimension, 1, Uniform.of(-2, 4));
        DiscreteFourierTransform transformer = DiscreteFourierTransform.newInstance(dimension);
```

Provide the construction code for each of the five new test inputs, and explain why this input is valid. 