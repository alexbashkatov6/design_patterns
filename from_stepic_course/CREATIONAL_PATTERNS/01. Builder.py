class CodeStr:
    def __init__(self, root_name):
        self.root_name = root_name
        self.code_strs = [f"class {self.root_name}:", "pass"]

    def __str__(self):
        return "\n  ".join(self.code_strs)


class CodeBuilder:
    def __init__(self, root_name):
        self.root_name = CodeStr(root_name)

    def add_field(self, type_, name):
        if "pass" in self.root_name.code_strs:
            self.root_name.code_strs.pop()
            self.root_name.code_strs.append("def __init__(self):")
        self.root_name.code_strs.append(f"  self.{type_} = {name}")
        return self

    def __str__(self):
        return str(self.root_name)


if __name__ == "__main__":
    cb = CodeBuilder('Person').add_field('name', '""').add_field('age', '0')
    print(cb)
