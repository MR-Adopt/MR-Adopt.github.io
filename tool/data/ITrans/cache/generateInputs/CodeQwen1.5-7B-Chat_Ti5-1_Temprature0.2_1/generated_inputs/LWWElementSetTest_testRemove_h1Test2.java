package com.thealgorithms.datastructures.crdt;

import com.thealgorithms.datastructures.crdt.LWWElementSet;
import com.thealgorithms.datastructures.crdt.LWWElementSet.*;
import static org.junit.jupiter.api.Assertions.*;
import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;

class LWWElementSetTest_testRemove_h1Test2 {

    private LWWElementSet set;

    private final Bias bias = Bias.ADDS;

    @BeforeEach
    void setUp() {
        set = new LWWElementSet();
    }

    @Test
    void testRemove_h1Test2() {
    Element element = new Element("key1", Integer.MIN_VALUE, bias);
    Element element2 = new Element("key1", Integer.MIN_VALUE, bias);
        set.add(element);
        set.remove(element2);
        assertFalse(set.lookup(element));
    }
}

