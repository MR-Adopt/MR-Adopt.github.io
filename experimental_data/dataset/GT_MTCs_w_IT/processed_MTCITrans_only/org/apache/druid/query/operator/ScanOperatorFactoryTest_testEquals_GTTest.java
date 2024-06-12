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

package org.apache.druid.query.operator;

import org.apache.druid.query.operator.ScanOperatorFactoryTest;
import org.apache.druid.query.operator.ScanOperatorFactoryTest.*;

import com.fasterxml.jackson.core.JsonProcessingException;
import com.fasterxml.jackson.databind.InjectableValues;
import com.fasterxml.jackson.databind.ObjectMapper;
import com.google.common.collect.ImmutableSet;
import org.apache.druid.common.config.NullHandling;
import org.apache.druid.jackson.DefaultObjectMapper;
import org.apache.druid.java.util.common.Intervals;
import org.apache.druid.java.util.common.StringUtils;
import org.apache.druid.math.expr.ExprMacroTable;
import org.apache.druid.query.expression.TestExprMacroTable;
import org.apache.druid.query.filter.DimFilter;
import org.apache.druid.query.filter.DimFilters;
import org.apache.druid.query.filter.InDimFilter;
import org.apache.druid.query.rowsandcols.RowsAndColumns;
import org.apache.druid.query.rowsandcols.TestRowsAndColumns;
import org.apache.druid.query.rowsandcols.semantic.RowsAndColumnsDecorator;
import org.apache.druid.query.rowsandcols.semantic.TestRowsAndColumnsDecorator;
import org.apache.druid.segment.VirtualColumns;
import org.apache.druid.segment.virtual.ExpressionVirtualColumn;
import org.joda.time.Interval;
import org.junit.Assert;
import org.junit.Test;

import javax.annotation.Nullable;
import java.io.Closeable;
import java.util.Arrays;
import java.util.Collections;
import java.util.List;

@SuppressWarnings("unchecked")
public class ScanOperatorFactoryTest_testEquals_GTTest
{
  static {
    NullHandling.initializeForTests();
  }

//   @Test
//   public void testEquals_h()
//   {
//     ScanOperatorFactoryTest_testEquals_GTTest.Builder bob = new ScanOperatorFactoryTest_testEquals_GTTest.Builder();
//     bob.timeRange = Intervals.utc(0, 6);
//     bob.filter = DimFilters.dimEquals("abc", "b");
//     bob.offsetLimit = OffsetLimit.limit(48);
//     bob.projectedColumns = Arrays.asList("a", "b");
//     bob.virtualColumns = VirtualColumns.EMPTY;
//     bob.ordering = Collections.singletonList(ColumnWithDirection.ascending("a"));
//     ScanOperatorFactory factory = bob.build();
//     ScanOperatorFactoryTest_testEquals_GTTest.Builder bob2 = (ScanOperatorFactoryTest_testEquals_GTTest.Builder) new ScanOperatorFactoryTest_testEquals_GTTest.Builder();
//     bob2.timeRange = Intervals.utc(0, 6);
//     bob2.filter = DimFilters.dimEquals("abc", "b");
//     bob2.offsetLimit = OffsetLimit.limit(48);
//     bob2.projectedColumns = Arrays.asList("a", "b");
//     bob2.virtualColumns = VirtualColumns.EMPTY;
//     bob2.ordering = null;
//     Assert.assertNotEquals(factory, bob2.build());
// 
//     Assert.assertEquals(factory, factory);
//     Assert.assertNotEquals(factory, new Object());
// 
//     Assert.assertNotEquals(factory, bob.copy().setTimeRange(null).build());
//     Assert.assertNotEquals(factory, bob.copy().setFilter(null).build());
//     Assert.assertNotEquals(factory, bob.copy().setOffsetLimit(null).build());
//     Assert.assertNotEquals(factory, bob.copy().setProjectedColumns(null).build());
//     Assert.assertNotEquals(factory, bob.copy().setVirtualColumns(null).build());
//     Assert.assertNotEquals(factory, bob.copy().setOrdering(null).build());
//   }
// 
// 
// //   public static ScanOperatorFactoryTest_testEquals_GTTest.Builder inputTransformation_testEquals(ScanOperatorFactoryTest_testEquals_GTTest.Builder bob) {
// //     ScanOperatorFactoryTest_testEquals_GTTest.Builder bob2 = bob.copy();
// //     bob2.setOrdering(null);
// //     return bob2;
// //   }
// // 
// // 
  @Test
  public void testEquals_IT()
  {
    ScanOperatorFactoryTest_testEquals_GTTest.Builder bob = new ScanOperatorFactoryTest_testEquals_GTTest.Builder();
    bob.timeRange = Intervals.utc(0, 6);
    bob.filter = DimFilters.dimEquals("abc", "b");
    bob.offsetLimit = OffsetLimit.limit(48);
    bob.projectedColumns = Arrays.asList("a", "b");
    bob.virtualColumns = VirtualColumns.EMPTY;
    bob.ordering = Collections.singletonList(ColumnWithDirection.ascending("a"));
    ScanOperatorFactory factory = bob.build();
    ScanOperatorFactoryTest_testEquals_GTTest.Builder bob2 = (ScanOperatorFactoryTest_testEquals_GTTest.Builder) ScanOperatorFactoryTest_testEquals_GT.inputTransformation_testEquals(bob);
    Assert.assertNotEquals(factory, bob2.build());

    Assert.assertEquals(factory, factory);
    Assert.assertNotEquals(factory, new Object());

    Assert.assertNotEquals(factory, bob.copy().setTimeRange(null).build());
    Assert.assertNotEquals(factory, bob.copy().setFilter(null).build());
    Assert.assertNotEquals(factory, bob.copy().setOffsetLimit(null).build());
    Assert.assertNotEquals(factory, bob.copy().setProjectedColumns(null).build());
    Assert.assertNotEquals(factory, bob.copy().setVirtualColumns(null).build());
    Assert.assertNotEquals(factory, bob.copy().setOrdering(null).build());
  }

  




  private static <T> void validateList(
      String msg,
      List<T> expectedList,
      List<T> actualList
  )
  {
    if (expectedList != null && expectedList.isEmpty()) {
      Assert.assertNull(msg, actualList);
    } else {
      Assert.assertEquals(msg, expectedList, actualList);
    }
  }

  public static class Builder
  {
    private Interval timeRange;
    private DimFilter filter;
    private OffsetLimit offsetLimit;
    private List<String> projectedColumns;
    private VirtualColumns virtualColumns;
    private List<ColumnWithDirection> ordering;

    public Builder setTimeRange(Interval timeRange)
    {
      this.timeRange = timeRange;
      return this;
    }

    public Builder setFilter(DimFilter filter)
    {
      this.filter = filter;
      return this;
    }

    public Builder setOffsetLimit(OffsetLimit offsetLimit)
    {
      this.offsetLimit = offsetLimit;
      return this;
    }

    public Builder setProjectedColumns(List<String> projectedColumns)
    {
      this.projectedColumns = projectedColumns;
      return this;
    }

    public Builder setVirtualColumns(VirtualColumns virtualColumns)
    {
      this.virtualColumns = virtualColumns;
      return this;
    }

    public Builder setOrdering(List<ColumnWithDirection> ordering)
    {
      this.ordering = ordering;
      return this;
    }

    private Builder copy()
    {
      Builder retVal = new Builder();
      retVal.timeRange = timeRange;
      retVal.filter = filter;
      retVal.offsetLimit = offsetLimit;
      retVal.projectedColumns = projectedColumns;
      retVal.virtualColumns = virtualColumns;
      retVal.ordering = ordering;
      return retVal;
    }

    private ScanOperatorFactory build()
    {
      return new ScanOperatorFactory(
          timeRange,
          filter,
          offsetLimit,
          projectedColumns,
          virtualColumns,
          ordering
      );
    }
  }
}