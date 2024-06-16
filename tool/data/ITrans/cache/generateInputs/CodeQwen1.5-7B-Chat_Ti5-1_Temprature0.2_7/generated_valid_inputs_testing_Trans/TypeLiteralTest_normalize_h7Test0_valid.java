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

import io.bootique.di.TypeLiteralTest_normalize;

import io.bootique.di.TypeLiteral;
import io.bootique.di.TypeLiteral.*;
import org.junit.jupiter.api.Test;
import java.util.List;
import java.util.Map;
import java.util.Set;
import static org.junit.jupiter.api.Assertions.*;

public class TypeLiteralTest_normalize_h7Test0_valid {

    @Test
    public void normalize_h7Test0() {
    Class input = String.class;
        TypeLiteral<List<Integer>> type1 = TypeLiteral.listOf(input);
        TypeLiteral<List<Integer>> type2 = new TypeLiteral<List<Integer>>() {
        };
        TypeLiteral<List<Integer>> input2  = TypeLiteralTest_normalize.inputTransformation_normalize(input);
        TypeLiteral<List<Integer>> type3 = TypeLiteral.normalize(input2);
        TypeLiteral<List<Integer>> type4 = TypeLiteral.normalize(type2);
        assertTypesEqual(type1, type3);
        assertEquals(type1, type3);
    }

    private static <T> TypeLiteral<List<T>> genericMethodForTest() {
        // Can't resolve variable type, should throw
        return new TypeLiteral<List<T>>() {
        };
    }

    private static void assertTypesEqual(TypeLiteral<?> literal1, TypeLiteral<?> literal2) {
        assertEquals(literal1.hashCode(), literal2.hashCode());
        assertEquals(literal1.toString(), literal2.toString());
        assertEquals(literal1, literal2);
    }

    private static void assertTypesNotEqual(TypeLiteral<?> literal1, TypeLiteral<?> literal2) {
        assertNotEquals(literal1.hashCode(), literal2.hashCode());
        assertNotEquals(literal1.toString(), literal2.toString());
        assertNotEquals(literal1, literal2);
    }
}

