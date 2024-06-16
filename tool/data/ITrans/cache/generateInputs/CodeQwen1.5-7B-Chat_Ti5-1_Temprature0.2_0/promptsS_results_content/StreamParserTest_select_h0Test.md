## New input1:
```java
    StreamParser parser = new StreamParser(Parser.htmlParser()).parse("<title>One</title><p id=1>P One</p><p id=2>P Two</p>", "");
    String queryTitle = "p";
```
Explanation: This input is valid and boundary-case because it queries for all paragraph elements, which are present in the parsed document. The `expectFirst` method will return the first matching element, which is the first paragraph in this case.

## New input2:
```java
    StreamParser parser = new StreamParser(Parser.htmlParser()).parse("<title>One</title><p id=1>P One</p><p id=2>P Two</p>", "");
    String queryTitle = "h1";
```
Explanation: This input is valid and boundary-case because it queries for a non-existent heading element. The `expectFirst` method will throw an `IllegalArgumentException` as there are no heading elements in the parsed document.

## New input3:
```java
    StreamParser parser = new StreamParser(Parser.htmlParser()).parse("<title>One</title><p id=1>P One</p><p id=2>P Two</p>", "");
    String queryTitle = "";
```
Explanation: This input is valid and boundary-case because it queries for an empty string. The `expectFirst` method will throw an `IllegalArgumentException` as the query string is empty.

## New input4:
```java
    StreamParser parser = new StreamParser(Parser.htmlParser()).parse("<title>One</title><p id=1>P One</p><p id=2>P Two</p>", "");
    String queryTitle = "*";
```
Explanation: This input is valid and boundary-case because it queries for all elements. The `expectFirst` method will return the first matching element, which is the title in this case.

## New input5:
```java
    StreamParser parser = new StreamParser(Parser.htmlParser()).parse("<title>One</title><p id=1>P One</p><p id=2>P Two</p>", "");
    String queryTitle = "title, p";
```
Explanation: This input is valid and boundary-case because it queries for both title and paragraph elements. The `expectFirst` method will return the first matching element, which is the title in this case.
