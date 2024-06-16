package com.itextpdf.commons.datastructures;

import com.itextpdf.test.ExtendedITextTest;
import com.itextpdf.test.annotations.type.UnitTest;
import java.util.Collection;
import java.util.HashMap;
import java.util.Map;
import org.junit.Assert;
import org.junit.Test;
import org.junit.experimental.categories.Category;


import com.itextpdf.commons.datastructures.ConcurrentWeakMap;
import com.itextpdf.commons.datastructures.ConcurrentWeakMap.*;
import java.util.List;
import java.util.Arrays;

public class ConcurrentWeakMapTest_keySetTest {
    public static ConcurrentWeakMap<Integer, Integer> inputTransformation_keySetTest(Map<Integer, Integer> anotherMap) {
        ConcurrentWeakMap<Integer, Integer> map = new ConcurrentWeakMap<>();
        map.putAll(anotherMap);
        return map;
    }
}