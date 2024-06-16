package com.thealgorithms.datastructures.crdt;

import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;


import com.thealgorithms.datastructures.crdt.LWWElementSet;
import com.thealgorithms.datastructures.crdt.LWWElementSet.*;
import java.util.List;
import java.util.Arrays;

public class LWWElementSetTest_testCompareDifferentSets {
    public static Element inputTransformation_testCompareDifferentSets(Element element1)  {
        Element element2 = new Element("key2", element1.value, element1.bias);
        return element2;
    }
}