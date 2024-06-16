## New input1:
```java
    String v1 = "1.0-A1";
```
Explanation: This input is valid because it follows the version format "major.minor-build". The "-A1" part is considered as a build number and is optional.

## New input2:
```java
    String v1 = "1.1.0";
```
Explanation: This input is valid because it follows the version format "major.minor.revision". The ".revision" part is optional.

## New input3:
```java
    String v1 = "1.1.0-A1";
```
Explanation: This input is valid because it follows the version format "major.minor.revision-build". The "-build" part is optional.

## New input4:
```java
    String v1 = "1.0.0";
```
Explanation: This input is valid because it follows the version format "major.minor.revision". The ".minor" and ".revision" parts are optional.

## New input5:
```java
    String v1 = "1";
```
Explanation: This input is valid because it follows the version format "major.minor.revision". The ".minor" and ".revision" parts are optional, and "1" is a valid major version.
