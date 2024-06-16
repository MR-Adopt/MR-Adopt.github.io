# ORIGINAL TEST CASE
```java
@Test
void toJson() {
    String XML = "<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n" + "<Projects>\n" + "  <underscore-java language=\"Java\" scm=\"SVN\">\n" + "    <Location type=\"URL\">https://github.com/javadev/underscore-java/</Location>\n" + "  </underscore-java>\n" + "  <JetS3t language=\"Java\" scm=\"CVS\">\n" + "    <Location type=\"URL\">https://jets3t.s3.amazonaws.com/index.html</Location>\n" + "  </JetS3t>\n" + "</Projects>";
    String XML2 = "<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n" + "<Projects>\n" + "  <underscore-java language=\"Java\" scm=\"SVN\">\n" + "    <Location type=\"URL\">https://github.com/javadev/underscore-java/</Location>\n" + "  </underscore-java>\n" + "  <JetS3t language=\"Java\" scm=\"CVS\">\n" + "    <Location type=\"URL\">https://jets3t.s3.amazonaws.com/index.html</Location>\n" + "  </JetS3t>\n" + "</Projects>";
    XmlBuilder xmlBuilder = XmlBuilder.parse(XML);
    XmlBuilder xmlBuilder2 = XmlBuilder.parse(XML2);
    assertEquals(U.xmlToJson(XML), xmlBuilder2.toJson());
}

```
SOURCE INPUT: `XML`
FOLLOW UP INPUT: `xmlBuilder2`


# METHOD UNDER TEST
```java
public static XmlBuilder parse(String xml) {
    Map<String, Object> xmlData = U.fromXmlMap(xml);
    XmlBuilder xmlBuilder = new XmlBuilder(Xml.XmlValue.getMapKey(xmlData));
    xmlBuilder.setData(xmlData);
    return xmlBuilder;
}

public String toJson() {
    return U.toJson(data);
}

```


# NEW SOURCE INPUTS
## New source input0:
```java
    String XML = "<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n" + "<Projects>\n" + "  <underscore-java language=\"Java\" scm=\"SVN\">\n" + "    <Location type=\"URL\">https://github.com/javadev/underscore-java/</Location>\n" + "  </underscore-java>\n" + "  <JetS3t language=\"Java\" scm=\"CVS\">\n" + "    <Location type=\"URL\">https://jets3t.s3.amazonaws.com/index.html</Location>\n" + "  </JetS3t>\n" + "  <NewProject language=\"Python\" scm=\"Git\">\n" + "    <Location type=\"URL\">https://github.com/newproject/newproject/</Location>\n" + "  </NewProject>\n" + "</Projects>";
```

## New source input1:
```java
    String XML = "<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n" + "<Projects>\n" + "  <underscore-java language=\"Java\" scm=\"SVN\">\n" + "    <Location type=\"URL\">https://github.com/javadev/underscore-java/</Location>\n" + "  </underscore-java>\n" + "  <JetS3t language=\"Java\" scm=\"CVS\">\n" + "    <Location type=\"URL\">https://jets3t.s3.amazonaws.com/index.html</Location>\n" + "  </JetS3t>\n" + "  <NewProject language=\"Java\" scm=\"SVN\">\n" + "    <Location type=\"URL\">https://github.com/newproject/newproject/</Location>\n" + "  </NewProject>\n" + "</Projects>";
```



# REQUIRED DELIVERABLE
For each new source input listed under 'NEW SOURCE INPUTS', please construct the corresponding follow-up input that satisfies your inferred relation and pass the assertions in the 'ORIGINAL TEST CASE'. Document the complete code for each new input pair in the format shown below:
## New input pairN:
```java
    String XML = "<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n" + "<Projects>\n" + "  <underscore-java language=\"Java\" scm=\"SVN\">\n" + "    <Location type=\"URL\">https://github.com/javadev/underscore-java/</Location>\n" + "  </underscore-java>\n" + "  <JetS3t language=\"Java\" scm=\"CVS\">\n" + "    <Location type=\"URL\">https://jets3t.s3.amazonaws.com/index.html</Location>\n" + "  </JetS3t>\n" + "</Projects>";
```

Additionally, for each new source input, provide the code used to generate the follow-up input along with its associated source input code. Please explain why this new input pair satisfies the inferred relation you have identified.