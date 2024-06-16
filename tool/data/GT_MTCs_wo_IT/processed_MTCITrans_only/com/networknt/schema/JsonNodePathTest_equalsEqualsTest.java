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

class JsonNodePathTest_equalsEqualsTest {

//     @Test
//     void equalsEquals_h() {
//         JsonNodePath root = new JsonNodePath(PathType.JSON_POINTER);
//         String token1 = "a";
//         String token2 = "a";
//         JsonNodePath a1 = root.append(token1);
//         JsonNodePath a2 = root.append(token2);
//         assertEquals(a1, a2);
//     }
// 
// //     public static String inputTransformation_equalsEquals(String token1) {
// //         String token2 = token1;
// //         return token2;
// //     }
// // 
    @Test
    void equalsEquals_IT() {
        JsonNodePath root = new JsonNodePath(PathType.JSON_POINTER);
        String token1 = "a";
        String token2 = JsonNodePathTest_equalsEquals.inputTransformation_equalsEquals(token1);
        JsonNodePath a1 = root.append(token1);
        JsonNodePath a2 = root.append(token2);
        assertEquals(a1, a2);
    }

    // todo
}