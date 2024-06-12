package com.thealgorithms.datastructures.crdt;

import com.thealgorithms.datastructures.crdt.LWWElementSet;
import com.thealgorithms.datastructures.crdt.LWWElementSet.*;

import static org.junit.jupiter.api.Assertions.*;

import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;

class LWWElementSetTest_testRemoveTest {

    private LWWElementSet set;
    private final Bias bias = Bias.ADDS;

    @BeforeEach
    void setUp() {
        set = new LWWElementSet();
    }

//     @Test
//     void testRemove_h() {
//         Element element = new Element("key1", 1, bias);
//         Element element2 = new Element("key1", 1, bias);
//         set.add(element);
//         set.remove(element2);
// 
//         assertFalse(set.lookup(element));
//     }
// 
// //     public static Element inputTransformation_testRemove(Element element) {
// //         String key = element.key;
// //         int timestamp = element.timestamp;
// //         Bias bias = element.bias;
// //         Element element2 = new Element(key, timestamp, bias);
// //         return element2;
// //     }
// // 
    @Test
    void testRemove_IT() {
        Element element = new Element("key1", 1, bias);
        Element element2 = LWWElementSetTest_testRemove.inputTransformation_testRemove(element);
        set.add(element);
        set.remove(element2);

        assertFalse(set.lookup(element));
    }

}