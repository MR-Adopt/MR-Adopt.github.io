# METHOD UNDER TEST
```java
public static XmlBuilder parse(String xml) {
    Map<String, Object> xmlData = U.fromXmlMap(xml);
    XmlBuilder xmlBuilder = new XmlBuilder(Xml.XmlValue.getMapKey(xmlData));
    xmlBuilder.setData(xmlData);
    return xmlBuilder;
}

public String asString() {
    return U.toXml(data);
}

```


# TEST CASE
```java
@Test
void parse() {
    String XML = "<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n" + "<Projects>\n" + "  <underscore-java language=\"Java\" scm=\"SVN\">\n" + "    <Location type=\"URL\">https://github.com/javadev/underscore-java/</Location>\n" + "  </underscore-java>\n" + "  <JetS3t language=\"Java\" scm=\"CVS\">\n" + "    <Location type=\"URL\">https://jets3t.s3.amazonaws.com/index.html</Location>\n" + "  </JetS3t>\n" + "</Projects>";
    String XML2 = "<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n" + "<Projects>\n" + "  <underscore-java language=\"Java\" scm=\"SVN\">\n" + "    <Location type=\"URL\">https://github.com/javadev/underscore-java/</Location>\n" + "  </underscore-java>\n" + "  <JetS3t language=\"Java\" scm=\"CVS\">\n" + "    <Location type=\"URL\">https://jets3t.s3.amazonaws.com/index.html</Location>\n" + "  </JetS3t>\n" + "</Projects>";
    XmlBuilder xmlBuilder = XmlBuilder.parse(XML);
    XmlBuilder xmlBuilder2 = XmlBuilder.parse(XML2);
    assertEquals(XML, xmlBuilder2.asString());
}

```
SOURCE INPUT: `XML`
FOLLOW UP INPUT: `xmlBuilder2`


# OTHER INPUT PAIRS 



# OUTPUT FORMAT
```java
public class XmlBuilderTest_parse {
    public static XmlBuilder inputTransformation_parse(String XML)  {
        // TODO
        XmlBuilder xmlBuilder2 = 
		return xmlBuilder2;
    }
}
```
Your task is to deduce the relationship between 'SOURCE INPUT' and 'FOLLOW UP INPUT' in the test case, and create a function that transforms 'SOURCE INPUT' into 'FOLLOW UP INPUT'.
The deduced relation and generated transformation function should be applicable to addtional input pairs and other potentail input pairs with similar characteristics.
Generate the transformation function by complementing the above code skeleton in 'OUTPUT FORMAT'.