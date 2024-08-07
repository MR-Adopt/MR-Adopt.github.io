# ORIGINAL TEST CASE
```java
@Test
public void testShiftAndRevertEven() {
    int c = 2;
    int r = 2;
    Primitive64Store original = Primitive64Store.FACTORY.make(2, 2);
    Primitive64Store original2 = Primitive64Store.FACTORY.make(2, 2);
    for (int j = 0; j < c; j++) {
        for (int i = 0; i < r; i++) {
            original.set(i, j, i + j);
        }
    }
    if (DEBUG) {
        BasicLogger.debugMatrix("Original " + r + "x" + c, original);
    }
    MatrixStore<Double> shifted = DiscreteFourierTransform.shift(original);
    if (DEBUG) {
        BasicLogger.debugMatrix("Shifted " + r + "x" + c, shifted);
    }
    int cr = r / 2;
    int cc = c / 2;
    // TestUtils.assertEquals("(" + cr + "," + cc + ")", PrimitiveMath.ZERO, shifted.doubleValue(cr, cc));
    MatrixStore<Double> retVal = original;
    int nbRows = original.getRowDim();
    int nbCols = original.getColDim();
    if (nbRows > 1) {
        int half = (nbRows + 1) / 2;
        MatrixStore<Double> first = retVal.limits(half, -1);
        MatrixStore<Double> second = retVal.offsets(half, 0);
        retVal = second.below(first);
    }
    if (nbCols > 1) {
        int half = (nbCols + 1) / 2;
        MatrixStore<Double> first = retVal.limits(-1, half);
        MatrixStore<Double> second = retVal.offsets(0, half);
        retVal = second.right(first);
    }
    MatrixStore<Double> shifted2 = retVal;
    MatrixStore<Double> reverted = DiscreteFourierTransform.shift(shifted2);
    if (DEBUG) {
        BasicLogger.debugMatrix("Reverted " + r + "x" + c, reverted);
    }
    TestUtils.assertEquals(original, reverted);
}

```
TEST INPUT: `original`


# METHOD UNDER TEST
```java
/**
 * There is a symmetry in the DFT matrix. The first half of the rows (and columns) are the complex
 * conjugates of the second half. Furthermore, the first half correspond to positive frequencies, and the
 * second half to negative frequencies.
 * <p>
 * Re-arranging the elements of a matrix, shifting the first and second halves of the rows (and columns),
 * puts the zero-frequency term in the middle, and the conjugate pairs at equal distances from the centre.
 * <p>
 * This is useful when displaying the 2D DFT matrix as an image.
 * <p>
 * To revert the shift, simply call {@linkplain #shift(MatrixStore)} again. However, this will not work
 * correctly if there's an odd number of rows or columns. In that case the second call will not correctly
 * revert the position of the zero-frequency term – it will end up in the last row/column instead of in
 * the first.
 */
public static <N extends Comparablefive> MatrixStorefive shift(final MatrixStorefive matrix) {
    MatrixStorefive retVal = matrix;
    int nbRows = matrix.getRowDim();
    int nbCols = matrix.getColDim();
    if (nbRows > 1) {
        int half = (nbRows + 1) / 2;
        MatrixStorefive first = retVal.limits(half, -1);
        MatrixStorefive second = retVal.offsets(half, 0);
        retVal = second.below(first);
    }
    if (nbCols > 1) {
        int half = (nbCols + 1) / 2;
        MatrixStorefive first = retVal.limits(-1, half);
        MatrixStorefive second = retVal.offsets(0, half);
        retVal = second.right(first);
    }
    return retVal;
}

```


# REQUIRED DELIVERABLE
Construct five new values for the test input `original`. Each new input should explore valid values. Present the code for constructing each new input in the following format:
## New inputN:
```java
    Primitive64Store original = Primitive64Store.FACTORY.make(2, 2);
            original.set(i, j, i + j);
```

Provide the construction code for each of the five new test inputs, and explain why this input is valid. 