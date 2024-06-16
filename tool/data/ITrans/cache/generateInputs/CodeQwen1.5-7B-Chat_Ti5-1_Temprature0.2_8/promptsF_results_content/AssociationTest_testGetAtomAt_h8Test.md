# REQUIRED DELIVERABLE
## New input pair0:
```java
    Atom c = new Atom("C");
    Atom o = new Atom("O");
    Atom n = new Atom("N");
    Association association = new Association(c, o);
    int position = 1;
    Association association2 = new Association(n, o);
    int position2 = 1;
```
## Explanation:
The inferred relation is that the `setAtomAt` method sets an Atom at a specific position in the `association` object, and the `getAtomAt` method retrieves the Atom at a specific position from the `association` object. Since the `setAtomAt` method sets the Atom at position 1, the `getAtomAt` method should retrieve the Atom at position 1 from the `association2` object. Therefore, the `position2` variable is set to 1 to satisfy the inferred relation.

## New input pair1:
```java
    Atom c = new Atom("C");
    Atom o = new Atom("O");
    Atom n = new Atom("N");
    Association association = new Association(c, o);
    int position = 2;
    Association association2 = new Association(n, o);
    int position2 = 2;
```
## Explanation:
The inferred relation is that the `setAtomAt` method sets an Atom at a specific position in the `association` object, and the `getAtomAt` method retrieves the Atom at a specific position from the `association` object. Since the `setAtomAt` method sets the Atom at position 2, the `getAtomAt` method should retrieve the Atom at position 2 from the `association2` object. Therefore, the `position2` variable is set to 2 to satisfy the inferred relation.

## New input pair2:
```java
    Atom c = new Atom("C");
    Atom o = new Atom("O");
    Atom n = new Atom("N");
    Association association = new Association(c, o);
    int position = -1;
    Association association2 = new Association(n, o);
    int position2 = -1;
```
## Explanation:
The inferred relation is that the `setAtomAt` method sets an Atom at a specific position in the `association` object, and the `getAtomAt` method retrieves the Atom at a specific position from the `association` object. Since the `setAtomAt` method does not allow setting an Atom at a negative position, the `getAtomAt` method should not retrieve an Atom at a negative position from the `association2` object. Therefore, the `position2` variable is set to -1 to satisfy the inferred relation.

## New input pair3:
```java
    Atom c = new Atom("C");
    Atom o = new Atom("O");
    Atom n = new Atom("N");
    Association association = new Association(c, o);
    int position = 3;
    Association association2 = new Association(n, o);
    int position2 = 3;
```
## Explanation:
The inferred relation is that the `setAtomAt` method sets an Atom at a specific position in the `association` object, and the `getAtomAt` method retrieves the Atom at a specific position from the `association` object. Since the `setAtomAt` method does not allow setting an Atom at a position greater than the number of atoms in the `association` object, the `getAtomAt` method should not retrieve an Atom at a position greater than the number of atoms in the `association2` object. Therefore, the `position2` variable is set to 3 to satisfy the inferred relation.

## New input pair4:
```java
    Atom c = new Atom("C");
    Atom o = new Atom("O");
    Atom n = new Atom("N");
    Association association = new Association(c, o);
    int position = 0;
    Association association2 = new Association(n, o);
    int position2 = 0;
```
## Explanation:
The inferred relation is that the `setAtomAt` method sets an Atom at a specific position in the `association` object, and the `getAtomAt` method retrieves the Atom at a specific position from the `association` object. Since the `setAtomAt` method sets the Atom at position 0, the `getAtomAt` method should retrieve the Atom at position 0 from the `association2` object. Therefore, the `position2` variable is set to 0 to satisfy the inferred relation.
