# Topic 19: Regular Expressions

## What a regex is for, and what it is NOT for
(Good uses, bad uses, which module to use instead for JSON/CSV/HTML/dates)

## re functions
| Function | Looks where | Returns |
|---|---|---|
| match | | |
| search | | |
| fullmatch | | |
| findall | | |
| finditer | | |
| sub / subn | | |
| split | | |
| compile | | |
| escape | | |

## Metacharacters
| Character | Meaning |
|---|---|

## Special sequences
| Sequence | Meaning |
|---|---|

## Groups
(Capturing, non-capturing, named, backreferences, what findall does with groups)

## Lookarounds
| Syntax | Meaning | Example |
|---|---|---|

## Greedy vs lazy
(Syntax for each, example with HTML tags, why [^>]+ can be better)

## Flags
| Flag | Effect |
|---|---|

## Match objects
(group, groups, groupdict, span, start, end, the None trap)

## Backtracking and safety
(What is catastrophic backtracking? Warning signs? How to protect a program?)

## Validation checklist
(fullmatch, then code for what a regex can't check)

## Regexes I wrote and what each does
| Task | Pattern |
|---|---|

## Errors I triggered
| Code | Error name | Why |
|---|---|---|

## Predictions I got wrong today

## Questions I still have

What is the difference between match, search, and fullmatch?
Why should regex patterns be raw strings?
What does findall return, and how does it change when the pattern has groups?
What is the difference between a capturing and a non-capturing group?
What is the difference between greedy and lazy quantifiers? Give an example.
What do \b, \B, \A, and \Z mean?
What are lookahead and lookbehind, and why must a lookbehind have a fixed width?
What do re.I, re.M, re.S, and re.X do?
What is catastrophic backtracking, and how can you avoid it?
How do you use a function as the replacement in re.sub?
Why cant a regular expression validate a date or an e-mail address completely?
When should you not use a regex?