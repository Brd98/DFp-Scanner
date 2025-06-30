import cmd

class MyNewCLI(cmd.Cmd):
    prompt = "hello!"
    intro = "Welcome to the DFp tool!"
    
    def do_hello(self, line):
        """Print a greeting."""
        print("Hello, World!")

    def do_quit(self, line):
        """Exit the CLI."""
        return True
# e


if __name__ == '__main__':
    MyNewCLI().cmdloop()
