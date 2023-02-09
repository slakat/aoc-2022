class Dir:
    def __init__(self, parent: 'Dir' = None):    
        self.parent: 'Dir' = parent
        self.filesize: int = 0
        self.dirs: dict = {} if parent else {"/": Dir(self)}
        self.size = None
    
    def part_1(self) -> int:
        size =  self.size if self.size <= 1e5 else 0
        return size + sum([x.part_1() for x in self.dirs.values()])
    
    def part_2(self, total: int = None) -> int:
        total = total if total else self.size
        size = self.size if 7e7 - total + self.size >= 3e7 else total
        return min([size, *[x.part_2(total) for x in self.dirs.values()]])
    
    def parse(self, datafile: str) -> 'Dir':
        cwd = self
        for line in open(datafile).readlines():
            args = line[:-1].split()
            if (args[0], args[1]) == ("$", "cd"):
                cwd = cwd.parent if args[2] == ".." else cwd.dirs[args[2]]
            elif args[0].isnumeric():
                cwd.filesize += int(args[0])
            elif args[0] == "dir":
                cwd.dirs[args[1]] = Dir(cwd)
        self.get_size()
        return self
    
    def get_size(self) -> int:
        dirsize = sum([d.get_size() for d in self.dirs.values()])
        self.size = self.filesize + dirsize
        return self.size
fs = Dir().parse("input.txt")
print(fs.part_1(), fs.part_2())