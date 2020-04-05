__SOLID design principles__:

1. **S**ingle responsibility - class should have only 1 responsibility
*each class should handle its own task; do not have different functionality in 1 class*
2. **O**pen-closed - classed should be open for extension but closed for modification 
*when there's a need to add functionality to working tested code, it's better to use inheritance (extend the class) 
instead of editing existing code; avoid making constant updates to tested code, use inheritance instead*
3. **L**iskov substitution - you should be able to substitute a base type for a subtype
4. **I**nterface segregation - split into separate interfaces
*if method is not going to be implemented for the object, it's better move the interface outside of the object class
and let object inherit only interface it uses; clients should not be forced to depend upon interfaces they do not use*
5. **D**ependency inversion - high level modules should not depend on low-level ones, use abstraction
*program to an interface not an implementation*