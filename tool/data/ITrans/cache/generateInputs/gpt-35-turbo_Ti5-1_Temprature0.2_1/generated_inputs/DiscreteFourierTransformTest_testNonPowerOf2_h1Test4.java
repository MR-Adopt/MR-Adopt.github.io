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

final class DiscreteFourierTransformTest_testNonPowerOf2_h1Test4 extends DataTransformTests {

    @Test
    public void testNonPowerOf2_h1Test4() {
        NumberContext accuracy = NumberContext.of(8);
        for (int dimension = 2; dimension <= 16; dimension++) {
        PhysicalStore<Double> input = Primitive64Store.FACTORY.makeFilled(10, 1, Uniform.of(-2, 4));
        DiscreteFourierTransform transformer = DiscreteFourierTransform.newInstance(10);
        MatrixStore<ComplexNumber> transformed2 = GenericStore.C128.makeDense(input.size(), 1);
            MatrixStore<ComplexNumber> transformed = transformer.transform(input);
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
}

