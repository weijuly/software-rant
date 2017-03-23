So, I was reading through promises and it took me a while to understand them to an extent. They allow us to sequence async callbacks in a neat order. To check my understanding on them, I though of writing a program with multiple / multi-level promises.

### Problem:
I have a file, `files.txt` that contains a list of file names. Each of the file listed contains some text. I want to read each of the file, count the number of words in them and sum it up across all files ( count of words in `ant.txt` + count of words in `bat.txt` + ... )

#### Constraint
I have to use promises.

### Implementation
1. Create a promise that returns a list of file paths
2. For each file, create a promise that reports the count of words in them
3. Wait for all promises to resolve, obtain the grand total and report it

I guess I kept my promise !
