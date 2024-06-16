package org.apache.druid.query.filter;

import com.fasterxml.jackson.core.JsonProcessingException;
import com.fasterxml.jackson.databind.ObjectMapper;
import nl.jqno.equalsverifier.EqualsVerifier;
import org.apache.druid.error.DruidException;
import org.apache.druid.jackson.DefaultObjectMapper;
import org.apache.druid.segment.column.ColumnType;
import org.apache.druid.testing.InitializedNullHandlingTest;
import org.junit.Assert;
import org.junit.Test;


import org.apache.druid.query.filter.IsFalseDimFilter;
import org.apache.druid.query.filter.IsFalseDimFilter.*;
import java.util.List;
import java.util.Arrays;

public class IsBooleanDimFilterTest_testGetCacheKey {
    public static EqualityFilter inputTransformation_testGetCacheKey(EqualityFilter f3)  {
        EqualityFilter f4 = new EqualityFilter(f3.getDimension(), f3.getType(), f3.getValue(), f3.getExtractionFn());
        return f4;
    }
}