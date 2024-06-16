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
SOURCE INPUT: `ipStr1`
FOLLOW UP INPUT: `ipLong2`


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


# NEW SOURCE INPUTS
## New source input0:
```java
    String ipStr1 = "192.168.0.1";
```

## New source input1:
```java
    String ipStr1 = "10.0.0.1";
```

## New source input2:
```java
    String ipStr1 = "172.16.0.1";
```

## New source input3:
```java
    String ipStr1 = "8.8.8.8";
```

## New source input4:
```java
    String ipStr1 = "255.255.255.255";
```



# REQUIRED DELIVERABLE
For each new source input listed under 'NEW SOURCE INPUTS', please construct the corresponding follow-up input that satisfies your inferred relation and pass the assertions in the 'ORIGINAL TEST CASE'. Document the complete code for each new input pair in the format shown below:
## New input pairN:
```java
    String ipStr1 = NetUtils.LOCAL_LOOPBACK_IP;
    long ipLong2 = 127000000001L;
```

Additionally, for each new source input, provide the code used to generate the follow-up input along with its associated source input code. Please explain why this new input pair satisfies the inferred relation you have identified.