
## Line wrapping within a string (python):
- To wrap the line: use `() `outside of entire string; use `"` to end on line, add in `f`-string to start next wrapped- line.  **preferred**
- Another line-wrap option:  Use `"` to end first line, then `\`, and start new `f`-string:  
**Example:**
```
def summary(self):
        return (f"{self.name} is signed up for {self.get_num_classes} classes. "
            f"Here is a list of the courses: {self.course_list}")
```
```
        return f"{self.name} is signed up for {self.get_num_classes} classes. "\
            f"Here is a list of the courses: {self.course_list}"
```
