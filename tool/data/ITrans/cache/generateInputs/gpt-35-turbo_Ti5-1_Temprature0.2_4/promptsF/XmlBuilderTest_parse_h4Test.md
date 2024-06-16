# ORIGINAL TEST CASE
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


# NEW SOURCE INPUTS
## New source input0:
```java
    String XML = "<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n" + "<Projects>\n" + "  <underscore-java language=\"Java\" scm=\"SVN\">\n" + "    <Location type=\"URL\">https://github.com/javadev/underscore-java/</Location>\n" + "  </underscore-java>\n" + "  <JetS3t language=\"Java\" scm=\"CVS\">\n" + "    <Location type=\"URL\">https://jets3t.s3.amazonaws.com/index.html</Location>\n" + "  </JetS3t>\n" + "</Projects>";
```

## New source input1:
```java
    String XML = "<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n" + "<Projects>\n" + "  <underscore-java language=\"Java\" scm=\"Git\">\n" + "    <Location type=\"URL\">https://github.com/javadev/underscore-java/</Location>\n" + "  </underscore-java>\n" + "  <JetS3t language=\"Java\" scm=\"CVS\">\n" + "    <Location type=\"URL\">https://jets3t.s3.amazonaws.com/index.html</Location>\n" + "  </JetS3t>\n" + "</Projects>";
```

## New source input2:
```java
    String XML = "<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n" + "<Projects>\n" + "  <underscore-java language=\"Java\" scm=\"SVN\">\n" + "    <Location type=\"URL\">https://github.com/javadev/underscore-java/</Location>\n" + "  </underscore-java>\n" + "  <JetS3t language=\"Java\" scm=\"CVS\">\n" + "    <Location type=\"URL\">https://jets3t.s3.amazonaws.com/index.html</Location>\n" + "  </JetS3t>\n" + "<ApacheCommons language=\"Java\" scm=\"Git\">\n" + "    <Location type=\"URL\">https://github.com/apache/commons/</Location>\n" + "  </ApacheCommons>\n" + "</Projects>";
```

## New source input3:
```java
    String XML = "<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n" + "<Projects>\n" + "  <underscore-java language=\"Java\" scm=\"SVN\">\n" + "    <Location type=\"URL\">https://github.com/javadev/underscore-java/</Location>\n" + "  </underscore-java>\n" + "  <JetS3t language=\"Java\" scm=\"CVS\">\n" + "    <Location type=\"URL\">https://jets3t.s3.amazonaws.com/index.html</Location>\n" + "  </JetS3t>\n" + "<JetS3t language=\"Java\" scm=\"Git\">\n" + "    <Location type=\"URL\">https://github.com/javadev/jets3t/</Location>\n" + "  </JetS3t>\n" + "</Projects>";
```

## New source input4:
```java
    String XML = "<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n" + "<Projects>\n" + "  <underscore-java language=\"Java\" scm=\"SVN\">\n" + "    <Location type=\"URL\">https://github.com/javadev/underscore-java/</Location>\n" + "  </underscore-java>\n" + "  <JetS3t language=\"Java\" scm=\"CVS\">\n" + "    <Location type=\"URL\">https://jets3t.s3.amazonaws.com/index.html</Location>\n" + "  </JetS3t>\n" + "<underscore-java language=\"Java\" scm=\"Git\">\n" + "    <Location type=\"URL\">https://github.com/javadev/underscore-java/</Location>\n" + "  </underscore-java>\n" + "</Projects>";
```



# REQUIRED DELIVERABLE
For each new source input listed under 'NEW SOURCE INPUTS', please construct the corresponding follow-up input that satisfies your inferred relation and pass the assertions in the 'ORIGINAL TEST CASE'. Document the complete code for each new input pair in the format shown below:
## New input pairN:
```java
    String XML = "<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n" + "<Projects>\n" + "  <underscore-java language=\"Java\" scm=\"SVN\">\n" + "    <Location type=\"URL\">https://github.com/javadev/underscore-java/</Location>\n" + "  </underscore-java>\n" + "  <JetS3t language=\"Java\" scm=\"CVS\">\n" + "    <Location type=\"URL\">https://jets3t.s3.amazonaws.com/index.html</Location>\n" + "  </JetS3t>\n" + "</Projects>";
```

Additionally, for each new source input, provide the code used to generate the follow-up input along with its associated source input code. Please explain why this new input pair satisfies the inferred relation you have identified.