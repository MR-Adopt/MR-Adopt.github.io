## New input1:
```java
    StreamParser parser = new StreamParser(Parser.htmlParser()).parse("<title>One</title><p id=1>P One</p><p id=2>P Two</p>", "");
    String queryTitle = "p";
```
Explanation: In this input, the queryTitle is set to "p", which matches the tag name of the first and second paragraph elements in the HTML document. This allows the test to verify that the `expectFirst` method correctly returns the first paragraph element.

## New input2:
```java
    StreamParser parser = new StreamParser(Parser.htmlParser()).parse("<title>One</title><p id=1>P One</p><p id=2>P Two</p>", "");
    String queryTitle = "#1";
```
Explanation: In this input, the queryTitle is set to "#1", which matches the id attribute of the first paragraph element in the HTML document. This allows the test to verify that the `expectFirst` method correctly returns the first paragraph element.

## New input3:
```java
    StreamParser parser = new StreamParser(Parser.htmlParser()).parse("<title>One</title><p id=1>P One</p><p id=2>P Two</p>", "");
    String queryTitle = "p#1";
```
Explanation: In this input, the queryTitle is set to "p#1", which matches both the tag name and the id attribute of the first paragraph element in the HTML document. This allows the test to verify that the `expectFirst` method correctly returns the first paragraph element.

## New input4:
```java
    StreamParser parser = new StreamParser(Parser.htmlParser()).parse("<title>One</title><p id=1>P One</p><p id=2>P Two</p>", "");
    String queryTitle = "title";
```
Explanation: In this input, the queryTitle is set to "title", which matches the tag name of the title element in the HTML document. This allows the test to verify that the `expectFirst` method correctly returns the title element.

## New input5:
```java
    StreamParser parser = new StreamParser(Parser.htmlParser()).parse("<title>One</title><p id=1>P One</p><p id=2>P Two</p>", "");
    String queryTitle = "nonexistent";
```
Explanation: In this input, the queryTitle is set to "nonexistent", which does not match any elements in the HTML document. This allows the test to verify that the `expectFirst` method correctly throws an `IllegalArgumentException` when no match is found.
