/*
 * Copyright (c) 2023 the original author or authors.
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 *      http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */
package com.networknt.schema;

import com.networknt.schema.JsonNodePath;
import com.networknt.schema.JsonNodePath.*;

import static org.junit.jupiter.api.Assertions.*;

import java.util.ArrayList;
import java.util.Collections;
import java.util.List;
import java.util.stream.Collectors;

import org.junit.jupiter.api.Test;

class JsonNodePathTest_hashCodeEqualsTest {

//     @Test
//     void hashCodeEquals_h() {
//         JsonNodePath root = new JsonNodePath(PathType.JSON_POINTER);
//         JsonNodePath a1 = root.append("a");
//         JsonNodePath a2 = root.append("a");
//         assertEquals(a1.hashCode(), a2.hashCode());
//     }
// 
// //     public static JsonNodePath inputTransformation_hashCodeEquals(JsonNodePath a1) {
// //         JsonNodePath a2 = new JsonNodePath(PathType.JSON_POINTER);
// //         // JsonNodePath a2 = a1;
// //         for (int i = 0; i < a1.getNameCount(); i++) {
// //             a2 = a2.append(a1.getName(i));
// //         }
// //         return a2;
// //     }
// // 
    @Test
    void hashCodeEquals_IT() {
        JsonNodePath root = new JsonNodePath(PathType.JSON_POINTER);
        JsonNodePath a1 = root.append("a");
        JsonNodePath a2 = JsonNodePathTest_hashCodeEquals.inputTransformation_hashCodeEquals(a1);
        assertEquals(a1.hashCode(), a2.hashCode());
    }

}