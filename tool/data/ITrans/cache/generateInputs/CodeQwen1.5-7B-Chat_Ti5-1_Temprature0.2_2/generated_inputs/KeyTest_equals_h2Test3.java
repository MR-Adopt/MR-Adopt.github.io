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

public class KeyTest_equals_h2Test3 {

    @Test
    public void equals_h2Test3() {

        Key<?> key1 = Key.get(type1);
        Key<?> key2 = Key.get(type2);
        Key<Integer> key3 = Key.get(Integer.class);
        Key<Integer> key4 = Key.get(Integer.class, "a");
        Key<Integer> key5 = Key.get(Integer.class, "a");
        Key<Integer> key6 = Key.get(Integer.class, "b");
        Key<String> key7 = Key.get(String.class, "a");
        Key<Integer> key8 = Key.get(Integer.class, "");
        assertTrue(key1.equals(key2));
    }

    @Qualifier
    @Documented
    @Retention(RetentionPolicy.RUNTIME)
    @interface CustomQualifier {
    }
}

