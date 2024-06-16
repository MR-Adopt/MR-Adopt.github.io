package com.thealgorithms.datastructures.crdt;

import com.thealgorithms.datastructures.crdt.LWWElementSetTest_testCompareDifferentSets;

import com.thealgorithms.datastructures.crdt.LWWElementSet;
import com.thealgorithms.datastructures.crdt.LWWElementSet.*;
import static org.junit.jupiter.api.Assertions.*;
import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;

class LWWElementSetTest_testCompareDifferentSets_h2Test0_valid {

    private LWWElementSet set;

    private final Bias bias = Bias.ADDS;

    @BeforeEach
    void setUp() {
        set = new LWWElementSet();
    }

    @Test
    void testCompareDifferentSets_h2Test0() {
        LWWElementSet set = new LWWElementSet();
        LWWElementSet otherSet = new LWWElementSet();
Element element1 = new Element("key1", 1, bias);
Element element2  = LWWElementSetTest_testCompareDifferentSets.inputTransformation_testCompareDifferentSets(element1);
        set.add(element1);
        otherSet.add(element2);
        assertFalse(set.compare(otherSet));
    }
}

