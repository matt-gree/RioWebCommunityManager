from prompt_toolkit import prompt
from prompt_toolkit.completion import WordCompleter

from project_rio_lib.api_manager import APIManager
from project_rio_lib.web_caching import CompleterCache
from comm_manager_functions import community_functions, tag_functions, game_mode_functions, rio_mod_functions
from prompt_validators import OptionValidator
from api_parameters import APIParameter
from function_executer import ParameterProcessor

manager = APIManager()
cache = CompleterCache(manager)

formatted_text = '''
    ______ _         _    _      _       _____                            ___  ___                                  
    | ___ (_)       | |  | |    | |     /  __ \\                           |  \\/  |                                  
    | |_/ /_  ___   | |  | | ___| |__   | /  \\/ ___  _ __ ___  _ __ ___   | .  . | __ _ _ __   __ _  __ _  ___ _ __ 
    |    /| |/ _ \\  | |/\\| |/ _ \\ '_ \\  | |    / _ \\| '_ ` _ \\| '_ ` _ \\  | |\\/| |/ _` | '_ \\ / _` |/ _` |/ _ \\ '__|
    | |\\ \\| | (_) | \\  /\\  /  __/ |_) | | \\__/\\ (_) | | | | | | | | || |  | |  | | (_| | | | | (_| | (_| |  __/ |   
    \\_| \\_|_|\\___/   \\/  \\/ \\___|_.__/   \\____/\\___/|_| |_| |_|_| |_||_|  \\_|  |_|\\__,_|_| |_|\\__,_|\\__, |\\___|_|   
                                                                                                    __/  |          
                                                                                                    |___/           
    '''

print(formatted_text)

function_groups = {
    'Manage Communities': community_functions,
    'Manage Game Modes': game_mode_functions,
    'Manage Tags': tag_functions,
    'Rio Mod Functions': rio_mod_functions
}
print(f'\nMenu Options: ')
for key in function_groups.keys():
    print(f'    {key}')
print()

selected_function_group = prompt('What would you like to do: ',
                                 completer=WordCompleter(list(function_groups.keys()), ignore_case=True),
                                 validator=OptionValidator(list(function_groups.keys())))

print()
print(f'{selected_function_group}: ')
selected_function_group = function_groups[selected_function_group]

for key in selected_function_group:
    print(f'    {key}')
print()

selected_function_str = prompt('What would you like to do: ',
                                 completer=WordCompleter(list(selected_function_group.keys()), ignore_case=True),
                                 validator=OptionValidator(list(selected_function_group.keys())))

executor = ParameterProcessor()
selected_function = selected_function_group[selected_function_str]
function_args = executor.gather_function_args(selected_function.inputs)
    
function_args['api_manager'] = manager

if selected_function.constant_inputs:
    function_args = function_args | selected_function.constant_inputs

output = selected_function.func(**function_args)
if selected_function.parse_data:
    result = selected_function.parse_data(cache, output)
    if isinstance(result, (list, tuple, set)):  
        for item in result:
            print(item, '\n')
    else:
        print(result)
