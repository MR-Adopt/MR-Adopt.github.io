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

public class XmlBuilderTest_parse {
    public static XmlBuilder inputTransformation_parse(String XML)  {
        XmlBuilder xmlBuilder = XmlBuilder.parse(XML);
        String xmlString = xmlBuilder.asString();
        XmlBuilder xmlBuilder2 = XmlBuilder.parse(xmlString);
        return xmlBuilder2;
    }
}