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

/**
 * 返回{@linkplain Version}的字符串形式。
 *
 * @param version
 * @return
 */
public static String stringOf(Version version) {
    return version.stringOf();
}

```


# TEST CASE
```java
@Test
public void stringOfTest() {
    String v = "1.0.0";
    String v1 = "1.0.0";
    Version version = Version.valueOf(v);
    Version version1 = Version.valueOf(v1);
    assertEquals(v, version.stringOf());
    assertEquals(v, Version.stringOf(version1));
}

```
SOURCE INPUT: `v`
FOLLOW UP INPUT: `version1`


# OTHER INPUT PAIRS 



# OUTPUT FORMAT
```java
public class VersionTest_stringOfTest {
 public static Version inputTransformation_stringOfTest(String version)  {
        // TODO
 Version version1 = 
		return version1;
 }
}
```
Your task is to deduce the relationship between 'SOURCE INPUT' and 'FOLLOW UP INPUT' in the test case, and create a function that transforms 'SOURCE INPUT' into 'FOLLOW UP INPUT'.
The deduced relation and generated transformation function should be applicable to additional input pairs and other potential input pairs with similar characteristics.
Generate the transformation function by complementing the above code skeleton in 'OUTPUT FORMAT'.