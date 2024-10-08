# ORIGINAL TEST CASE
```java
@Test
void select() throws IOException {
    StreamParser parser = new StreamParser(Parser.htmlParser()).parse("<title>One</title><p id=1>P One</p><p id=2>P Two</p>", "");
    String queryTitle = "title";
    Element title = parser.expectFirst(queryTitle);
    String queryTitle2 = "title";
    Element title2 = parser.selectFirst(queryTitle2);
    assertSame(title2, title);
// Element p1 = parser.expectNext("p");
// assertEquals("P One", p1.text());
// Element p2 = parser.expectNext("p");
// assertEquals("P Two", p2.text());
// Element pNone = parser.selectNext("p");
// assertNull(pNone);
}

```
TEST INPUT: `parser`,`queryTitle`


# METHOD UNDER TEST
```java
/**
 *     Just like {@link #selectFirst(String)}, but if there is no match, throws an {@link IllegalArgumentException}. This
 *     is useful if you want to simply abort processing on a failed match.
 *     @param query the {@link org.jsoup.select.Selector} query.
 *     @return the first matching element
 *     @throws IllegalArgumentException if no match is found
 *     @throws IOException if an I/O error occurs
 */
public Element expectFirst(String query) throws IOException {
    return (Element) Validate.ensureNotNull(selectFirst(query), "No elements matched the query '%s' in the document.", query);
}

/**
 *     Finds the first Element that matches the provided query. If the parsed Document does not already have a match, the
 *     input will be parsed until the first match is found, or the input is completely read.
 *     @param eval the {@link org.jsoup.select.Selector} evaluator.
 *     @return the first matching {@link Element}, or {@code null} if there's no match
 *     @throws IOException if an I/O error occurs
 */
@Nullable
public Element selectFirst(Evaluator eval) throws IOException {
    final Document doc = document();
    // run the query on the existing (partial) doc first, as there may be a hit already parsed
    Element first = doc.selectFirst(eval);
    if (first != null)
        return first;
    return selectNext(eval);
}

```


# REQUIRED DELIVERABLE
Construct five new values for the test input `parser`,`queryTitle`. Each new input should explore valid values. Present the code for constructing each new input in the following format:
## New inputN:
```java
    StreamParser parser = new StreamParser(Parser.htmlParser()).parse("<title>One</title><p id=1>P One</p><p id=2>P Two</p>", "");
    String queryTitle = "title";
```

Provide the construction code for each of the five new test inputs, and explain why this input is valid. 