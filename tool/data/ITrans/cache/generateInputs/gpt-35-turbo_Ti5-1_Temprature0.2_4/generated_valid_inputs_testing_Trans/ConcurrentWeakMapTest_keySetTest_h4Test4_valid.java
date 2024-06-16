/*
    This file is part of the iText (R) project.
    Copyright (c) 1998-2024 Apryse Group NV
    Authors: Apryse Software.

    This program is offered under a commercial and under the AGPL license.
    For commercial licensing, contact us at https://itextpdf.com/sales.  For AGPL licensing, see below.

    AGPL licensing:
    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU Affero General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU Affero General Public License for more details.

    You should have received a copy of the GNU Affero General Public License
    along with this program.  If not, see <https://www.gnu.org/licenses/>.
 */
package com.itextpdf.commons.datastructures;

import com.itextpdf.commons.datastructures.ConcurrentWeakMapTest_keySetTest;

import com.itextpdf.commons.datastructures.ConcurrentWeakMap;
import com.itextpdf.commons.datastructures.ConcurrentWeakMap.*;
import com.itextpdf.test.ExtendedITextTest;
import com.itextpdf.test.annotations.type.UnitTest;
import static org.junit.Assert.assertEquals;
import java.util.Collection;
import java.util.HashMap;
import java.util.Map;
import org.junit.Assert;
import org.junit.Test;
import org.junit.experimental.categories.Category;

@Category(UnitTest.class)
public class ConcurrentWeakMapTest_keySetTest_h4Test4_valid extends ExtendedITextTest {

    @Test
    public void keySetTest_h4Test4() {
    Map<Integer, Integer> anotherMap = new HashMap<>();
    anotherMap.put(-1, -2);
    anotherMap.put(-2, -3);
    anotherMap.put(-3, -4);
    ConcurrentWeakMap<Integer, Integer> map  = ConcurrentWeakMapTest_keySetTest.inputTransformation_keySetTest(anotherMap);
    map.put(-1, 6);
    map.put(-2, 6);
    map.put(-3, 6);
        Assert.assertEquals(anotherMap.keySet(), map.keySet());
    }
}

