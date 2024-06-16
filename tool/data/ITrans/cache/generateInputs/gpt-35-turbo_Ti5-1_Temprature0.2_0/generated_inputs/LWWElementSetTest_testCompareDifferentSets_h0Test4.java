package com.thealgorithms.datastructures.crdt;

import com.thealgorithms.datastructures.crdt.LWWElementSet;
import com.thealgorithms.datastructures.crdt.LWWElementSet.*;
import static org.junit.jupiter.api.Assertions.*;
import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;

class LWWElementSetTest_testCompareDifferentSets_h0Test4 {

    private LWWElementSet set;

    private final Bias bias = Bias.ADDS;

    @BeforeEach
    void setUp() {
        set = new LWWElementSet();
    }

    @Test
    void testCompareDifferentSets_h0Test4() {
        LWWElementSet set = new LWWElementSet();
        LWWElementSet otherSet = new LWWElementSet();
Element element1 = new Element("key1", 1000, bias);
Element element2 = new Element("key2", 2, bias);
        set.add(element1);
        otherSet.add(element2);
        assertFalse(set.compare(otherSet));
    }
}

