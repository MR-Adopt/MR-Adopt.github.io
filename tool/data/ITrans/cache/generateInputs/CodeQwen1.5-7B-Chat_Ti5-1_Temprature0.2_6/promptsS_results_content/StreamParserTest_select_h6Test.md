## New input1:
```java
    StreamParser parser = new StreamParser(Parser.htmlParser()).parse("<title>One</title><p id=1>P One</p><p id=2>P Two</p>", "");
    String queryTitle = "p";
```
Explanation: This input is valid because it selects all paragraph elements in the document, which are `<p>P One</p>` and `<p>P Two</p>`.

## New input2:
```java
    StreamParser parser = new StreamParser(Parser.htmlParser()).parse("<title>One</title><p id=1>P One</p><p id=2>P Two</p>", "");
    String queryTitle = "h1";
```
Explanation: This input is valid because it selects all heading elements in the document, which is `<h1>One</h1>`.

## New input3:
```java
    StreamParser parser = new StreamParser(Parser.htmlParser()).parse("<title>One</title><p id=1>P One</p><p id=2>P Two</p>", "");
    String queryTitle = "div";
```
Explanation: This input is valid because it selects all div elements in the document, which is `<div></div>`.

## New input4:
```java
    StreamParser parser = new StreamParser(Parser.htmlParser()).parse("<title>One</title><p id=1>P One</p><p id=2>P Two</p>", "");
    String queryTitle = "a";
```
Explanation: This input is valid because it selects all anchor elements in the document, which is `<a href=""></a>`.

## New input5:
```java
    StreamParser parser = new StreamParser(Parser.htmlParser()).parse("<title>One</title><p id=1>P One</p><p id=2>P Two</p>", "");
    String queryTitle = "img";
```
Explanation: This input is valid because it selects all image elements in the document, which is `<img src="">`.
