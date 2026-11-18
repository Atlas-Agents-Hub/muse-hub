# Generics and Type Parameters

## Basic Type Parameters

```go
package main

import (
    "cmp" // cmp.Ordered is in the standard library since Go 1.21
    "fmt"
)

// Generic function with type parameter
func MaxT cmp.Ordered T {
    if a > b {
        return a
    }
    return b
}

// Multiple type parameters
func MapT, U any U) []U {
    result := make([]U, len(slice))
    for i, v := range slice {
        result[i] = fn(v)
    }
    return result
}

// Usage
func main() {
    maxInt := Max(10, 20)           // T = int
    maxFloat := Max(3.14, 2.71)     // T = float64
    maxString := Max("abc", "xyz")  // T = string

    nums := []int{1, 2, 3}
    doubled := Map(nums, func(n int) int { return n * 2 })
    strings := Map(nums, func(n int) string { return fmt.Sprintf("%d", n) })
}
```

## Type Constraints

```go
// Integer and Float are not in the standard library: go get golang.org/x/exp
import "golang.org/x/exp/constraints"

type Number interface {
    constraints.Integer | constraints.Float
}

func SumT Number T {
    var total T
    for _, n := range numbers {
        total += n
    }
    return total
}

// Custom constraints with methods
type Stringer interface {
    String() string
}

func PrintAllT Stringer {
    for _, item := range items {
        fmt.Println(item.String())
    }
}

// Approximate constraint using ~
type Integer interface {
    ~int | ~int8 | ~int16 | ~int32 | ~int64
}

type MyInt int

func DoubleT Integer T {
    return n * 2
}

// Works with both int and MyInt
func main() {
    fmt.Println(Double(5))          // int
    fmt.Println(Double(MyInt(5)))   // MyInt
}
```

## Generic Data Structures

```go
// Generic Stack
type Stack[T any] struct {
    items []T
}

func NewStack[T any]() *Stack[T] {
    return &Stack[T]{
        items: make([]T, 0),
    }
}

func (s *Stack[T]) Push(item T) {
    s.items = append(s.items, item)
}

func (s *Stack[T]) Pop() (T, bool) {
    if len(s.items) == 0 {
        var zero T
        return zero, false
    }
    item := s.items[len(s.items)-1]
    s.items = s.items[:len(s.items)-1]
    return item, true
}

func (s *Stack[T]) IsEmpty() bool {
    return len(s.items) == 0
}

// Usage
intStack := NewStack[int]()
intStack.Push(1)
intStack.Push(2)

stringStack := NewStack[string]()
stringStack.Push("hello")
stringStack.Push("world")
```

## Generic Map Operations

```go
// Filter with generics
func FilterT any bool) []T {
    result := make([]T, 0, len(slice))
    for _, v := range slice {
        if predicate(v) {
            result = append(result, v)
        }
    }
    return result
}

// Reduce/Fold
func ReduceT, U any U) U {
    acc := initial
    for _, v := range slice {
        acc = fn(acc, v)
    }
    return acc
}

// Keys from map
func KeysK comparable, V any []K {
    keys := make([]K, 0, len(m))
    for k := range m {
        keys = append(keys, k)
    }
    return keys
}

// Values from map
func ValuesK comparable, V any []V {
    values := make([]V, 0, len(m))
    for _, v := range m {
        values = append(values, v)
    }
    return values
}

// Usage
numbers := []int{1, 2, 3, 4, 5, 6}
evens := Filter(numbers, func(n int) bool { return n%2 == 0 })

sum := Reduce(numbers, 0, func(acc, n int) int { return acc + n })

m := map[string]int{"a": 1, "b": 2}
keys := Keys(m)     // []string{"a", "b"}
values := Values(m) // []int{1, 2}
```

## Generic Pairs and Tuples

```go
// Generic Pair
type Pair[T, U any] struct {
    First  T
    Second U
}

func NewPairT, U any Pair[T, U] {
    return Pair[T, U]{First: first, Second: second}
}

func (p Pair[T, U]) Swap() Pair[U, T] {
    return Pair[U, T]{First: p.Second, Second: p.First}
}

// Usage
pair := NewPair("name", 42)
swapped := pair.Swap() // Pair[int, string]

// Generic Result type (like Rust's Result<T, E>)
type Result[T any] struct {
    value T
    err   error
}

func OkT any Result[T] {
    return Result[T]{value: value}
}

func ErrT any Result[T] {
    return Result[T]{err: err}
}

func (r Result[T]) IsOk() bool {
    return r.err == nil
}

func (r Result[T]) Unwrap() (T, error) {
    return r.value, r.err
}

func (r Result[T]) UnwrapOr(defaultValue T) T {
    if r.err != nil {
        return defaultValue
    }
    return r.value
}
```

## Comparable Constraint

```go
// Find using comparable
func FindT comparable (int, bool) {
    for i, v := range slice {
        if v == target {
            return i, true
        }
    }
    return -1, false
}

// Contains
func ContainsT comparable bool {
    _, found := Find(slice, target)
    return found
}

// Unique elements
func UniqueT comparable []T {
    seen := make(map[T]struct{})
    result := make([]T, 0, len(slice))

    for _, v := range slice {
        if _, exists := seen[v]; !exists {
            seen[v] = struct{}{}
            result = append(result, v)
        }
    }

    return result
}

// Usage
nums := []int{1, 2, 2, 3, 3, 4}
unique := Unique(nums) // []int{1, 2, 3, 4}

idx, found := Find([]string{"a", "b", "c"}, "b") // 1, true
```

## Generic Interfaces

```go
// Generic interface
type Container[T any] interface {
    Add(item T)
    Remove() (T, bool)
    Size() int
}

// Implementation
type Queue[T any] struct {
    items []T
}

func (q *Queue[T]) Add(item T) {
    q.items = append(q.items, item)
}

func (q *Queue[T]) Remove() (T, bool) {
    if len(q.items) == 0 {
        var zero T
        return zero, false
    }
    item := q.items[0]
    q.items = q.items[1:]
    return item, true
}

func (q *Queue[T]) Size() int {
    return len(q.items)
}

// Function accepting generic interface
func ProcessContainerT any {
    c.Add(item)
    fmt.Printf("Container size: %d\n", c.Size())
}
```

## Type Inference

```go
// Type inference works in most cases
func IdentityT any T {
    return x
}

// No need to specify type
result := Identity(42)          // T inferred as int
str := Identity("hello")        // T inferred as string

// Type inference with constraints
func MinT cmp.Ordered T {
    if a < b {
        return a
    }
    return b
}

// Inferred from arguments
minVal := Min(10, 20)           // T = int
minFloat := Min(1.5, 2.5)       // T = float64

// Explicit type when needed
result := Mapint, string string {
    return fmt.Sprintf("%d", n)
})
```

## Generic Channels

```go
// Generic channel operations
func MergeT any <-chan T {
    out := make(chan T)
    var wg sync.WaitGroup

    for _, ch := range channels {
        wg.Add(1)
        go func(c <-chan T) {
            defer wg.Done()
            for v := range c {
                out <- v
            }
        }(ch)
    }

    go func() {
        wg.Wait()
        close(out)
    }()

    return out
}

// Generic pipeline stage
func StageT, U any U) <-chan U {
    out := make(chan U)
    go func() {
        defer close(out)
        for v := range in {
            out <- fn(v)
        }
    }()
    return out
}

// Usage
ch1 := make(chan int)
ch2 := make(chan int)

merged := Merge(ch1, ch2)

numbers := make(chan int)
doubled := Stage(numbers, func(n int) int { return n * 2 })
strings := Stage(doubled, func(n int) string { return fmt.Sprintf("%d", n) })
```

## Union Constraints

```go
// Union of types
type StringOrInt interface {
    string | int
}

func ProcessT StringOrInt string {
    return fmt.Sprintf("%v", val)
}

// More complex unions
type Numeric interface {
    int | int8 | int16 | int32 | int64 |
    uint | uint8 | uint16 | uint32 | uint64 |
    float32 | float64
}

func AbsT Numeric T {
    if n < 0 {
        return -n
    }
    return n
}

// Union with methods
type Serializable interface {
    string | []byte
}

func SerializeT Serializable []byte {
    switch v := any(data).(type) {
    case string:
        return []byte(v)
    case []byte:
        return v
    default:
        panic("unreachable")
    }
}
```

## Quick Reference

| Feature | Syntax | Use Case |
|---------|--------|----------|
| Basic generic | `func F[T any]()` | Any type |
| Constraint | `func F[T Constraint]()` | Restricted types |
| Multiple params | `func F[T, U any]()` | Multiple type variables |
| Comparable | `func F[T comparable]()` | Types supporting == and != |
| Ordered | `func F[T cmp.Ordered]()` | Types supporting <, >, <=, >= |
| Union | `T interface{int \| string}` | Either type |
| Approximate | `~int` | Include type aliases |
