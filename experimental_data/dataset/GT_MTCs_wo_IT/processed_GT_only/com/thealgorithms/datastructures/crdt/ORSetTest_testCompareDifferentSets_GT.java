package com.thealgorithms.datastructures.crdt;

import com.thealgorithms.datastructures.crdt.ORSet;
import com.thealgorithms.datastructures.crdt.ORSet.*;

import static org.junit.jupiter.api.Assertions.*;

import java.util.Set;
import org.junit.jupiter.api.Test;

class ORSetTest_testCompareDifferentSets_GT {

    @Test
    void testCompareDifferentSets_h() {
        ORSet<String> orSet1 = new ORSet<>();
        ORSet<String> orSet2 = new ORSet<>();
        
        String element1 = "A";
        String element2 = "B";

        orSet1.add(element1);
        orSet2.add(element2);

        assertFalse(orSet1.compare(orSet2));
    }

    public static String inputTransformation_testCompareDifferentSets(String element1) {
        String element2 = element1+"B";
        return element2;
    }

    @Test
    void testCompareDifferentSets_IT() {
        ORSet<String> orSet1 = new ORSet<>();
        ORSet<String> orSet2 = new ORSet<>();
        
        String element1 = "A";
        String element2 = inputTransformation_testCompareDifferentSets(element1);

        orSet1.add(element1);
        orSet2.add(element2);

        assertFalse(orSet1.compare(orSet2));
    }

}