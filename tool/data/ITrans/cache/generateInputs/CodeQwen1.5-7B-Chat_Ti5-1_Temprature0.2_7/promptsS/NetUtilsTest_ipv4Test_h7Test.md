# ORIGINAL TEST CASE
```java
@Test
public void ipv4Test() {
    String ipStr1 = NetUtils.LOCAL_LOOPBACK_IP;
    long ipLong = NetUtils.ipv4ToLong(ipStr1);
    long ipLong2 = 127000000001L;
    String ipStr2 = NetUtils.longToIpv4(ipLong2);
    Assert.assertEquals(ipStr2, ipStr1);
}

```
TEST INPUT: `ipStr1`


# METHOD UNDER TEST
```java
/**
 * 根据ip地址计算出long型的数据
 *
 * @param strIP IP V4 地址
 * @return long值
 */
public static long ipv4ToLong(String strIP) {
    if (isValidAddress(strIP)) {
        long[] ip = new long[4];
        // 先找到IP地址字符串中.的位置
        int position1 = strIP.indexOf(".");
        int position2 = strIP.indexOf(".", position1 + 1);
        int position3 = strIP.indexOf(".", position2 + 1);
        // 将每个.之间的字符串转换成整型
        ip[0] = Long.parseLong(strIP.substring(0, position1));
        ip[1] = Long.parseLong(strIP.substring(position1 + 1, position2));
        ip[2] = Long.parseLong(strIP.substring(position2 + 1, position3));
        ip[3] = Long.parseLong(strIP.substring(position3 + 1));
        return (ip[0] * 1_000_000_000) + (ip[1] * 1_000_000) + (ip[2] * 1_000) + ip[3];
    }
    return 0;
}

/**
 * 根据long值获取ip v4地址
 *
 * @param longIP IP的long表示形式
 * @return IP V4 地址
 */
public static String longToIpv4(long longIP) {
    final StringBuilder sb = new StringBuilder();
    // 直接右移24位
    sb.append((longIP / 1_000_000_000));
    sb.append(".");
    // 将高8位置0，然后右移16位
    sb.append(longIP / 1_000_000 % 1_000);
    sb.append(".");
    sb.append(longIP / 1_000 % 1_000);
    sb.append(".");
    sb.append(longIP % 1_000);
    return sb.toString();
}

```


# REQUIRED DELIVERABLE
Construct five new values for the test input `ipStr1`. Each new input should explore valid values. Present the code for constructing each new input in the following format:
## New inputN:
```java
    String ipStr1 = NetUtils.LOCAL_LOOPBACK_IP;
```

Provide the construction code for each of the five new test inputs, and explain why this input is valid. 