
/*
 * Licensed to ObjectStyle LLC under one
 * or more contributor license agreements.  See the NOTICE file
 * distributed with this work for additional information
 * regarding copyright ownership.  The ObjectStyle LLC licenses
 * this file to you under the Apache License, Version 2.0 (the
 * "License"); you may not use this file except in compliance
 * with the License.  You may obtain a copy of the License at
 *
 *   http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing,
 * software distributed under the License is distributed on an
 * "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
 * KIND, either express or implied.  See the License for the
 * specific language governing permissions and limitations
 * under the License.
 */

package io.bootique.di;

import io.bootique.di.Key;
import io.bootique.di.Key.*;

import org.junit.jupiter.api.Test;

import javax.inject.Qualifier;
import java.lang.annotation.Documented;
import java.lang.annotation.Retention;
import java.lang.annotation.RetentionPolicy;
import java.util.List;
import java.util.Map;

import static org.junit.jupiter.api.Assertions.*;

public class KeyTest_equalsTest {

//     @Test
//     public void equals_h() {
//         Class<?> type1 = String.class;
//         Class<?> type2 = String.class;
// 
//         Key<?> key1 = Key.get(type1);
//         Key<?> key2 = Key.get(type2);
//         Key<Integer> key3 = Key.get(Integer.class);
//         Key<Integer> key4 = Key.get(Integer.class, "a");
//         Key<Integer> key5 = Key.get(Integer.class, "a");
//         Key<Integer> key6 = Key.get(Integer.class, "b");
//         Key<String> key7 = Key.get(String.class, "a");
//         Key<Integer> key8 = Key.get(Integer.class, "");
// 
//         assertNull(key1.getBindingName());
//         assertTrue(key1.equals(key2));
// 
//         assertFalse(key1.equals(key3));
// 
//         assertTrue(key3.equals(key8));
//         assertNull(key3.getBindingName());
//         assertTrue(key8.equals(key3));
//         assertNull(key8.getBindingName());
// 
//         assertFalse(key3.equals(key4));
//         assertFalse(key4.equals(key3));
//         assertEquals("a", key4.getBindingName());
// 
//         assertTrue(key4.equals(key5));
//         assertEquals("a", key5.getBindingName());
//         assertTrue(key5.equals(key4));
// 
//         assertFalse(key5.equals(key6));
//         assertEquals("b", key6.getBindingName());
//         assertFalse(key6.equals(key5));
// 
//         assertFalse(key4.equals(key7));
//         assertEquals("a", key7.getBindingName());
//         assertFalse(key7.equals(key4));
//     }
// 
//     
// //     public static Class<?> inputTransformation_equals(Class<?> type1) {
// //         Class<?> type2 = type1.getClass().cast(type1);
// //         return type2;
// //     }
// // 
    @Test
    public void equals_IT() {
        Class<?> type1 = String.class;
        Class<?> type2 = KeyTest_equals.inputTransformation_equals(type1);

        Key<?> key1 = Key.get(type1);
        Key<?> key2 = Key.get(type2);
        Key<Integer> key3 = Key.get(Integer.class);
        Key<Integer> key4 = Key.get(Integer.class, "a");
        Key<Integer> key5 = Key.get(Integer.class, "a");
        Key<Integer> key6 = Key.get(Integer.class, "b");
        Key<String> key7 = Key.get(String.class, "a");
        Key<Integer> key8 = Key.get(Integer.class, "");

        assertNull(key1.getBindingName());
        assertTrue(key1.equals(key2));

        assertFalse(key1.equals(key3));

        assertTrue(key3.equals(key8));
        assertNull(key3.getBindingName());
        assertTrue(key8.equals(key3));
        assertNull(key8.getBindingName());

        assertFalse(key3.equals(key4));
        assertFalse(key4.equals(key3));
        assertEquals("a", key4.getBindingName());

        assertTrue(key4.equals(key5));
        assertEquals("a", key5.getBindingName());
        assertTrue(key5.equals(key4));

        assertFalse(key5.equals(key6));
        assertEquals("b", key6.getBindingName());
        assertFalse(key6.equals(key5));

        assertFalse(key4.equals(key7));
        assertEquals("a", key7.getBindingName());
        assertFalse(key7.equals(key4));
    }

    @Qualifier
    @Documented
    @Retention(RetentionPolicy.RUNTIME)
    @interface CustomQualifier {
    }
}