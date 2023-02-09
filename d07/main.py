# day 07

class Element(object):
    def __init__(self, parent, name, size):
        self.name = name
        self.parent = parent
        self.size = int(size)

    def get_name(self):
        return self.name

    def get_parent(self):
        return self.parent

    def get_size(self):
        return self.size

    def get_parent_name(self):

        if(self.parent == None):
            return ''
        else:
            r = self.parent.get_parent_name()
            return (r+'/'+self.parent.get_name())


class Folder(Element):

    def __init__(self, parent, name):
        Element.__init__(self, parent, name, 0)
        self.dirs = {}
        self.files = {}
        self.children = {}
        self.has_children = True
       
    def add_child(self,child):
        if (child.has_children):
            self.dirs[child.get_name()] = child
        else:
            self.files[child.get_name()] = child
        self.children[child.get_name()] = child
        self.add_size(child.get_size())
        # if(self.parent != None):
        #    self.parent.add_size(child.get_size())

    def add_size(self,size):
        self.size =  self.size + size

    def reset_children(self):
        self.children = {}
        if(self.parent != None):
            self.parent.add_size(-self.size)
        self.size = 0

    def calculate_size(self):
        dirsize = sum([self.dirs[d].get_size() for d in self.dirs.keys()])
        filesize = sum([self.files[d].get_size() for d in self.files.keys()])
        self.size = filesize + dirsize
        return self.size

    def get_child(self,name):
        if(child.has_children):
            return self.dirs[child]
        else:
            return self.files[child]


class File(Element):
    def __init__(self, parent, name, size):
            Element.__init__(self, parent, name, size)
            self.has_children = False


def cd_action(current_node,command):
    if( command == '/' ):
        current_node = current_node
    elif( command == '..' ):
        current_node = current_node.get_parent()
    else:
        name = command.split('.')[0]
        current_node = current_node.children[name]
    return current_node


file = "input.txt"

with open(file) as f:
    lines = f.readlines()

tree = Folder(None, 'root')
folders = []
current_node = tree

for i in lines:
    command = i.replace('\n','').split(' ')
    if(command[0]=='$'):
        if(command[1]=='cd'):
           temp = cd_action(current_node, command[2])
           current_node = temp
        elif(command[1]=='ls'):
            current_node.reset_children()
    else:
        if(command[0] == 'dir'):
            folder = Folder(current_node,command[1])
            current_node.add_child(folder)
            folders.append(folder)
        else:
            file = File(current_node,command[1], command[0])
            current_node.add_child(file)

total_size_selected = 0
for f in folders:
 if(f.get_size()<=100000):
    if(f.get_size()>0):
        total_size_selected = total_size_selected + f.calculate_size()
        print(f.get_name(), f.get_size())

print(total_size_selected)



