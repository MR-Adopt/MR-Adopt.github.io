/*
 * Licensed to the Apache Software Foundation (ASF) under one
 * or more contributor license agreements.  See the NOTICE file
 * distributed with this work for additional information
 * regarding copyright ownership.  The ASF licenses this file
 * to you under the Apache License, Version 2.0 (the
 * "License"); you may not use this file except in compliance
 * with the License.  You may obtain a copy of the License at
 *
 *   http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing,
 * software distributed under the License is distributed on an
 * "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
 * KIND, either express or implied.  See the License for the
 * specific language governing permissions and limitations
 * under the License.
 */
package org.apache.sysds.test.component.compress.util;

import org.apache.sysds.runtime.compress.utils.IntArrayList.*;
import static org.junit.Assert.assertEquals;
import static org.junit.Assert.assertTrue;
import java.util.Arrays;
import java.util.List;
import org.apache.sysds.runtime.compress.DMLCompressionException;
import org.apache.sysds.runtime.compress.utils.IntArrayList;
import org.junit.Test;
import org.sparkproject.dmg.pmml.False;

public class ArrayListTest_extract_h1Test1 {

    @Test
    public void extract_h1Test1() {
    IntArrayList a = new IntArrayList();
    boolean trimFlag = true;
    boolean trimFlag2 = true;
        a.appendValue(0);
        a.appendValue(1);
        a.appendValue(0);
        IntArrayList b = new IntArrayList();
        b.appendValue(0);
        b.appendValue(1);
        b.appendValue(0);
        int[] ex = a.extractValues(trimFlag);
        int[] et = b.extractValues(trimFlag2);
        assertTrue(ex.length >= et.length);
    }
}

