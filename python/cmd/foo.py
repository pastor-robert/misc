

# $ python my_prog_prompt.py
# (my_prog_prompt)> cmd1 subcmd1 subsubcmd1
# (my_prog_prompt)> cmd1 subcmd1 subsubcmd2
# (my_prog_prompt)> cmd1 subcmd2 subsubcmd1 -x -y
# (my_prog_prompt)> cmd2 subcmd1 
# (my_prog_prompt)> cmd2 subcmd1 
# (my_prog_prompt)> exit
# $

import cmd

class Command_main(cmd.Cmd):
    prompt = '(my_prog_prompt)> '

    class Command_cmd1(cmd.Cmd):
        def do_subcmd1(self, line):
            print repr(line)
        def do_subcmd2(self, line):
            print repr(line)
    command_cmd1 = Command_cmd1()

    class Command_cmd2(cmd.Cmd):
        def do_subcmd1(self, line):
            print repr(line)
    command_cmd2 = Command_cmd2()

    def do_cmd1(self, line):
        return self.command_cmd1.onecmd(line)
    def do_cmd2(self):
        return self.command_cmd1.onecmd(line)
    def do_exit(self, line):
        return True
    def do_EOF(self, line):
        print ''
        return True
    def postcmd(self, stop, line):
        return stop

if __name__=="__main__":
    shell = Command_main()
    shell.cmdloop()
