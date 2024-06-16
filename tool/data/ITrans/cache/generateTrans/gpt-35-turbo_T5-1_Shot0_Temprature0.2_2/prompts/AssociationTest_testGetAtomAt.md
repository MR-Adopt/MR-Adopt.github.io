# METHOD UNDER TEST
```java
/**
 * Sets an Atom in this Association.
 *
 * @param   atom  The atom to be set
 * @param   position  The position in this Association where the atom is to be inserted
 *
 * @see     #getAtomAt
 */
public void setAtomAt(IAtom atom, int position) {
    atoms[position] = atom;
    notifyChanged();
}

/**
 * Returns an Atom from this Association.
 *
 * @param   position  The position in this bond where the atom is
 * @return            The atom at the specified position
 *
 * @see     #setAtomAt
 */
public IAtom getAtomAt(int position) {
    return atoms[position];
}

```


# TEST CASE
```java
@Test
void testGetAtomAt() {
    Atom c = new Atom("C");
    Atom o = new Atom("O");
    Atom n = new Atom("N");
    Association association = new Association(c, o);
    // Assertions.assertEquals(c, association.getAtomAt(0));
    // Assertions.assertEquals(o, association.getAtomAt(1));
    int position = 0;
    association.setAtomAt(n, position);
    Association association2 = new Association(n, o);
    int position2 = 0;
    Assertions.assertEquals(n, association2.getAtomAt(position2));
}

```
SOURCE INPUT: `association`,`n`,`position`
FOLLOW UP INPUT: `association2`,`position2`


# OTHER INPUT PAIRS 
## Input pair1:
```java
Atom c = new Atom("C");
Atom o = new Atom("O");
Atom n = new Atom("N");
Association association = new Association(c, o);
int position = 0;
Association association2 = new Association(n, o);
int position2 = 0;
```

## Input pair2:
```java
Atom c = new Atom("C");
Atom o = new Atom("O");
Atom n = new Atom("N");
Association association = new Association(c, o);
int position = 0;
association.setAtomAt(n, position);
Association association2 = new Association(n, o);
int position2 = 0;
```

## Input pair3:
```java
Atom c = new Atom("C");
Atom o = new Atom("O");
Atom n = new Atom("N");
Association association = new Association(c, o);
int position = 1;
Association association2 = new Association(c, n);
int position2 = 1;
```



# OUTPUT FORMAT
```java
public class AssociationTest_testGetAtomAt {
    public static List<Object> inputTransformation_testGetAtomAt(Association association, Atom n, int position)  {
        // TODO
        Association association2 = 
		int position2 = 
		List<Object> transformed_inputs = Arrays.asList(association2, position2);
		return transformed_inputs;
    }
}
```
Your task is to deduce the relationship between 'SOURCE INPUT' and 'FOLLOW UP INPUT' in the test case, and create a function that transforms 'SOURCE INPUT' into 'FOLLOW UP INPUT'.
The deduced relation and generated transformation function should be applicable to addtional input pairs and other potentail input pairs with similar characteristics.
Generate the transformation function by complementing the above code skeleton in 'OUTPUT FORMAT'.