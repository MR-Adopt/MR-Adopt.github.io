package com.github.underscore;

import static org.junit.jupiter.api.Assertions.assertEquals;
import static org.junit.jupiter.api.Assertions.assertFalse;
import static org.junit.jupiter.api.Assertions.assertThrows;
import static org.junit.jupiter.api.Assertions.assertTrue;
import org.junit.jupiter.api.Test;
import org.w3c.dom.Document;


import com.github.underscore.XmlBuilder;
import com.github.underscore.XmlBuilder.*;
import java.util.List;
import java.util.Arrays;

public class XmlBuilderTest_toJson {
    public static XmlBuilder inputTransformation_toJson(String XML) {
        XmlBuilder xmlBuilder = XmlBuilder.parse(XML);
        return xmlBuilder;
    }
}