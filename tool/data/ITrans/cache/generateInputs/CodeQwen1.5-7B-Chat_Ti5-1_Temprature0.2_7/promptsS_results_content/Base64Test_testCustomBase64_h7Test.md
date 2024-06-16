## New input1:
```java
    byte[] testDataBytes = {0x00, 0x01, 0x02, 0x03, 0x04, 0x05, 0x06, 0x07, 0x08, 0x09, 0x0A, 0x0B, 0x0C, 0x0D, 0x0E, 0x0F};
```
Explanation: This input consists of 16 bytes, each ranging from 0 to 15. This covers the entire range of possible single-byte values in the ASCII character set.

## New input2:
```java
    byte[] testDataBytes = {0x10, 0x20, 0x30, 0x40, 0x50, 0x60, 0x70, 0x80, 0x90, 0xA0, 0xB0, 0xC0, 0xD0, 0xE0, 0xF0};
```
Explanation: This input consists of 16 bytes, each ranging from 16 to 240. This covers the entire range of possible single-byte values in the ASCII character set, starting from the second octet.

## New input3:
```java
    byte[] testDataBytes = {0xFF, 0xFE, 0xFD, 0xFC, 0xFB, 0xFA, 0xF9, 0xF8, 0xF7, 0xF6, 0xF5, 0xF4, 0xF3, 0xF2, 0xF1};
```
Explanation: This input consists of 16 bytes, each ranging from 240 to 255. This covers the entire range of possible single-byte values in the ASCII character set, starting from the last octet.

## New input4:
```java
    byte[] testDataBytes = {0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00};
```
Explanation: This input consists of 16 bytes, all of which are 0. This covers the case where all bytes in the input are 0.

## New input5:
```java
    byte[] testDataBytes = {0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF};
```
Explanation: This input consists of 16 bytes, all of which are 255. This covers the case where all bytes in the input are 255.
