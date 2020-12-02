# iat-score

Compute IAT score & provide human readable feedback based on the score

## Installation

```
pip install iat-score
```

## Usage

```
scorer = Scorer('Male', 'Female', 'Family', 'Career')

d1 = scorer.score(data) # data is an array of dictionaries. See test/iat.json for sample data
print(d1)

feedback = scorer.feedback(d1)
print(feedback)
```
