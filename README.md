# Python Exam Preparation With RBTree Context

This repository contains small Python exercises and exam-preparation examples. The main exam goal is Python practice, with Red-Black Trees used as the shared context.

The focus is on:

- basic Python: dictionaries, loops, conditions, lists, strings, files, and JSON
- recursive functions
- OOP: classes, `__init__`, attributes, properties, and methods
- only the RBTree logic needed to understand insertion, deletion, traversal, validation, and simple access methods

This is not meant to be a deep mathematical or theoretical study of trees and nodes. The tree tasks are mainly a way to practice writing correct Python code in the same style as the exercises.

## Workspace

- `simpleBinaryTree/`: nested dictionary tree and traversal basics.
- `classesBinaryTree/`: class-based tree nodes, insert logic, and visitor callbacks.
- `RBTree1/`: RBTree insertion, recoloring, and rotations.
- `RBTree2/`: RBTree deletion, transplant, successor, and delete fix cases.
- `RBTree3/`: RBTree save/load with flat JSON.
- `alte_klausure/`: old exam material used only to recognize likely Python-style task types.

## Exam Prep Files

- `notiz.md` is the quick guide. It lists every `catch_ohl/*.py` file and the methods inside it.
- `catch_ohl/` contains the detailed runnable examples. Each file focuses on one topic and keeps the code close to the original exercise style.

## How To Test

Run one example:

```bash
python3 catch_ohl/rb_access_methods.py
```

Compile all examples:

```bash
python3 -m py_compile catch_ohl/*.py
```
