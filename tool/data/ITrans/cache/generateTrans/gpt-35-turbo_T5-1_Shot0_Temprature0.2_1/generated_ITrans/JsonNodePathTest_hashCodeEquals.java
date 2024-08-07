package com.networknt.schema;

import java.util.ArrayList;
import java.util.Collections;
import java.util.stream.Collectors;
import org.junit.jupiter.api.Test;


import com.networknt.schema.JsonNodePath;
import com.networknt.schema.JsonNodePath.*;
import java.util.List;
import java.util.Arrays;

public class JsonNodePathTest_hashCodeEquals {
    public static JsonNodePath inputTransformation_hashCodeEquals(JsonNodePath a1)  {
        JsonNodePath a2 = new JsonNodePath(a1.getPathType());
        a2.setPathSegment(a1.getPathSegment());
        a2.setPathSegmentIndex(a1.getPathSegmentIndex());
        return a2;
    }
}