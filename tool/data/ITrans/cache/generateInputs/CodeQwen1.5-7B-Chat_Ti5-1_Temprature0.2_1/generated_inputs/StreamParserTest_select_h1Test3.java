package org.jsoup.parser;

import org.jsoup.parser.StreamParser;
import org.jsoup.parser.StreamParser.*;
import org.jsoup.helper.DataUtil;
import org.jsoup.integration.ParseTest;
import org.jsoup.nodes.Document;
import org.jsoup.nodes.Element;
import org.jsoup.nodes.Node;
import org.jsoup.select.Elements;
import org.junit.jupiter.api.Test;
import java.io.BufferedReader;
import java.io.File;
import java.io.IOException;
import java.io.InputStreamReader;
import java.nio.charset.StandardCharsets;
import java.nio.file.Files;
import java.util.Iterator;
import java.util.List;
import java.util.NoSuchElementException;
import static org.junit.jupiter.api.Assertions.*;

/**
 * Tests for the StreamParser. There are also some tests in {@link org.jsoup.integration.ConnectTest}.
 */
class StreamParserTest_select_h1Test3 {

    static void trackSeen(Element el, StringBuilder actual) {
        actual.append(el.tagName());
        if (el.hasAttr("id"))
            actual.append("#").append(el.id());
        if (!el.ownText().isEmpty())
            actual.append("[").append(el.ownText()).append("]");
        if (el.nextElementSibling() != null)
            actual.append("+");
        actual.append(";");
    }

    @Test
    void select_h1Test3() throws IOException {
    StreamParser parser = new StreamParser(Parser.htmlParser()).parse("<title>One</title><p id=1>P One</p><p id=2>P Two</p>", "");
    String queryTitle = "*";
    String queryTitle2 = "*";
        Element title = parser.expectFirst(queryTitle);
        Element title2 = parser.selectFirst(queryTitle2);
        assertSame(title2, title);
    // Element p1 = parser.expectNext("p");
    // assertEquals("P One", p1.text());
    // Element p2 = parser.expectNext("p");
    // assertEquals("P Two", p2.text());
    // Element pNone = parser.selectNext("p");
    // assertNull(pNone);
    }

    static StreamParser basic() {
        String html = "<div>One</div><div><p>Two</div>";
        StreamParser parser = new StreamParser(Parser.htmlParser()).parse(html, "");
        parser.parse(html, "");
        return parser;
    }

    static boolean isClosed(StreamParser streamer) {
        // a bit of a back door in!
        return getReader(streamer) == null;
    }

    private static CharacterReader getReader(StreamParser streamer) {
        return streamer.document().parser().getTreeBuilder().reader;
    }
}

