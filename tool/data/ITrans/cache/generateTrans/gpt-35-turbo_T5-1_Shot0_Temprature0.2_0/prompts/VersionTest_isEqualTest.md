# METHOD UNDER TEST
```java
/**
 * 构建Version。
 * <p>
 * 1.0、1.0-A1、1.1.0、1.1.0-A1
 * </p>
 *
 * @param version
 * @return
 * @throws IllegalArgumentException
 */
public static Version valueOf(String version) throws IllegalArgumentException {
    if (!isValidVersion(version))
        throw new IllegalArgumentException("illegal version : " + version);
    String[] vs = version.split(SPLITTER_D_REGEX);
    String major = vs[0];
    String minor = (vs.length > 1 ? vs[1] : null);
    String revision = (vs.length > 2 ? vs[2] : null);
    String build = null;
    if (revision != null) {
        String[] bs = revision.split(SPLITTER_L_REGEX);
        revision = bs[0];
        build = (bs.length > 1 ? bs[1] : null);
    } else if (minor != null) {
        String[] bs = minor.split(SPLITTER_L_REGEX);
        minor = bs[0];
        build = (bs.length > 1 ? bs[1] : null);
    } else if (major != null) {
        String[] bs = major.split(SPLITTER_L_REGEX);
        major = bs[0];
        build = (bs.length > 1 ? bs[1] : null);
    }
    return new Version(major, minor, revision, build);
}

```


# TEST CASE
```java
@Test
public void isEqualTest() {
    String v1 = "1.0";
    String v2 = "1.10";
    String v3 = "1.0";
    Version a = Version.valueOf(v1);
    Version b = Version.valueOf(v2);
    Version c = Version.valueOf(v3);
    assertFalse(a.isEqual(b));
}

```
SOURCE INPUT: `v1`
FOLLOW UP INPUT: `v2`


# OTHER INPUT PAIRS 
## Input pair1:
```java
String v1 = "1.0";
String v2 = "1.10";
```

## Input pair2:
```java
String v1 = "1.0";
String v2 = "1.0-A1";
```

## Input pair3:
```java
String v1 = "1.0";
String v2 = "1.1.0";
```

## Input pair4:
```java
String v1 = "1.0";
String v2 = "1.1.0-A1";
```

## Input pair5:
```java
String v1 = "1.0";
String v2 = "2.0";
```

## Input pair6:
```java
String v1 = "1.0";
String v2 = "2.0-A1";
```

## Input pair7:
```java
String v1 = "1.0";
String v2 = "1.0.1";
```

## Input pair8:
```java
String v1 = "1.0";
String v2 = "1.1";
```



# OUTPUT FORMAT
```java
public class VersionTest_isEqualTest {
    public static String inputTransformation_isEqualTest(String version)  {
        // TODO
        String v2 = 
		return v2;
    }
}
```
Your task is to deduce the relationship between 'SOURCE INPUT' and 'FOLLOW UP INPUT' in the test case, and create a function that transforms 'SOURCE INPUT' into 'FOLLOW UP INPUT'.
The deduced relation and generated transformation function should be applicable to addtional input pairs and other potentail input pairs with similar characteristics.
Generate the transformation function by complementing the above code skeleton in 'OUTPUT FORMAT'.