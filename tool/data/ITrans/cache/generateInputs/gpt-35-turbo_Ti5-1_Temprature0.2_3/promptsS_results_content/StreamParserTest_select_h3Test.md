## New input1:
```java
    StreamParser parser = new StreamParser(Parser.htmlParser()).parse("<title>One</title><p id=1>P One</p><p id=2>P Two</p>", "");
    String queryTitle = "p";
```
Explanation: In this test input, we are selecting the first matching element with the query "p". This is a valid input as it tests the functionality of the `expectFirst` method when searching for a specific element.

## New input2:
```java
    StreamParser parser = new StreamParser(Parser.htmlParser()).parse("<title>One</title><p id=1>P One</p><p id=2>P Two</p>", "");
    String queryTitle = "p[id=1]";
```
Explanation: In this test input, we are selecting the first matching element with the query "p[id=1]". This is a valid input as it tests the functionality of the `expectFirst` method when searching for a specific element with a specific attribute value.

## New input3:
```java
    StreamParser parser = new StreamParser(Parser.htmlParser()).parse("<title>One</title><p id=1>P One</p><p id=2>P Two</p>", "");
    String queryTitle = "p:contains(P One)";
```
Explanation: In this test input, we are selecting the first matching element with the query "p:contains(P One)". This is a valid input as it tests the functionality of the `expectFirst` method when searching for a specific element containing a specific text.

## New input4:
```java
    StreamParser parser = new StreamParser(Parser.htmlParser()).parse("<title>One</title><p id=1>P One</p><p id=2>P Two</p>", "");
    String queryTitle = "p:first-child";
```
Explanation: In this test input, we are selecting the first matching element with the query "p:first-child". This is a valid input as it tests the functionality of the `expectFirst` method when searching for the first child element of its parent.

## New input5:
```java
    StreamParser parser = new StreamParser(Parser.htmlParser()).parse("<title>One</title><p id=1>P One</p><p id=2>P Two</p>", "");
    String queryTitle = "p:nth-child(2)";
```
Explanation: In this test input, we are selecting the first matching element with the query "p:nth-child(2)". This is a valid input as it tests the functionality of the `expectFirst` method when searching for the second child element of its parent.