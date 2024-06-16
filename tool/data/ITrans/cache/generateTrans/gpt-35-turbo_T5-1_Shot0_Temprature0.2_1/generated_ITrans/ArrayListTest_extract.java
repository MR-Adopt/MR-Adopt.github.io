package org.apache.sysds.test.component.compress.util;

import static org.junit.Assert.assertEquals;
import static org.junit.Assert.assertTrue;
import org.apache.sysds.runtime.compress.DMLCompressionException;
import org.junit.Test;


import org.apache.sysds.runtime.compress.utils.IntArrayList;
import org.apache.sysds.runtime.compress.utils.IntArrayList.*;
import java.util.List;
import java.util.Arrays;

public class ArrayListTest_extract {
    public static List<Object> inputTransformation_extract(IntArrayList a, boolean trimFlag) {
        IntArrayList a2 = new IntArrayList();
        for (int i = a.size() - 1; i >= 0; i--) {
            a2.appendValue(a.get(i));
        }
        boolean trimFlag2 = !trimFlag;
        List<Object> transformed_inputs = Arrays.asList(a2, trimFlag2);
        return transformed_inputs;
    }
}