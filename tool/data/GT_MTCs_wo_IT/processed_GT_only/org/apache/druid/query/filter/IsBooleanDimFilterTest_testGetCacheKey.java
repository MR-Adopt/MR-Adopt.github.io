/*
 * Licensed to the Apache Software Foundation (ASF) under one
 * or more contributor license agreements.  See the NOTICE file
 * distributed with this work for additional information
 * regarding copyright ownership.  The ASF licenses this file
 * to you under the Apache License, Version 2.0 (the
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

package org.apache.druid.query.filter;

import org.apache.druid.query.filter.IsFalseDimFilter;
import org.apache.druid.query.filter.IsFalseDimFilter.*;

import com.fasterxml.jackson.core.JsonProcessingException;
import com.fasterxml.jackson.databind.ObjectMapper;
import nl.jqno.equalsverifier.EqualsVerifier;
import org.apache.druid.error.DruidException;
import org.apache.druid.jackson.DefaultObjectMapper;
import org.apache.druid.segment.column.ColumnType;
import org.apache.druid.testing.InitializedNullHandlingTest;
import org.junit.Assert;
import org.junit.Test;

import java.util.Arrays;

public class IsBooleanDimFilterTest_testGetCacheKey extends InitializedNullHandlingTest
{
  @Test
  public void testGetCacheKey_h()
  {
    EqualityFilter f3 = new EqualityFilter("x", ColumnType.STRING, "hello", null);
    EqualityFilter f4 = new EqualityFilter("x", ColumnType.STRING, "hello", null);

    IsFalseDimFilter f1_3 = IsFalseDimFilter.of(f3);
    IsFalseDimFilter f1_4 = IsFalseDimFilter.of(f4);
   
    Assert.assertArrayEquals(f1_3.getCacheKey(), f1_4.getCacheKey());
  }

  public static EqualityFilter inputTransformation_testGetCacheKey(EqualityFilter f3) {
    String column = f3.getColumn();
    ColumnType matchValueType = f3.getMatchValueType();
    Object matchValue = f3.getMatchValue();
    FilterTuning filterTuning = f3.getFilterTuning();
    EqualityFilter f4 = new EqualityFilter(column, matchValueType, matchValue, filterTuning);
    return f4;
  }

  @Test
  public void testGetCacheKey_IT()
  {
    EqualityFilter f3 = new EqualityFilter("x", ColumnType.STRING, "hello", null);
    EqualityFilter f4 = inputTransformation_testGetCacheKey(f3);

    IsFalseDimFilter f1_3 = IsFalseDimFilter.of(f3);
    IsFalseDimFilter f1_4 = IsFalseDimFilter.of(f4);
   
    Assert.assertArrayEquals(f1_3.getCacheKey(), f1_4.getCacheKey());
  }


}