from cliff.commandmanager import CommandManager


def load_commands(command_manager: CommandManager):
    from .add import Add
    from .get import Get
    from .list import List
    from .update import Update
    from .remove import Remove
    
    command_manager.add_command('add', Add)
    command_manager.add_command('get', Get)
    command_manager.add_command('list', List)
    command_manager.add_command('update', Update)
    command_manager.add_command('remove', Remove)
