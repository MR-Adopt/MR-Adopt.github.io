package com.thealgorithms.datastructures.crdt;

import com.thealgorithms.datastructures.crdt.ORSet;
import com.thealgorithms.datastructures.crdt.ORSet.*;
import static org.junit.jupiter.api.Assertions.*;
import java.util.Set;
import org.junit.jupiter.api.Test;

class ORSetTest_testCompareDifferentSets_h9Test3 {

    @Test
    void testCompareDifferentSets_h9Test3() {
        ORSet<String> orSet1 = new ORSet<>();
        ORSet<String> orSet2 = new ORSet<>();
String element1 = "E";
String element2 = "F";
        orSet1.add(element1);
        orSet2.add(element2);
        assertFalse(orSet1.compare(orSet2));
    }
}

