/*
 * Copyright 1997-2023 Optimatika
 *
 * Permission is hereby granted, free of charge, to any person obtaining a copy
 * of this software and associated documentation files (the "Software"), to deal
 * in the Software without restriction, including without limitation the rights
 * to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
 * copies of the Software, and to permit persons to whom the Software is
 * furnished to do so, subject to the following conditions:
 *
 * The above copyright notice and this permission notice shall be included in
 * all copies or substantial portions of the Software.
 *
 * THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
 * IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
 * FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
 * AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
 * LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
 * OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
 * SOFTWARE.
 */
package org.ojalgo.data.transform;

import org.ojalgo.data.transform.DiscreteFourierTransform;
import org.ojalgo.data.transform.DiscreteFourierTransform.*;
import org.junit.jupiter.api.Test;
import org.ojalgo.TestUtils;
import org.ojalgo.function.constant.ComplexMath;
import org.ojalgo.function.constant.PrimitiveMath;
import org.ojalgo.function.polynomial.PolynomialR064;
import org.ojalgo.function.special.PowerOf2;
import org.ojalgo.matrix.MatrixC128;
import org.ojalgo.matrix.MatrixC128.DenseReceiver;
import org.ojalgo.matrix.store.MatrixStore;
import org.ojalgo.matrix.store.PhysicalStore;
import org.ojalgo.matrix.store.Primitive64Store;
import org.ojalgo.netio.BasicLogger;
import org.ojalgo.random.Uniform;
import org.ojalgo.scalar.ComplexNumber;
import org.ojalgo.structure.Access1D;
import org.ojalgo.type.context.NumberContext;
import org.ojalgo.matrix.store.GenericStore;

final class DiscreteFourierTransformTest_testShiftAndRevertEven_h4Test8 extends DataTransformTests {

    @Test
    public void testShiftAndRevertEven_h4Test8() {
        int c = 2;
        int r = 2;
    Primitive64Store original = Primitive64Store.FACTORY.make(0, 0);
        Primitive64Store original2 = Primitive64Store.FACTORY.make(2, 2);
        for (int j = 0; j < c; j++) {
            for (int i = 0; i < r; i++) {
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
}

