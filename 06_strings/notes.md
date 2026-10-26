# Topic 6: String Handling

## What a string is
(Immutable, ordered, Unicode, no char type)

## Representations
| Concept | Example | What it does |
|---|---|---|
| Escape sequences | | |
| Raw string | | |
| str() vs repr() | | |

## Unicode
(Code point vs encoding, UTF-8, str vs bytes, encode/decode, len in chars vs bytes)

## Methods I used today
| Group | Methods | One gotcha |
|---|---|---|
| Case | | |
| Search | | |
| Trim/pad | | |
| Split/join | | |
| Replace | | |
| Testing | | |

## Concatenation and repetition
(+, *, join vs +=, comparison rules)

## Indexing and slicing
(Index ranges, negative index, start:stop:step, why slicing never raises IndexError)

## Formatting
| Style | Example | When to use |
|---|---|---|
| f-string | | |
| str.format() | | |
| % | | |
| Template | | |

## Format spec cheat sheet
(.2f, >8, <8, ^8, 05d, comma, percent)

## Errors I triggered
| Code | Error name | Why |
|---|---|---|

## Predictions I got wrong today

## Questions I still have

Interview questions to answer in notes.md
Are Python strings mutable? How do you “change” a character?
What is the difference between find() and index()?
What does split() do differently from split(" ")?
How do you reverse a string and check for a palindrome?
Why is "".join() preferred over += in a loop?
What is the difference between str and bytes, and what do encode() and decode() do?
What is a raw string, and when would you use one?
What is the difference between str() and repr()?
Why does slicing never raise IndexError but indexing does?
Compare % formatting, str.format(), and f-strings.
Why does "-5".isdigit() return False?
What does "xxhixx".strip("x") do, and how is it different from removeprefix?