package org.ojalgo.data.transform;

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


import org.ojalgo.data.transform.DiscreteFourierTransform;
import org.ojalgo.data.transform.DiscreteFourierTransform.*;
import java.util.List;
import java.util.Arrays;

public class DiscreteFourierTransformTest_testNonPowerOf2 {
    public static MatrixStore<ComplexNumber> inputTransformation_testNonPowerOf2(DiscreteFourierTransform transformer, PhysicalStore<Double> input) {
        MatrixStore<ComplexNumber> transformed2 = transformer.transform(input, DiscreteFourierTransform.DEFAULT, GenericStore.C128.makeDense(input.size(), 1));
        return transformed2;
    }
}