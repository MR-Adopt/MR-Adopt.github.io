package io.bootique.di;

import org.junit.jupiter.api.Test;
import java.util.Map;
import java.util.Set;


import io.bootique.di.TypeLiteral;
import io.bootique.di.TypeLiteral.*;
import java.util.List;
import java.util.Arrays;

public class TypeLiteralTest_normalize {
    public static TypeLiteral inputTransformation_normalize(Class input) {
        TypeLiteral<List<Integer>> input2 = TypeLiteral.listOf(input);
        return input2;
    }
}