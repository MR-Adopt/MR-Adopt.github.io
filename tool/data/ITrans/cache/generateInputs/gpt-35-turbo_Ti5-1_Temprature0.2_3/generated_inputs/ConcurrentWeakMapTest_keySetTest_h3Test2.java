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
public class ConcurrentWeakMapTest_keySetTest_h3Test2 extends ExtendedITextTest {

    @Test
    public void keySetTest_h3Test2() {
    Map<Integer, Integer> anotherMap = new HashMap<>();
    anotherMap.put(100, 200);
    anotherMap.put(200, 300);
    anotherMap.put(300, 400);
    ConcurrentWeakMap<Integer, Integer> map = new ConcurrentWeakMap<>();
    map.put(100, 6);
    map.put(200, 6);
    map.put(300, 6);
        Assert.assertEquals(anotherMap.keySet(), map.keySet());
    }
}

