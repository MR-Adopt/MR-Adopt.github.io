package com.thealgorithms.datastructures.crdt;

import com.thealgorithms.datastructures.crdt.LWWElementSet;
import com.thealgorithms.datastructures.crdt.LWWElementSet.*;

import static org.junit.jupiter.api.Assertions.*;

import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;

class LWWElementSetTest_testCompareDifferentSets_GTTest {

    private LWWElementSet set;
    private final Bias bias = Bias.ADDS;

    @BeforeEach
    void setUp() {
        set = new LWWElementSet();
    }

//     @Test
//     void testCompareDifferentSets_h() {
//         LWWElementSet set = new LWWElementSet();
//         LWWElementSet otherSet = new LWWElementSet();
// 
//         Element element1 = new Element("key1", 1, bias);
//         Element element2 = new Element("key2", 2, bias);
// 
//         set.add(element1);
//         otherSet.add(element2);
// 
//         assertFalse(set.compare(otherSet));
//     }
// 
// //     public static Element inputTransformation_testCompareDifferentSets(Element element1) {
// //         String key = element1.key + "1";
// //         int timestamp = element1.timestamp;
// //         Bias bias = element1.bias;
// // 
// //         Element element2 = new Element(key, timestamp+1, bias);
// //         return element2;
// //     }
// // 
    @Test
    void testCompareDifferentSets_IT() {
        LWWElementSet set = new LWWElementSet();
        LWWElementSet otherSet = new LWWElementSet();

        Element element1 = new Element("key1", 1, bias);
        Element element2 = LWWElementSetTest_testCompareDifferentSets_GT.inputTransformation_testCompareDifferentSets(element1);

        set.add(element1);
        otherSet.add(element2);

        assertFalse(set.compare(otherSet));
    }

}