package com.thealgorithms.datastructures.crdt;

import com.thealgorithms.datastructures.crdt.LWWElementSetTest_testRemove;

import com.thealgorithms.datastructures.crdt.LWWElementSet;
import com.thealgorithms.datastructures.crdt.LWWElementSet.*;
import static org.junit.jupiter.api.Assertions.*;
import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;

class LWWElementSetTest_testRemove_h0Test0_valid {

    private LWWElementSet set;

    private final Bias bias = Bias.ADDS;

    @BeforeEach
    void setUp() {
        set = new LWWElementSet();
    }

    @Test
    void testRemove_h0Test0() {
    Element element = new Element("key1", 0, bias);
    Element element2  = LWWElementSetTest_testRemove.inputTransformation_testRemove(element);
        set.add(element);
        set.remove(element2);
        assertFalse(set.lookup(element));
    }
}

