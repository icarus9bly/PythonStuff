# Zen of Python (https://towardsdatascience.com/how-to-be-pythonic-and-why-you-should-care-188d63a5037e)
    - Beautiful is better than ugly.
    - Explicit is better than implicit.
    - Simple is better than complex.
    - Complex is better than complicated.
    - Flat is better than nested.
    - Sparse is better than dense.
    - Readability counts.
    - Special cases aren’t special enough to break the rules.
    - Although practicality beats purity.
    - Errors should never pass silently.
    - Unless explicitly silenced.
    - In the face of ambiguity, refuse the temptation to guess.
    - There should be one — and preferably only one — obvious way to do it.
    - Although that way may not be obvious at first unless you’re Dutch.
    - Now is better than never.
    - Although never is often better than *right* now.
    - If the implementation is hard to explain, it’s a bad idea.
    - If the implementation is easy to explain, it may be a good idea.
    - Namespaces are one honking great idea — let’s do more of those!
```c
#include <stdbool.h>
char * arr[] = {"apples", "oranges", "bananas", "grapes"};
char * s = "cherries";
bool found = false;
int len = sizeof(arr) / sizeof(arr[0]);
for (int i = 0; i < len; i++) {
    if (!strcmp(arr[i], s)) {
        found = true;
    }
}
```

```python
# Unpythonic (Direct translation of the cwould be this)
arr = ["apples", "oranges", "bananas", "grapes"]
s = "cherries"
found = False
size = len(arr)
for i in range(0, size):
    if arr[i] == s:
        found = True
#Pythonic
arr = ["apples", "oranges", "bananas", "grapes"]
found = "cherries" in arr
```
